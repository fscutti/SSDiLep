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


    ## configure the list of triggers 
    ## with eventual prescales and puts a
    ## trig list to the store for later cutflow
    ## ---------------------------------------
    loop += ssdilep.algs.vars.BuildTrigConfig(
        required_triggers = ['HLT_mu26_ivarmedium','HLT_mu50'],
        key               = 'muons',
        )

    ## build and pt-sort objects
    ## ---------------------------------------
    loop += pyframe.algs.ListBuilder(
        prefixes = ['tau_','jet_','muon_'],
        keys = ['taus','jets','muons'],
        )
    loop += pyframe.algs.AttachTLVs(
        keys = ['taus','jets','muons'],
        )
    # just a decoration of particles ...
    loop += ssdilep.algs.vars.ParticlesBuilder(key='taus')
    loop += ssdilep.algs.vars.ParticlesBuilder(key='muons')


    # build tight jets here !!!

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
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneTau') 
    
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='LeadTauIsVeryLoose') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='EleVeto') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='MuVeto') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='SingleJetTrigger') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTauPt20') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='JetCleaning') 
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneTightJet') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneJet') 

    
    ## initialize and/or decorate objects
    ## ---------------------------------------
    loop += ssdilep.algs.vars.MuTauVars()   
    loop += ssdilep.algs.vars.JetsBuilder()

    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
   
    loop += ssdilep.algs.EvWeights.MuTrigSF(
            trig_list = ["HLT_mu26_ivarmedium","HLT_mu50"],
            mu_reco   = "Medium",
            key       = "MuTrigSFMedium",
            scale     = None,
            )

    # jet weights 
    loop += ssdilep.algs.EvWeights.GlobalBjet(
            key       = "GlobBJetSF",
            )
    loop += ssdilep.algs.EvWeights.GlobalJVT(
            key       = "JVTSF",
            )

    ## objects
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.ObjWeights.MuAllSF(
            mu_index      = 0,
            mu_iso        = "FixedCutTightTrackOnly",
            mu_reco       = "Medium",
            key           = "MuSFFixedCutTightTrackOnlyMedium",
            scale         = None,
            )

    ## configure histograms
    ## ---------------------------------------
    hist_list = []
    hist_list += ssdilep.hists.PtOnly_hists.hist_list
    
    
    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------
    
   
    ## F1
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['TauJetDphi27', None],
              ['LeadTauIsMedium', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['TauJetDphi27', None],
              ['LeadTauIsNotMedium', None],
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



