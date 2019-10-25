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
        required_triggers = [
                             # -------------
                             # tau triggers 
                             # -------------
                             #'HLT_tau80_medium1_tracktwo_L1TAU60',
                             #'HLT_tau125_medium1_tracktwo',
                             'HLT_tau160_medium1_tracktwo',
                             #'HLT_tau160_medium1_tracktwo_L1TAU100',
                             #'HLT_tau35_medium1_tracktwo_tau25_medium1_tracktwo_L1TAU20IM_2TAU12IM',
                             #'HLT_tau80_medium1_TAU60_tau50_medium1_L1TAU12',
                             'HLT_tau35_medium1_tracktwo_tau25_medium1_tracktwo',
                             #'HLT_tau80_medium1_tracktwo_L1TAU60_tau60_medium1_tracktwo_L1TAU40',
                             #'HLT_tau35_medium1_tracktwo_tau25_medium1_tracktwo_L1DR-TAU20ITAU12I-J25',
                             # -------------
                             # muon triggers 
                             # -------------
                             'HLT_mu26_ivarmedium',
                             'HLT_mu50',
                             # -----------------
                             # electron triggers 
                             # -----------------
                             'HLT_e26_lhtight_nod0_ivarloose',
                             'HLT_e140_lhloose_nod0',
                             # -----------------
                             # muon+tau triggers
                             # -----------------
                             'HLT_mu14_ivarloose_tau35_medium1_tracktwo',
                             # ---------------------
                             # electron+tau triggers
                             # ---------------------
                             'HLT_e24_lhmedium_nod0_ivarloose_tau35_medium1_tracktwo',
                             ],
                             key                = ['taus','muons','electrons'],
                             )


    ## build and pt-sort objects
    ## ---------------------------------------
    loop += pyframe.algs.ListBuilder(
        prefixes = ['tau_','jet_','el_','muon_'],
        keys = ['taus','jets','electrons','muons'],
        )
    loop += pyframe.algs.AttachTLVs(
        keys = ['taus','jets','electrons','muons'],
        )
    
    # just a decoration of particles ...
    loop += ssdilep.algs.vars.ParticlesBuilder(key='taus')
    loop += ssdilep.algs.vars.ParticlesBuilder(key='muons')
    loop += ssdilep.algs.vars.ParticlesBuilder(key='electrons')
    
    # building pairs with combinations of leptons
    loop += ssdilep.algs.vars.PairsBuilder(key=['taus','muons','electrons'])

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
    loop += ssdilep.algs.vars.PairsVars() 

    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='TwoSSPairs') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='FourLeptons') 
    
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AtLeastOneTau') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTaus1OR3Prong') 
    
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTausEleBDTLoose') 

    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTausLoose') 

    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='BVeto') 
    
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuPt30') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuMedium') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuEta247') 

    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllElPt30') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllElEta247') 

    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='ZVeto') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='mTtot300') 
    
    
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

    ## objects
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.ObjWeights.FakeFactor(
            config_file_light_lepton = os.path.join(main_path,'ssdilep/data/fake_factors.root'),
            config_file_tau_lepton   = [
              os.path.join(main_path,'ssdilep/data/merged_SepTalk_ff_taulead_pt_data_1PMedium_All_1PMedium.root'),
              os.path.join(main_path,'ssdilep/data/merged_SepTalk_ff_taulead_pt_data_3PMedium_All_3PMedium.root')],
            key                      = 'FFDijet',
            scale                    = None,
            )
    
    loop += ssdilep.algs.ObjWeights.FakeFactor(
            config_file_light_lepton = os.path.join(main_path,'ssdilep/data/fake_factors.root'),
            config_file_tau_lepton   = [
              os.path.join(main_path,'ssdilep/data/merged_SepTalk_ff_1DF2L_taulead_pt_1P.root'),
              os.path.join(main_path,'ssdilep/data/merged_SepTalk_ff_1DF2L_taulead_pt_3P.root')],
            key                      = 'FFMultilep2L',
            scale                    = None,
            )
   
    loop += ssdilep.algs.ObjWeights.FakeFactor(
            config_file_light_lepton = os.path.join(main_path,'ssdilep/data/fake_factors.root'),
            config_file_tau_lepton   = [
              os.path.join(main_path,'ssdilep/data/merged_SepTalk_ff_1DF3L_taulead_pt_1P.root'),
              os.path.join(main_path,'ssdilep/data/merged_SepTalk_ff_1DF3L_taulead_pt_3P.root')],
            key                      = 'FFMultilep3L',
            scale                    = None,
            )
    
    ## configure histograms
    ## ---------------------------------------
    hist_list = []
    hist_list += ssdilep.hists.EVENT_hists.hist_list
    hist_list += ssdilep.hists.TAUS_hists.hist_list
    hist_list += ssdilep.hists.MET_hists.hist_list
    hist_list += ssdilep.hists.MULTIPAIRS_hists.hist_list
    
    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------

    # four lepton regions
    # --------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = '2SF4L_SignalRegionFiltered',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list + ssdilep.hists.MULTIPAIRS_hists.hist_list,
            cut_flow     = [
              ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
              ['AtLeastTwoTaus', None],
              ['AllSSPairsAreSF', None],
              ['AllPassLeptons', None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = '2SF4L_SideBandFiltered',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list + ssdilep.hists.MULTIPAIRS_hists.hist_list,
            cut_flow     = [
              ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
              ['AtLeastTwoTaus', None],
              ['AllSSPairsAreSF', None],
              ['AtLeastOneFailLepton', ['FFDijet']],
              ],
            )




    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'al1DF4L_SignalRegionFiltered',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list + ssdilep.hists.MULTIPAIRS_hists.hist_list,
            cut_flow     = [
              ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
              ['AtLeastOneSSPairIsDF', None],
              ['AllPassLeptons', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'al1DF4L_SideBandFiltered',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list + ssdilep.hists.MULTIPAIRS_hists.hist_list,
            cut_flow     = [
              ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
              ['AtLeastOneSSPairIsDF', None],
              ['AtLeastOneFailLepton', ['FFDijet']],
              ],
            )


    """
    # non filtered MC
    loop += ssdilep.algs.algs.PlotAlg(
            region       = '2SF4L_SignalRegionNonFiltered',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list + ssdilep.hists.MULTIPAIRS_hists.hist_list,
            cut_flow     = [
              ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
              ['AtLeastTwoTaus', None],
              ['AllSSPairsAreSF', None],
              ['AllPassLeptonsNoFilter', None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = '2SF4L_SideBandNonFiltered',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list + ssdilep.hists.MULTIPAIRS_hists.hist_list,
            cut_flow     = [
              ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
              ['AtLeastTwoTaus', None],
              ['AllSSPairsAreSF', None],
              ['AtLeastOneFailLeptonNoFilter', None],
              ],
            )




    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'al1DF4L_SignalRegionNonFiltered',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list + ssdilep.hists.MULTIPAIRS_hists.hist_list,
            cut_flow     = [
              ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
              ['AtLeastOneSSPairIsDF', None],
              ['AllPassLeptonsNoFilter', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'al1DF4L_SideBandNonFiltered',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list + ssdilep.hists.MULTIPAIRS_hists.hist_list,
            cut_flow     = [
              ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
              ['AtLeastOneSSPairIsDF', None],
              ['AtLeastOneFailLeptonNoFilter', None],
              ],
            )
    """

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



