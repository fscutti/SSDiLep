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
        required_triggers = ["HLT_mu26_ivarmedium", "HLT_mu50"],          
        key               = 'muons',
        )
    
    ## build and pt-sort objects
    ## ---------------------------------------
    loop += pyframe.algs.ListBuilder(
        prefixes = ['muon_','el_','jet_'],
        keys = ['muons','electrons','jets'],
        )
    loop += pyframe.algs.AttachTLVs(
        keys = ['muons','jets','electrons'],
        )
    # just a decoration of particles ...
    loop += ssdilep.algs.vars.ParticlesBuilder(
        key='muons',
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
   
    ## initialize and/or decorate objects
    ## ---------------------------------------
    loop += ssdilep.algs.vars.DiMuVars(key_muons='muons')   
    loop += ssdilep.algs.vars.DiJetVars(key_leptons='muons',key_jets='jets',build_tight_jets=True)   
    
    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='TwoMuons') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuMedium') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuZ0SinTheta05') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllMuEta247') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='JetCleaning') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AtLeastTwoTightJets') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='SingleMuTrigger') 
    

    
    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
    
    # WARNING: weight should be modified
    #loop += ssdilep.algs.EvWeights.MuTrigSF(
    #        trig_list     = ["HLT_mu26_ivarmedium_OR_HLT_mu50"],
    #        mu_reco       = "Medium",
    #        key           = "MuTrigSFRecoMedium",
    #        scale         = None,
    #        )
    
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
            key           = "Mu0RecoSF",
            scale         = None,
            )
    loop += ssdilep.algs.ObjWeights.MuAllSF(
            mu_index      = 0,
            mu_iso        = "FixedCutTightTrackOnly",
            mu_reco       = "Medium",
            key           = "Mu0AllSF",
            scale         = None,
            )
    loop += ssdilep.algs.ObjWeights.MuAllSF(
            mu_index      = 1,
            mu_iso        = "NotFixedCutTightTrackOnly",
            mu_reco       = "Medium",
            key           = "Mu1RecoSF",
            scale         = None,
            )
    loop += ssdilep.algs.ObjWeights.MuAllSF(
            mu_index      = 1,
            mu_iso        = "FixedCutTightTrackOnly",
            mu_reco       = "Medium",
            key           = "Mu1AllSF",
            scale         = None,
            )
    """ 
    # fake-factors
    loop += ssdilep.algs.ObjWeights.MuFakeFactorGraph(
            config_file=os.path.join(main_path,'ssdilep/data/sys_ff_mulead_pt_data_v9.root'),
            mu_index=0,
            key='Mu0FF',
            scale=sys_ff,
            )
    loop += ssdilep.algs.ObjWeights.MuFakeFactorGraph(
            config_file=os.path.join(main_path,'ssdilep/data/sys_ff_mulead_pt_data_v9.root'),
            mu_index=1,
            key='Mu1FF',
            scale=sys_ff,
            )
    """
    ## configure histograms
    ## ---------------------------------------
    hist_list = []
    hist_list += ssdilep.hists.Main_hists.hist_list
    #hist_list += ssdilep.hists.H2D_hists.hist_list
    
    
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
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom60to130',None],
              #['MuNoFilterTT',['Mu0AllSF','Mu1AllSF']],
              ['MuTT',['Mu0AllSF','Mu1AllSF']],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSZ_LT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom60to130',None],
              #['MuNoFilterLT',['Mu0RecoSF','Mu1AllSF',]],
              ['MuLT',['Mu0RecoSF','Mu1AllSF',]],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSZ_TL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom60to130',None],
              #['MuNoFilterTL',['Mu0AllSF','Mu1RecoSF',]],
              ['MuTL',['Mu0AllSF','Mu1RecoSF',]],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSZ_LL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom60to130',None],
              #['MuNoFilterLL',['Mu0RecoSF','Mu1RecoSF',]],
              ['MuLL',['Mu0RecoSF','Mu1RecoSF',]],
              ],
            )

    ## OS W+jet VR
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSW_TT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom35to60orFrom100to125',None],
              ['mVisMMfrom130toINF',None],
              #['MuNoFilterTT',['Mu0AllSF','Mu1AllSF']],
              ['MuTT',['Mu0AllSF','Mu1AllSF']],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSW_LT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom35to60orFrom100to125',None],
              ['mVisMMfrom130toINF',None],
              #['MuNoFilterLT',['Mu0RecoSF','Mu1AllSF']],
              ['MuLT',['Mu0RecoSF','Mu1AllSF']],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSW_TL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom35to60orFrom100to125',None],
              ['mVisMMfrom130toINF',None],
              #['MuNoFilterTL',['Mu0AllSF','Mu1RecoSF']],
              ['MuTL',['Mu0AllSF','Mu1RecoSF']],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSW_LL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom35to60orFrom100to125',None],
              ['mVisMMfrom130toINF',None],
              #['MuNoFilterLL',['Mu0RecoSF','Mu1RecoSF']],
              ['MuLL',['Mu0RecoSF','Mu1RecoSF']],
              ],
            )

    ## OS Top CR
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSTop_TT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig5',None],
              ['AtLeastTwoBjets',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom130toINF',None],
              #['MuNoFilterTT',['Mu0AllSF','Mu1AllSF']],
              ['MuTT',['Mu0AllSF','Mu1AllSF']],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSTop_LT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig5',None],
              ['AtLeastTwoBjets',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom130toINF',None],
              #['MuNoFilterLT',['Mu0RecoSF','Mu1AllSF',]],
              ['MuLT',['Mu0RecoSF','Mu1AllSF',]],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSTop_TL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig5',None],
              ['AtLeastTwoBjets',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom130toINF',None],
              #['MuNoFilterTL',['Mu0AllSF','Mu1RecoSF',]],
              ['MuTL',['Mu0AllSF','Mu1RecoSF',]],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSTop_LL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig5',None],
              ['AtLeastTwoBjets',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom130toINF',None],
              #['MuNoFilterLL',['Mu0RecoSF','Mu1RecoSF',]],
              ['MuLL',['Mu0RecoSF','Mu1RecoSF',]],
              ],
            )

    ## OS Sig
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSSig_TT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig10',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom130toINF',None],
              #['MuNoFilterTT',['Mu0AllSF','Mu1AllSF']],
              ['MuTT',['Mu0AllSF','Mu1AllSF']],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSSig_LT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig10',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom130toINF',None],
              #['MuNoFilterLT',['Mu0RecoSF','Mu1AllSF',]],
              ['MuLT',['Mu0RecoSF','Mu1AllSF',]],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSSig_TL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig10',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom130toINF',None],
              #['MuNoFilterTL',['Mu0AllSF','Mu1RecoSF',]],
              ['MuTL',['Mu0AllSF','Mu1RecoSF',]],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'OSSig_LL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoOSMuons',None],
              ['LeadMuPt80',None],
              ['LeadJetPt50',None],
              ['METSig10',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom130toINF',None],
              #['MuNoFilterLL',['Mu0RecoSF','Mu1RecoSF',]],
              ['MuLL',['Mu0RecoSF','Mu1RecoSF',]],
              ],
            )


    ## SS Z+jet CR
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'SSZ_TT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoSSMuons',None],
              ['LeadMuPt60',None],
              ['LeadJetPt40',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom60to100',None],
              #['MuNoFilterTT',['Mu0AllSF','Mu1AllSF']],
              ['MuTT',['Mu0AllSF','Mu1AllSF']],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'SSZ_LT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoSSMuons',None],
              ['LeadMuPt60',None],
              ['LeadJetPt40',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom60to100',None],
              #['MuNoFilterLT',['Mu0RecoSF','Mu1AllSF',]],
              ['MuLT',['Mu0RecoSF','Mu1AllSF',]],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'SSZ_TL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoSSMuons',None],
              ['LeadMuPt60',None],
              ['LeadJetPt40',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom60to100',None],
              #['MuNoFilterTL',['Mu0AllSF','Mu1RecoSF',]],
              ['MuTL',['Mu0AllSF','Mu1RecoSF',]],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'SSZ_LL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoSSMuons',None],
              ['LeadMuPt60',None],
              ['LeadJetPt40',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom60to100',None],
              #['MuNoFilterLL',['Mu0RecoSF','Mu1RecoSF',]],
              ['MuLL',['Mu0RecoSF','Mu1RecoSF',]],
              ],
            )

    ## SS W+jet VR
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'SSW_TT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoSSMuons',None],
              ['LeadMuPt60',None],
              ['LeadJetPt40',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom35to60orFrom100to125',None],
              ['mVisMMfrom100toINF',None],
              #['MuNoFilterTT',['Mu0AllSF','Mu1AllSF']],
              ['MuTT',['Mu0AllSF','Mu1AllSF']],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'SSW_LT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoSSMuons',None],
              ['LeadMuPt60',None],
              ['LeadJetPt40',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom35to60orFrom100to125',None],
              ['mVisMMfrom100toINF',None],
              #['MuNoFilterLT',['Mu0RecoSF','Mu1AllSF']],
              ['MuLT',['Mu0RecoSF','Mu1AllSF']],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'SSW_TL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoSSMuons',None],
              ['LeadMuPt60',None],
              ['LeadJetPt40',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom35to60orFrom100to125',None],
              ['mVisMMfrom100toINF',None],
              #['MuNoFilterTL',['Mu0AllSF','Mu1RecoSF']],
              ['MuTL',['Mu0AllSF','Mu1RecoSF']],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'SSW_LL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoSSMuons',None],
              ['LeadMuPt60',None],
              ['LeadJetPt40',None],
              ['METSig5',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom35to60orFrom100to125',None],
              ['mVisMMfrom100toINF',None],
              #['MuNoFilterLL',['Mu0RecoSF','Mu1RecoSF']],
              ['MuLL',['Mu0RecoSF','Mu1RecoSF']],
              ],
            )

    ## SS Sig
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'SSSig_TT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoSSMuons',None],
              ['LeadMuPt60',None],
              ['LeadJetPt40',None],
              ['METSig75',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom100toINF',None],
              #['MuNoFilterTT',['Mu0AllSF','Mu1AllSF']],
              ['MuTT',['Mu0AllSF','Mu1AllSF']],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'SSSig_LT',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoSSMuons',None],
              ['LeadMuPt60',None],
              ['LeadJetPt40',None],
              ['METSig75',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom100toINF',None],
              #['MuNoFilterLT',['Mu0RecoSF','Mu1AllSF',]],
              ['MuLT',['Mu0RecoSF','Mu1AllSF',]],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'SSSig_TL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoSSMuons',None],
              ['LeadMuPt60',None],
              ['LeadJetPt40',None],
              ['METSig75',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom100toINF',None],
              #['MuNoFilterTL',['Mu0AllSF','Mu1RecoSF',]],
              ['MuTL',['Mu0AllSF','Mu1RecoSF',]],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'SSSig_LL',
            plot_all     = False,
            do_var_check = False,
            hist_list    = hist_list,
            cut_flow     = [
              ['TwoSSMuons',None],
              ['LeadMuPt60',None],
              ['LeadJetPt40',None],
              ['METSig75',None],
              ['BVeto',['GlobBJetSF','JVTSF']],
              ['mVisJJfrom60to100',None],
              ['mVisMMfrom100toINF',None],
              #['MuNoFilterLL',['Mu0RecoSF','Mu1RecoSF',]],
              ['MuLL',['Mu0RecoSF','Mu1RecoSF',]],
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



