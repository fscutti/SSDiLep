#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
j.postprocessor.py
"""

## std modules
import os,re

## ROOT
import ROOT
ROOT.gROOT.SetBatch(True)

## my modules
import pyframe

## local modules
import ssdilep

#_____________________________________________________________________________
def analyze(config):
  
    ##-------------------------------------------------------------------------
    ## setup
    ##-------------------------------------------------------------------------
    config['tree']       = 'physics/nominal'
    config['do_var_log'] = True
    main_path = os.getenv('MAIN')
    
    ## build chain
    chain = ROOT.TChain(config['tree'])
    for fn in config['input']: chain.Add(fn)

    ##-------------------------------------------------------------------------
    ## systematics 
    ##-------------------------------------------------------------------------
    """
    pass systematics on the command line like this:
    python j.plotter.py --config="sys:SYS_UP"
    """
    config.setdefault('sys',None)
    systematic = config['sys']

    sys_somesys    = None

    if   systematic == None: pass
    elif systematic == 'SOMESYS_UP':      sys_somesys    = 'up'
    elif systematic == 'SOMESYS_DN':      sys_somesys    = 'dn'
    else: 
        assert False, "Invalid systematic %s!"%(systematic)


    ##-------------------------------------------------------------------------
    ## event loop
    ##-------------------------------------------------------------------------
    loop = pyframe.core.EventLoop(name='ssdilep',
                                  sampletype=config['sampletype'],
                                  samplename=config['samplename'],
                                  outfile=config['samplename']+".root",
                                  quiet=False,
                                  )

    print config['samplename']

    single_tau_triggers = [
         #'HLT_tau80_medium1_tracktwo_L1TAU60',   
         #'HLT_tau125_medium1_tracktwo',           
         'HLT_tau160_medium1_tracktwo',          
         #'HLT_tau160_medium1_tracktwo_L1TAU100', 
        ]

    ditau_triggers = [
         'HLT_tau35_medium1_tracktwo_tau25_medium1_tracktwo_L1TAU20IM_2TAU12IM',    # 2015 only
         'HLT_tau80_medium1_TAU60_tau50_medium1_L1TAU12',                           # 2016 only
         'HLT_tau35_medium1_tracktwo_tau25_medium1_tracktwo',                       # 2016 only (with L1_J25)
         'HLT_tau80_medium1_tracktwo_L1TAU60_tau60_medium1_tracktwo_L1TAU40',       # 2017 only
         'HLT_tau35_medium1_tracktwo_tau25_medium1_tracktwo_L1DR-TAU20ITAU12I-J25', # 2017 only (with L1_J25)
        ]

    ## configure the list of triggers 
    ## with eventual prescales and puts a
    ## trig list to the store for later cutflow
    ## ---------------------------------------
    loop += ssdilep.algs.vars.BuildTrigConfig(
        required_triggers = single_tau_triggers,
                             key               = 'taus',
                             )

    ## build and pt-sort objects
    ## ---------------------------------------
    loop += pyframe.algs.ListBuilder(
        prefixes = ['tau_','jet_','muon_','el_'],
        keys = ['taus','jets','muons','electrons'],
        )
    loop += pyframe.algs.AttachTLVs(
        keys = ['taus','jets','muons','electrons'],
        )
    # just a decoration of particles ...
    loop += ssdilep.algs.vars.ParticlesBuilder(
        key='taus',
        )

    ## build MET
    ## ---------------------------------------
    loop += ssdilep.algs.met.METTRK(
        prefix='metFinalTrk',
        key = 'met_trk',
        )

    ## start preselection cutflow 
    ## ---------------------------------------
    loop += pyframe.algs.CutFlowAlg(key='presel')
    
    ## filter weights
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.EvWeights.MCEventWeight(cutflow='presel',key='weight_mc_event')
    loop += ssdilep.algs.EvWeights.Pileup(cutflow='presel',key='weight_pileup')
   
    
    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='TwoTaus') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTausEleBDTMedium') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='EleVeto') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='MuVeto') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='SingleTauTrigger') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTauPt20') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='JetCleaning') 


    ## initialize and/or decorate objects
    ## ---------------------------------------
    loop += ssdilep.algs.vars.DiTauVars(key_leptons='taus',
                                        key_jets='jets',
                                        build_tight_jets=True,
                                        )   
    
    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
    
    # jet weights 
    loop += ssdilep.algs.EvWeights.GlobalBjet(
            key       = "GlobBJetSF",
            )
    loop += ssdilep.algs.EvWeights.GlobalJVT(
            key       = "JVTSF",
            )
    
    loop += ssdilep.algs.EvWeights.TauTrigSF(
            trig_list    = single_tau_triggers,
            tau_index    = 0,
            tau_eolr     = "Medium",
            tau_id       = "Medium",
            key          = "LeadTauTrigSF",
            scale        = None,
            )

    ## objects
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.ObjWeights.TauAllSF(
            tau_index    = 0,
            tau_eolr     = "Medium",
            tau_id       = "Medium",
            key          = "Tau0AllSF",
            scale        = None,
            )
    loop += ssdilep.algs.ObjWeights.TauAllSF(
            tau_index    = 1,
            tau_eolr     = "Medium",
            tau_id       = "Medium",
            key          = "Tau1AllSF",
            scale        = None,
            )

    # add Fake-factors here


    ## configure histograms
    ## ---------------------------------------
    hist_list = []
    hist_list += ssdilep.hists.OneTauPairVR_hists.hist_list
    #hist_list += ssdilep.hists.H2D_hists.hist_list
    #hist_list += ssdilep.hists.PtOnly_hists.hist_list
    
    
    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------
    
   
    ## OS Z+jet CR
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSZ_TT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSTaus',['LeadTauTrigSF']],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['DiTauDphi27',None],
              ['TauPPMedium',['Tau0AllSF','Tau1AllSF']],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSZ_TL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSTaus',['LeadTauTrigSF']],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['DiTauDphi27',None],
              ['TauPFMedium',['Tau0AllSF']],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSZ_LT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSTaus',['LeadTauTrigSF']],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['DiTauDphi27',None],
              ['TauFPMedium',['Tau1AllSF']],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSZ_LL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSTaus',['LeadTauTrigSF']],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['DiTauDphi27',None],
              ['TauFFMedium',None],
              ],
            )
    
    loop += pyframe.algs.HistCopyAlg()

    ##-------------------------------------------------------------------------
    ## run the job
    ##-------------------------------------------------------------------------
    loop.run(chain, 
             min_entry=config['minentry'], 
             max_entry=config['maxentry'],
             #min_entry=0, 
             #max_entry=config['events'],
             branches_on_file = config.get('branches_on_file'),
             do_var_log = config.get('do_var_log'),
             )
    
    
#______________________________________________________________________________
if __name__ == '__main__':
    pyframe.config.main(analyze)



