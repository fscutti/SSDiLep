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
        required_triggers = [
                             'HLT_j15',
                             'HLT_j25',
                             'HLT_j35',
                             ###'HLT_j55',  # 2015-2016 only
                             'HLT_j60',
                             'HLT_j85',
                             'HLT_j110',
                             #'HLT_j150', # 2015-2016 only
                             'HLT_j175',
                             'HLT_j260', # 2017- only
                             ###'HLT_j360', # 2017- only
                             'HLT_j380', # 2015-2016 only
                             'HLT_j400',
                             'HLT_j420',
                             ],
                             get_prescales_lumi = True,
                             key                = 'jets',
                             )

    ## build and pt-sort objects
    ## ---------------------------------------
    loop += pyframe.algs.ListBuilder(
        prefixes = ['tau_','jet_','trigJet_a4tcemsubjesFS_','trigJet_a4tcemsubjesISFS_'],
        attr_prefixes = ['tau_tracks_'],
        keys = ['taus','jets','trigJetsFS','trigJetsISFS'],
        )
    loop += pyframe.algs.AttachTLVs(
        keys = ['taus','jets','trigJetsFS','trigJetsISFS'],
        attr_keys = ['tau_tracks'],
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
    loop += ssdilep.algs.EvWeights.MCEventWeight(cutflow='presel',key='weight_mc_event')
    loop += ssdilep.algs.EvWeights.Pileup(cutflow='presel',key='weight_pileup')
    loop += ssdilep.algs.EvWeights.TrigPresc(cutflow='presel',particles="jets",key="weight_data_unpresc")
   
    ## initialize and/or decorate objects
    ## ---------------------------------------
    loop += ssdilep.algs.vars.JetsBuilder(build_trigger_jets=True)   

    loop += ssdilep.algs.vars.DiJetVars(key_leptons='taus',
                                        key_jets='jets_tight',
    ) 
    
    ## cuts
    ## +++++++++++++++++++++++++++++++++++++++
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='OneTau') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='LeadTauIsVeryLoose') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='EleVeto') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='MuVeto') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='SingleJetTrigger') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AllTauPt20') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='JetCleaning') 
    loop += ssdilep.algs.algs.CutAlg(cutflow='presel',cut='AtLeastOneJet') 

    
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
    
    ## NOFILTER
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NOFILTER_F1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NOFILTER_1PF1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['One1PTau', None],
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_NOFILTER_3PF1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['One3PTau', None],
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ],
            )
    
    ## TRUETAUHAD
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_TRUETAUHAD_F1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ['TrueTauHadFilter', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_TRUETAUHAD_1PF1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['One1PTau', None],
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ['TrueTauHadFilter', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_TRUETAUHAD_3PF1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['One3PTau', None],
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ['TrueTauHadFilter', None],
              ],
            )
    
    """
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_TRUETAUHAD_F2',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetPtRatioHigh1', None],
              ['TauJetDphi27', None],
              ['TrueTauHadFilter', None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_TRUETAUHAD_F3',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetPtRatioLow1', None],
              ['TauJetDphi27', None],
              ['TrueTauHadFilter', None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_TRUETAUHAD_F4',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['TwoJets', ['JVTSF']],
              ['TrueTauHadFilter', None],
              ],
            )

    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_TRUETAUHAD_F5',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', ['JVTSF']],
              ['TrueTauHadFilter', None],
              ],
            )
    """
    
    ## GLUONS
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_GLUONS_F1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ['GluonFilter', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_GLUONS_1PF1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['One1PTau', None],
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ['GluonFilter', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_GLUONS_3PF1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['One3PTau', None],
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ['GluonFilter', None],
              ],
            )
    
    """
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_GLUONS_F2',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetPtRatioHigh1', None],
              ['TauJetDphi27', None],
              ['GluonFilter', None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_GLUONS_F3',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetPtRatioLow1', None],
              ['TauJetDphi27', None],
              ['GluonFilter', None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_GLUONS_F4',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['TwoJets', ['JVTSF']],
              ['GluonFilter', None],
              ],
            )

    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_GLUONS_F5',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', ['JVTSF']],
              ['GluonFilter', None],
              ],
            )
    """ 
    ## QUARKS
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_QUARKS_F1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ['QuarkFilter', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_QUARKS_1PF1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['One1PTau', None],
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ['QuarkFilter', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_QUARKS_3PF1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['One3PTau', None],
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ['QuarkFilter', None],
              ],
            )
    
    """
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_QUARKS_F2',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetPtRatioHigh1', None],
              ['TauJetDphi27', None],
              ['QuarkFilter', None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_QUARKS_F3',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetPtRatioLow1', None],
              ['TauJetDphi27', None],
              ['QuarkFilter', None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_QUARKS_F4',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['TwoJets', ['JVTSF']],
              ['QuarkFilter', None],
              ],
            )

    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_QUARKS_F5',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', ['JVTSF']],
              ['QuarkFilter', None],
              ],
            )
    """

    ## UNKNOWN
    ## ---------------------------------------
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_UNKNOWN_F1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ['UnknownFilter', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_UNKNOWN_1PF1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['One1PTau', None],
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ['UnknownFilter', None],
              ],
            )
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_UNKNOWN_3PF1',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['One3PTau', None],
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetDphi27', None],
              ['UnknownFilter', None],
              ],
            )
    
    """
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_UNKNOWN_F2',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetPtRatioHigh1', None],
              ['TauJetDphi27', None],
              ['UnknownFilter', None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_UNKNOWN_F3',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['OneJet', ['JVTSF']],
              ['TauJetPtRatioLow1', None],
              ['TauJetDphi27', None],
              ['UnknownFilter', None],
              ],
            )
    
    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_UNKNOWN_F4',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', None],
              ['TwoJets', ['JVTSF']],
              ['UnknownFilter', None],
              ],
            )

    loop += ssdilep.algs.algs.PlotAlg(
            region       = 'FAKES_UNKNOWN_F5',
            plot_all     = False,
            do_var_check = True,
            hist_list    = hist_list,
            cut_flow     = [
              ['LeadJetPt20', ['JVTSF']],
              ['UnknownFilter', None],
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



