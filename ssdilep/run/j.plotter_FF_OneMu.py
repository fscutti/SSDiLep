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
        required_triggers  = ["HLT_mu24", "HLT_mu50"],
        get_prescales_lumi = True,
        key                = 'muons',
        )
    
    ## build and pt-sort objects
    ## ---------------------------------------
    loop += pyframe.algs.ListBuilder(
        prefixes = ['muon_','jet_'],
        keys = ['muons','jets'],
        )
    loop += pyframe.algs.AttachTLVs(
        keys = ['muons','jets'],
        )
    # just a decoration of particles ...
    loop += ssdilep.algs.vars.ParticlesBuilder(key='muons')
    
    ## build MET
    ## ---------------------------------------
    #loop += ssdilep.algs.met.METCLUS(
    #    prefix='metFinalClus',
    #    key = 'met_clus',
    #    )
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
    loop += ssdilep.algs.vars.DiJetVars(key_leptons='muons',key_jets='jets')   
    loop += ssdilep.algs.vars.JetsBuilder()
    
    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneMuon') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='LeadMuIsMedium') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuZ0SinTheta05') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuPt30') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuEta247') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='JetCleaning') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneTightJet') 
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuIsoBound15') 

    
    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
    
    # WARNING: no trigger correction available for HLT_mu24
    loop += ssdilep.algs.EvWeights.MuTrigSF(
            trig_list = ["HLT_mu50"],
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
    ## configure histograms
    ## ---------------------------------------
    hist_list = []
    hist_list += ssdilep.hists.MuFF_hists.hist_list
    #hist_list += ssdilep.hists.H2D_hists.hist_list
    
    
    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------
    ## before any selection
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F0',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoFixedCutTightTrackOnly',['MuSFFixedCutTightTrackOnlyMedium']],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F0',
            plot_all     = False,
            hist_list    = hist_list,
            do_var_check = True,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoNotFixedCutTightTrackOnly',['MuSFNotFixedCutTightTrackOnlyMedium']],
              ],
            )
    ## F1
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoFixedCutTightTrackOnly',['MuSFFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi27',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig3',None],
              ['METlow40',None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoNotFixedCutTightTrackOnly',['MuSFNotFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi27',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig10',None],
              ['METlow40',None],
              ],
            )
    
    ## F2
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F2',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoFixedCutTightTrackOnly',['MuSFFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi27',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig3',None],
              ['METlow50',None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F2',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoNotFixedCutTightTrackOnly',['MuSFNotFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi27',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig10',None],
              ['METlow50',None],
              ],
            )
    
    ## F3
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F3',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoFixedCutTightTrackOnly',['MuSFFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi27',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig3',None],
              ['METlow30',None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F3',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoNotFixedCutTightTrackOnly',['MuSFNotFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi27',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig10',None],
              ['METlow30',None],
              ],
            )
    
    ## F4
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F4',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoFixedCutTightTrackOnly',['MuSFFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi29',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig3',None],
              ['METlow40',None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F4',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoNotFixedCutTightTrackOnly',['MuSFNotFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi29',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig10',None],
              ['METlow40',None],
              ],
            )
    
    ## F5
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F5',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoFixedCutTightTrackOnly',['MuSFFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi25',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig3',None],
              ['METlow40',None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F5',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoNotFixedCutTightTrackOnly',['MuSFNotFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi25',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig10',None],
              ['METlow40',None],
              ],
            )
    
    ## F6
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F6',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoFixedCutTightTrackOnly',['MuSFFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi27',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig2',None],
              ['METlow40',None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F6',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoNotFixedCutTightTrackOnly',['MuSFNotFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi27',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig10',None],
              ['METlow40',None],
              ],
            )
    
    ## F7
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F7',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoFixedCutTightTrackOnly',['MuSFFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi27',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig4',None],
              ['METlow40',None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F7',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoNotFixedCutTightTrackOnly',['MuSFNotFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi27',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig10',None],
              ['METlow40',None],
              ],
            )
    
    
    ## F8
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F8',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoFixedCutTightTrackOnly',['MuSFFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi27',None],
              ['TightJetPt40',None],
              ['LeadMuD0Sig3',None],
              ['METlow40',None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F8',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['BVeto',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoNotFixedCutTightTrackOnly',['MuSFNotFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi27',None],
              ['TightJetPt40',None],
              ['LeadMuD0Sig10',None],
              ['METlow40',None],
              ],
            )

    ## F9
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NUM_F9',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['AtLeastOneBjet',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoFixedCutTightTrackOnly',['MuSFFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi27',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig3',None],
              ['METlow40',None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_DEN_F9',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['AtLeastOneBjet',None],
              ['SingleMuTriggerMatch',['GlobBJetSF','JVTSF','MuTrigSFMedium']],
              ['LeadMuTruthFilter',None],
              ['LeadMuIsoNotFixedCutTightTrackOnly',['MuSFNotFixedCutTightTrackOnlyMedium']],
              ['MuJetDphi27',None],
              ['TightJetPt35',None],
              ['LeadMuD0Sig10',None],
              ['METlow40',None],
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



