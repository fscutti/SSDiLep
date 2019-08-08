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


    #loop += pyframe.algs.MetaDataHistGetAlg()
    
    
    ## configure the list of triggers 
    ## with eventual prescales and puts a
    ## trig list to the store for later cutflow
    ## ---------------------------------------
    loop += ssdilep.algs.vars.BuildTrigConfig(
        required_triggers = [
                             'HLT_j15',
                             'HLT_j25',
                             'HLT_j35',
                             'HLT_j45',
                             'HLT_j55',  # 2015-2016 only, rem
                             'HLT_j60',
                             'HLT_j85',
                             'HLT_j110',
                             'HLT_j150', # 2015-2016 only Frank removed
                             'HLT_j175',
                             'HLT_j260', # 2017- only
                             'HLT_j360', # 2017- only, rem
                             'HLT_j380', # 2015-2016 only
                             'HLT_j400',
                             'HLT_j420',
                             #'HLT_tau160_medium1_tracktwo',
                             #'HLT_tau35_medium1_tracktwo_tau25_medium1_tracktwo',
                             ],
                             get_prescales_lumi = True,
                             key                = ['jets','taus'],
                             )

    ## build and pt-sort objects
    ## ---------------------------------------
    loop += pyframe.algs.ListBuilder(
        prefixes = ['tau_','jet_','trigJet_a4tcemsubjesFS_','trigJet_a4tcemsubjesISFS_'],
        #attr_prefixes = ['tau_tracks_'],
        keys = ['taus','jets','trigJetsFS','trigJetsISFS'],
        )
    loop += pyframe.algs.AttachTLVs(
        keys = ['taus','jets','trigJetsFS','trigJetsISFS'],
        #attr_keys = ['tau_tracks'],
        )
    # just a decoration of particles ...
    loop += ssdilep.algs.vars.ParticlesBuilder(key='taus')

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
    loop += ssdilep.algs.EvWeights.MCEventWeight(cutflow='presel',metadata=metadata_dict,key='weight_mc_event')
    loop += ssdilep.algs.EvWeights.Pileup(cutflow='presel',key='weight_pileup')
    loop += ssdilep.algs.EvWeights.TrigPresc(cutflow='presel',particles="jets",key="weight_data_unpresc")
   
    ## initialize and/or decorate objects
    ## ---------------------------------------
    loop += ssdilep.algs.vars.JetsBuilder(build_trigger_jets=True)   
    
    loop += ssdilep.algs.vars.DiJetVars(key_leptons='taus',
                                        key_jets='jets',
    ) 

    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneTau') 
    
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='LeadTauIsVeryLoose') # do we need to test this?
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='LeadTauIsLoose') # do we need to test this?
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='LeadTauBDT0005') 
    
    
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='EleVeto') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='MuVeto') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='SingleJetTriggerMatch') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTauPt20') 
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='JetCleaning') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AtLeastOneJet') 
    
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='TauOriginFilter') 
    
    #loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='TrueTauHadFilter') 
    #if 'qfakes' in config['samplename']:    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='QuarkFilter') 
    #elif 'gfakes' in config['samplename']:  loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='GluonFilter') 
    #elif 'ufakes' in config['samplename']:  loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='UnknownFilter') 

    
    ## weights configuration
    ## ---------------------------------------
    ## event
    ## +++++++++++++++++++++++++++++++++++++++
    
    # jet weights 
    #loop += ssdilep.algs.EvWeights.GlobalBjet(
    #        key       = "GlobBJetSF",
    #        )
    loop += ssdilep.algs.EvWeights.GlobalJVT(
            key       = "JVTSF",
            )

    ## objects
    ## +++++++++++++++++++++++++++++++++++++++
    """
    """ 
    ## configure histograms
    ## ---------------------------------------
    hist_list = []
    hist_list += ssdilep.hists.OneTauFF_hists.hist_list
    hist_list += ssdilep.hists.TauTracks_hists.hist_list

    if config['sampletype'] == "mc":
      hist_list += ssdilep.hists.TRUTH_TAUS_hists.hist_list


    ##-------------------------------------------------------------------------
    ## make plots
    ##-------------------------------------------------------------------------
    
    #for tauPtBin in ["All","2030","3040","4060","6090","90150","150inf"]:
    for tauPtBin in ["All"]:
       for tauProngs in ["1P","3P"]:
         
         """     
         ## F0
         ## ---------------------------------------
         loop += ssdilep.algs.algs.PlotAlg(
                 region       = 'FAKES_NOSEL_%sPass_%s_F0'%(tauProngs,tauPtBin),
                 plot_all     = False,
                 do_var_check = True,
                 hist_list    = hist_list,
                 cut_flow     = [
                   #['SingleJetTriggerMatch', None],
                   ['One%sTau'%tauProngs, None],
                   ['OneJet', ['JVTSF']],
                   ['LeadJetPt20', None],
                   ['TauJetDphi27', None],
                   ['LeadTauPtBin%s'%tauPtBin, None],
                   ],
                 )
         """     

         for tauType in ["Medium"]:
             
             filter_list = ["TrueTauHadFilter","QuarkFilter","BFilter","GluonFilter","UnknownFilter"]

             if config['sampletype'] == "mc":     filters = filter_list
             elif config['sampletype'] == "data": filters = ["PASS"]

             for filterType in filters:
             
                ## F1
                ## ---------------------------------------
                loop += ssdilep.algs.algs.PlotAlg(
                        region       = 'FAKES_NUM_%s%s_%s_%s_F1'%(tauProngs,tauType,filterType,tauPtBin),
                        plot_all     = False,
                        do_var_check = True,
                        hist_list    = hist_list,
                        cut_flow     = [
                          ['%s'%filterType, None],
                          ['One%sTau'%tauProngs, None],
                          ['OneJet', ['JVTSF']],
                          ['LeadJetPt20', None],
                          ['TauJetDphi27', None],
                          ['LeadTauIs%s'%tauType, None],
                          ['LeadTauPtBin%s'%tauPtBin, None],
                          ],
                        )
                loop += ssdilep.algs.algs.PlotAlg(
                        region       = 'FAKES_DEN_%s%s_%s_%s_F1'%(tauProngs,tauType,filterType,tauPtBin),
                        plot_all     = False,
                        do_var_check = True,
                        hist_list    = hist_list,
                        cut_flow     = [
                          ['%s'%filterType, None],
                          ['One%sTau'%tauProngs, None],
                          ['OneJet', ['JVTSF']],
                          ['LeadJetPt20', None],
                          ['TauJetDphi27', None],
                          ['LeadTauIsNot%s'%tauType, None],
                          ['LeadTauPtBin%s'%tauPtBin, None],
                          ],
                        )
                
                
                ## F10
                ## ---------------------------------------
                loop += ssdilep.algs.algs.PlotAlg(
                        region       = 'FAKES_NUM_%s%s_%s_%s_F10'%(tauProngs,tauType,filterType,tauPtBin),
                        plot_all     = False,
                        do_var_check = True,
                        hist_list    = hist_list,
                        cut_flow     = [
                          ['%s'%filterType, None],
                          ['One%sTau'%tauProngs, None],
                          ['TauIsThirdJet', ['JVTSF']],
                          ['LeadJetPt20', None],
                          ['LeadTauIs%s'%tauType, None],
                          ['LeadTauPtBin%s'%tauPtBin, None],
                          ],
                        )
                loop += ssdilep.algs.algs.PlotAlg(
                        region       = 'FAKES_DEN_%s%s_%s_%s_F10'%(tauProngs,tauType,filterType,tauPtBin),
                        plot_all     = False,
                        do_var_check = True,
                        hist_list    = hist_list,
                        cut_flow     = [
                          ['%s'%filterType, None],
                          ['One%sTau'%tauProngs, None],
                          ['TauIsThirdJet', ['JVTSF']],
                          ['LeadJetPt20', None],
                          ['LeadTauIsNot%s'%tauType, None],
                          ['LeadTauPtBin%s'%tauPtBin, None],
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



