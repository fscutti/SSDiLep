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

from ssdilep.samples.SamplesID import SampleID
from ssdilep.samples.xsections import xsdict

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
                                  sampleDB={"ID":SampleID, "xs":xsdict},
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
                             #######'HLT_tau35_medium1_tracktwo_tau25_medium1_tracktwo', # KILLED
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
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneSSPair') 
    
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AtLeastOneTau') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTaus1OR3Prong') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTausEleBDTLoose') 
    
    # not strictly necessary
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTausBDT0005') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTausVeryLoose') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTauPt20') 

    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='BVeto') 
    
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuPt40') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuMedium') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuEta247') 

    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllElPt40') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllElEta247') 

    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='ZVeto') 
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='PairPt150') 
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='PairDR35') 
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='mTtot300') 

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
              os.path.join(main_path,'ssdilep/data/merged_Jun2_ff_taulead_pt_data_1PMedium_All_1PMedium.root'),
              os.path.join(main_path,'ssdilep/data/merged_Jun2_ff_taulead_pt_data_3PMedium_All_3PMedium.root')],
            key                      = 'FF',
            scale                    = None,
            )
    
    
    
    ## configure histograms
    ## ---------------------------------------
    hist_list = []
    hist_list += ssdilep.hists.EVENT_hists.hist_list
    hist_list += ssdilep.hists.TAUS_hists.hist_list
    hist_list += ssdilep.hists.MET_hists.hist_list
    
    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------

    # two lepton regions
    # ------------------


    for vrCut in ["ANTIZVeto","ANTIPairPt150","ANTIPairDR35","ANTImTtot300"]:

        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1SF2L_inv%s_ValRegionFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  #['SingleTauTriggerMatch-OR-DiTauTriggerMatch', None],
                  ['SingleTauTriggerMatch', None],
                  ['TwoLeptons', None],
                  ['AtLeastOneSSPairIsSF', None],
                  ['AllPassLeptons', None],
                  ['%s'%vrCut, None],
                  ],
                )
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1SF2L_inv%s_SideBandFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  #['SingleTauTriggerMatch-OR-DiTauTriggerMatch', None],
                  ['SingleTauTriggerMatch', None],
                  ['TwoLeptons', None],
                  ['AtLeastOneSSPairIsSF', None],
                  ['AtLeastOneFailLepton', None],
                  ['%s'%vrCut, ['FF']],
                  ],
                )
       
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1DF2L_inv%s_ValRegionFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['TwoLeptons', None],
                  ['AtLeastOneSSPairIsDF', None],
                  ['AllPassLeptons', None],
                  ['%s'%vrCut, None],
                  ],
                )
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1DF2L_inv%s_SideBandFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['TwoLeptons', None],
                  ['AtLeastOneSSPairIsDF', None],
                  ['AtLeastOneFailLepton', None],
                  ['%s'%vrCut, ['FF']],
                  ],
                )
       
       
        # three lepton regions
        # --------------------
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1SF3L_inv%s_ValRegionFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  #['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['ThreeLeptons', None],
                  ['AtLeastOneSSPairIsSF', None],
                  ['AllPassLeptons', None],
                  ['%s'%vrCut, None],
                  ],
                )
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1SF3L_inv%s_SideBandFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  #['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['ThreeLeptons', None],
                  ['AtLeastOneSSPairIsSF', None],
                  ['AtLeastOneFailLepton', None],
                  ['%s'%vrCut, ['FF']],
                  ],
                )
       
       
       
       
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1DF3L_inv%s_ValRegionFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  #['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['ThreeLeptons', None],
                  ['AtLeastOneSSPairIsDF', None],
                  ['AllPassLeptons', None],
                  ['%s'%vrCut, None],
                  ],
                )
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1DF3L_inv%s_SideBandFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  #['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['ThreeLeptons', None],
                  ['AtLeastOneSSPairIsDF', None],
                  ['AtLeastOneFailLepton', None],
                  ['%s'%vrCut, ['FF']],
                  ],
                )
       
       
       
       
        """ 
        # non filtered MC
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1SF2L_inv%s_ValRegionNonFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  ['SingleTauTriggerMatch-OR-DiTauTriggerMatch', None],
                  ['TwoLeptons', None],
                  ['AtLeastOneSSPairIsSF', None],
                  ['AllPassLeptonsNoFilter', None],
                  ['%s'%vrCut, None],
                  ],
                )
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1SF2L_inv%s_SideBandNonFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  ['SingleTauTriggerMatch-OR-DiTauTriggerMatch', None],
                  ['TwoLeptons', None],
                  ['AtLeastOneSSPairIsSF', None],
                  ['AtLeastOneFailLeptonNoFilter', None],
                  ['%s'%vrCut, None],
                  ],
                )
       
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1DF2L_inv%s_ValRegionNonFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['TwoLeptons', None],
                  ['AtLeastOneSSPairIsDF', None],
                  ['AllPassLeptonsNoFilter', None],
                  ['%s'%vrCut, None],
                  ],
                )
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1DF2L_inv%s_SideBandNonFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['TwoLeptons', None],
                  ['AtLeastOneSSPairIsDF', None],
                  ['AtLeastOneFailLeptonNoFilter', None],
                  ['%s'%vrCut, None],
                  ],
                )
       
       
        # three lepton regions
        # --------------------
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1SF3L_inv%s_ValRegionNonFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['ThreeLeptons', None],
                  ['AtLeastOneSSPairIsSF', None],
                  ['AllPassLeptonsNoFilter', None],
                  ['%s'%vrCut, None],
                  ],
                )
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1SF3L_inv%s_SideBandNonFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['ThreeLeptons', None],
                  ['AtLeastOneSSPairIsSF', None],
                  ['AtLeastOneFailLeptonNoFilter', None],
                  ['%s'%vrCut, None],
                  ],
                )
       
       
       
       
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1DF3L_inv%s_ValRegionNonFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['ThreeLeptons', None],
                  ['AtLeastOneSSPairIsDF', None],
                  ['AllPassLeptonsNoFilter', None],
                  ['%s'%vrCut, None],
                  ],
                )
        loop += ssdilep.algs.algs.PlotAlg(
                region       = '1DF3L_inv%s_SideBandNonFiltered'%vrCut,
                plot_all     = False,
                do_var_check = True,
                hist_list    = hist_list + ssdilep.hists.ONEPAIR_hists.hist_list,
                cut_flow     = [
                  ['SingleTauTriggerMatch-OR-SingleElTriggerMatch-OR-SingleMuTriggerMatch-OR-DiTauTriggerMatch-OR-MuTauTriggerMatch-OR-ElTauTriggerMatch', None],
                  ['ThreeLeptons', None],
                  ['AtLeastOneSSPairIsDF', None],
                  ['AtLeastOneFailLeptonNoFilter', None],
                  ['%s'%vrCut, None],
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


