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
        #required_triggers = ['HLT_mu26_ivarmedium','HLT_mu50'],
        required_triggers  = ['HLT_mu24','HLT_mu50'],
        get_prescales_lumi = True,
        key                = 'muons',
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
    loop += ssdilep.algs.EvWeights.TrigPresc(cutflow='presel',particles="muons",key="weight_data_unpresc")
   
    ## initialize and/or decorate objects
    ## ---------------------------------------

    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneTau') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneMuon') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='LeadMuIsMedium') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuZ0SinTheta05') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='LeadMuIsoNotFixedCutTightTrackOnly') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuEta247') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='LeadTauIsVeryLoose') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='EleVeto') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='SingleMuTriggerMatch') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTauPt20') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='JetCleaning') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='MuTauDphi27') 

    loop += ssdilep.algs.vars.MuTauVars()   
    loop += ssdilep.algs.vars.JetsBuilder()
    
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='LeadMuTruthFilter') 
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='METlow40') 

    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
   
    loop += ssdilep.algs.EvWeights.MuTrigSF(
            #trig_list = ["HLT_mu26_ivarmedium","HLT_mu50"],
            trig_list = ["HLT_mu24","HLT_mu50"],
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
            mu_iso        = "NotFixedCutTightTrackOnly",
            mu_reco       = "Medium",
            key           = "MuSFNotFixedCutTightTrackOnlyMedium",
            scale         = None,
            )
    loop += ssdilep.algs.ObjWeights.MuAllSF(
            mu_index      = 0,
            mu_iso        = "FixedCutTightTrackOnly",
            mu_reco       = "Medium",
            key           = "MuSFFixedCutTightTrackOnlyMedium",
            scale         = None,
            )
    loop += ssdilep.algs.ObjWeights.TauAllSF(
            tau_index    = 0,
            tau_eolr     = "Medium",
            tau_id       = "Medium",
            key          = "Tau0AllSF",
            scale        = None,
            )

    # Tau fake-factors 
    loop += ssdilep.algs.ObjWeights.TauFakeFactorGraph(
            config_file = [
                           os.path.join(main_path,'ssdilep/data/sys_ff_taulead_pt_fullSYS_MediumTau1P.root'),
                           os.path.join(main_path,'ssdilep/data/sys_ff_taulead_pt_fullSYS_MediumTau3P.root'),
                           ],
            tau_index   = 0,
            key         = 'Tau0FF',
            scale       = None,
            )

    ## configure histograms
    ## ---------------------------------------
    hist_list = []
    hist_list += ssdilep.hists.MuTauVR_hists.hist_list
    
    
    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------
    
    ## Di-jet VR
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'DJ_PP',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['LeadTauIsMedium',['MuTrigSFMedium','MuSFNotFixedCutTightTrackOnlyMedium','Tau0AllSF','GlobBJetSF','JVTSF']],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'DJ_PF',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['LeadTauIsMedium',['MuTrigSFMedium','MuSFNotFixedCutTightTrackOnlyMedium','Tau0AllSF','GlobBJetSF','JVTSF','Tau0FF']],
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



