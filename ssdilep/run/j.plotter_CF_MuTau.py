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

    ## getting metadata histograms
    metadata_dict = {}
    
    inf = ROOT.TFile(config['input'][0],"READ")
    for obj in inf.GetListOfKeys():
      if "MetaData" in obj.GetName():
        h = inf.Get(obj.GetName()).Clone()
        metadata_dict[h.GetName()] = h

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

    # building pairs with combinations of leptons
    loop += ssdilep.algs.vars.PairsBuilder(key=['taus','muons'])

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
    loop += ssdilep.algs.EvWeights.MCEventWeight(cutflow='presel',metadata=metadata_dict,key='weight_mc_event')
    loop += ssdilep.algs.EvWeights.Pileup(cutflow='presel',key='weight_pileup')
   
    ## initialize and/or decorate objects
    ## ---------------------------------------
    loop += ssdilep.algs.vars.JetsBuilder()

    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneTau') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneMuon') 
    
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='LeadTauIsVeryLoose')
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTausMedium')
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTausEleBDTLoose')
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTauPt20') 

    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='EleVeto') 
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='JetCleaning') 
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneTightJet') 
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneJet') 


    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuPt30') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuMedium') 
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuZ0SinTheta05') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuEta247') 
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuD0Sig3') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuFCTightTrackOnly') 

    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='SingleMuTriggerMatch') 
    
    loop += ssdilep.algs.vars.MuTauVars()   

    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
   
    loop += ssdilep.algs.EvWeights.MuTrigSF(
            trig_list    = ["HLT_mu26_ivarmedium","HLT_mu50"],
            merge_menus  = True,
            mu_reco      = "Medium",
            key          = "MuTrigSFMedium",
            scale        = None,
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
            mu_iso        = "FCTightTrackOnly_FixedRad",
            mu_reco       = "Medium",
            key           = "MuSFFCTightTrackOnlyMedium",
            scale         = None,
            )
    loop += ssdilep.algs.ObjWeights.TauAllSF(
            tau_index    = 0,
            tau_eolr     = "Loose",
            tau_id       = "Medium",
            key          = "Tau0AllSF",
            scale        = None,
            )


    ## configure histograms
    ## ---------------------------------------
    hist_list = []
    hist_list += ssdilep.hists.MuTauVR_hists.hist_list
    
    
    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------
    
    # baseline region
    # -----------------


    for name,cut in {"nofil":"PASS","fil":"TrueLeptonFilter","antifil":"FakeLeptonFilter"}.iteritems():

      """ 
      loop += ssdilep.algs.algs.PlotAlg(
              region       = 'BASELINE'+name,
              plot_all     = False,
              do_var_check = True,
              hist_list    = hist_list,
              cut_flow     = [
                ['PASS', None],
                [cut, None],
                ],
              )
      ## OS Z
      ## ---------------------------------------
      loop += ssdilep.algs.algs.PlotAlg(
              region       = 'OSZ'+name,
              plot_all     = False,
              do_var_check = True,
              hist_list    = hist_list,
              cut_flow     = [
                ['OneOSPair', ['MuSFFCTightTrackOnlyMedium','MuTrigSFMedium','Tau0AllSF']],
                ['MuTauSumCosDphi05',None],
                ['mTMu50',None],
                ['MuTauZwin',None],
                [cut, None],
                ],
              )
      ## SS Z
      ## ---------------------------------------
      loop += ssdilep.algs.algs.PlotAlg(
              region       = 'SSZ'+name,
              plot_all     = False,
              do_var_check = True,
              hist_list    = hist_list,
              cut_flow     = [
                ['OneSSPair', ['MuSFFCTightTrackOnlyMedium','MuTrigSFMedium','Tau0AllSF']],
                ['MuTauSumCosDphi05',None],
                ['mTMu50',None],
                ['MuTauZwin',None],
                [cut, None],
                ],
              )
    
    
      ## full OS Z
      ## ---------------------------------------
      loop += ssdilep.algs.algs.PlotAlg(
              region       = 'FullOSZ'+name,
              plot_all     = False,
              do_var_check = True,
              hist_list    = hist_list,
              cut_flow     = [
                ['OneOSPair', ['MuSFFCTightTrackOnlyMedium','MuTrigSFMedium','Tau0AllSF']],
                ['MuTauSumCosDphi05',None],
                ['mTMu50',None],
                [cut, None],
                ],
              )
      ## full SS Z
      ## ---------------------------------------
      loop += ssdilep.algs.algs.PlotAlg(
              region       = 'FullSSZ'+name,
              plot_all     = False,
              do_var_check = True,
              hist_list    = hist_list,
              cut_flow     = [
                ['OneSSPair', ['MuSFFCTightTrackOnlyMedium','MuTrigSFMedium','Tau0AllSF']],
                ['MuTauSumCosDphi05',None],
                ['mTMu50',None],
                [cut, None],
                ],
              )
      """ 
    
      ## OS TTBAR
      ## ---------------------------------------
      loop += ssdilep.algs.algs.PlotAlg(
              region       = 'OSTTBAR_'+name,
              plot_all     = False,
              do_var_check = True,
              hist_list    = hist_list,
              cut_flow     = [
                ['OneOSPair', ['MuSFFCTightTrackOnlyMedium','MuTrigSFMedium','Tau0AllSF']],
                ['AtLeastTwoBjets',None],
                ['AllTauPt50',None],
                ['AllMuPt50',None],
                [cut, None],
                ],
              )
      ## SS TTBAR
      ## ---------------------------------------
      loop += ssdilep.algs.algs.PlotAlg(
              region       = 'SSTTBAR_'+name,
              plot_all     = False,
              do_var_check = True,
              hist_list    = hist_list,
              cut_flow     = [
                ['OneSSPair', ['MuSFFCTightTrackOnlyMedium','MuTrigSFMedium','Tau0AllSF']],
                ['AtLeastTwoBjets',None],
                ['AllTauPt50',None],
                ['AllMuPt50',None],
                [cut, None],
                ],
              )
   


      ## full OS TTBAR
      ## ---------------------------------------
      loop += ssdilep.algs.algs.PlotAlg(
              region       = 'FullOSTTBAR_'+name,
              plot_all     = False,
              do_var_check = True,
              hist_list    = hist_list,
              cut_flow     = [
                ['OneOSPair', ['MuSFFCTightTrackOnlyMedium','MuTrigSFMedium','Tau0AllSF']],
                ['AtLeastOneBjet',None],
                [cut, None],
                ],
              )
      ## full SS TTBAR
      ## ---------------------------------------
      loop += ssdilep.algs.algs.PlotAlg(
              region       = 'FullSSTTBAR_'+name,
              plot_all     = False,
              do_var_check = True,
              hist_list    = hist_list,
              cut_flow     = [
                ['OneSSPair', ['MuSFFCTightTrackOnlyMedium','MuTrigSFMedium','Tau0AllSF']],
                ['AtLeastOneBjet',None],
                [cut, None],
                ],
              )



      ## hi-pt full OS TTBAR
      ## ---------------------------------------
      loop += ssdilep.algs.algs.PlotAlg(
              region       = 'HiPtFullOSTTBAR_'+name,
              plot_all     = False,
              do_var_check = True,
              hist_list    = hist_list,
              cut_flow     = [
                ['OneOSPair', ['MuSFFCTightTrackOnlyMedium','MuTrigSFMedium','Tau0AllSF']],
                ['AtLeastOneBjet',None],
                ['AllTauPt50',None],
                ['AllMuPt50',None],
                [cut, None],
                ],
              )
      ## hi-pt full SS TTBAR
      ## ---------------------------------------
      loop += ssdilep.algs.algs.PlotAlg(
              region       = 'HiPtFullSSTTBAR_'+name,
              plot_all     = False,
              do_var_check = True,
              hist_list    = hist_list,
              cut_flow     = [
                ['OneSSPair', ['MuSFFCTightTrackOnlyMedium','MuTrigSFMedium','Tau0AllSF']],
                ['AtLeastOneBjet',None],
                ['AllTauPt50',None],
                ['AllMuPt50',None],
                [cut, None],
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



