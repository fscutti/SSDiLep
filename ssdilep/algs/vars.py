#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random
import os
from itertools import combinations
from copy import copy, deepcopy
from types import MethodType

import pyframe
import ROOT

from units import GeV

import logging
log = logging.getLogger(__name__)

def fatal(message):
    sys.exit("Fatal error in %s: %s" % (__file__, message))

#------------------------------------------------------------------------------
class BuildTrigConfig(pyframe.core.Algorithm):
    """
    Algorithm to configure the trigger chain
    """
    #__________________________________________________________________________
    def __init__(self, 
          cutflow            = None,
          required_triggers  = None,
          get_prescales_lumi = False,
          get_prescales_std  = False,
          key                = None):
        pyframe.core.Algorithm.__init__(self, name="TrigConfig", isfilter=True)
        self.cutflow            = cutflow
        self.required_triggers  = required_triggers
        self.get_prescales_lumi = get_prescales_lumi
        self.get_prescales_std  = get_prescales_std
        self.key                = key
    
    #__________________________________________________________________________
    def initialize(self):
        log.info('initialize trigger config for %s...' % self.key)

    #__________________________________________________________________________
    def execute(self, weight):
        
      #assert len(self.chain.passedTriggers) == len(self.chain.triggerPrescales), "ERROR: # passed triggers != # trigger prescales !!!"
     
      nolim = 1000. 

      # slices for jet triggers
      # -----------------------
      
      jet_trigger_slice = {}
      jet_trigger_slice["mc"] = {}
      jet_trigger_slice["data15"] = {}
      jet_trigger_slice["data16"] = {}
      jet_trigger_slice["data17"] = {}

      jet_trigger_slice["mc"]["HLT_j15"]  = (20.  * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j25"]  = (20.  * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j35"]  = (36.  * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j55"]  = (56.  * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j60"]  = (70.  * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j85"]  = (92.  * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j110"] = (120. * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j150"] = (158. * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j175"] = (184. * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j200"] = (210. * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j260"] = (266. * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j300"] = (300. * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j320"] = (326. * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j360"] = (380. * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j380"] = (414. * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j400"] = (440. * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j420"] = (460. * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j440"] = (480. * GeV , nolim * GeV)
      jet_trigger_slice["mc"]["HLT_j460"] = (500. * GeV , nolim * GeV)


      jet_trigger_slice["data15"]["HLT_j15"]  = (20.  * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j25"]  = (20.  * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j35"]  = (36.  * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j55"]  = (56.  * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j60"]  = (70.  * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j85"]  = (92.  * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j110"] = (120. * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j150"] = (158. * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j175"] = (184. * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j200"] = (210. * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j260"] = (266. * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j300"] = (300. * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j320"] = (326. * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j360"] = (380. * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j380"] = (414. * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j400"] = (440. * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j420"] = (460. * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j440"] = (480. * GeV , nolim * GeV)
      jet_trigger_slice["data15"]["HLT_j460"] = (500. * GeV , nolim * GeV)


      jet_trigger_slice["data16"]["HLT_j15"]  = (20.  * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j25"]  = (20.  * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j35"]  = (36.  * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j55"]  = (56.  * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j60"]  = (68.  * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j85"]  = (92.  * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j110"] = (120. * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j150"] = (158. * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j175"] = (186. * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j200"] = (nolim * GeV, nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j260"] = (270. * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j300"] = (nolim * GeV, nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j320"] = (330. * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j360"] = (366. * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j380"] = (412. * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j400"] = (440. * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j420"] = (470. * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j440"] = (482. * GeV , nolim * GeV)
      jet_trigger_slice["data16"]["HLT_j460"] = (504. * GeV , nolim * GeV)


      jet_trigger_slice["data17"]["HLT_j15"]  = (20.  * GeV , nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j25"]  = (20.  * GeV , nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j35"]  = (34.  * GeV , nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j55"]  = (nolim * GeV, nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j60"]  = (62. * GeV , nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j85"]  = (90. * GeV , nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j110"] = (120. * GeV , nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j150"] = (nolim * GeV, nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j175"] = (186. * GeV , nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j200"] = (nolim * GeV , nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j260"] = (272. * GeV , nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j300"] = (nolim * GeV, nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j320"] = (nolim * GeV, nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j360"] = (366. * GeV , nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j380"] = (378. * GeV , nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j400"] = (406. * GeV , nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j420"] = (448. * GeV , nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j440"] = (478. * GeV , nolim * GeV)
      jet_trigger_slice["data17"]["HLT_j460"] = (488. * GeV , nolim * GeV)


      # slices for muon triggers
      # ------------------------
      # for prescaled studies
      mu_trigger_slice = {}
      mu_trigger_slice["HLT_mu24"]  = (26. * GeV,  nolim * GeV)
      mu_trigger_slice["HLT_mu50"]  = (43. * GeV,  nolim * GeV)


      if self.key == "taus": 
        self.store["ChainsWithTau"] = {} 
        for i,trig in enumerate(self.chain.tau_listTrigChains):
          if trig in self.store["ChainsWithTau"].keys(): continue
          self.store["ChainsWithTau"][trig] = i

      if self.key == "muons": 
        self.store["ChainsWithMuon"] = {} 
        for i,trig in enumerate(self.chain.muon_listTrigChains):
          if trig in self.store["ChainsWithMuon"].keys(): continue
          self.store["ChainsWithMuon"][trig] = i


      # initialise the different slices
      """
      pt_slice = {}
      if self.key == "jets": 
        if self.sampletype == "mc": pt_slice = jet_trigger_slice[self.samplename["mc"]]
        else:                       pt_slice = jet_trigger_slice[self.samplename[:6]]
      if self.key == "muons": pt_slice = mu_trigger_slice
      """

      if not "reqTrig" in self.store.keys():
        self.store["reqTrig"] = self.required_triggers
    
      prescale_info = None
      if self.sampletype == "mc" or not (self.get_prescales_lumi or self.get_prescales_std):
        prescale_info = self.chain.passedTriggers
      elif self.get_prescales_lumi:
        prescale_info = self.chain.triggerPrescalesLumi
      elif self.get_prescales_std:
        prescale_info = self.chain.triggerPrescales


      if not "passTrig" in self.store.keys():
        self.store["passTrig"] = {}
        for trig,presc in zip(self.chain.passedTriggers,prescale_info):
          self.store["passTrig"][trig] = {"prescale":presc, "pt_slice":(0., nolim * GeV)}
          #if trig in pt_slice.keys():
          #self.store["passTrig"][trig] = {"prescale":presc, "pt_slice":pt_slice[trig]}

      if not "disTrig" in self.store.keys():
        self.store["disTrig"] = {}
        for trig in self.chain.disabledTriggers:
          self.store["disTrig"][trig] = {"prescale":1, "pt_slice":(0., nolim * GeV)}
          #if trig in pt_slice.keys():
          #self.store["disTrig"][trig] = {"prescale":1, "pt_slice":pt_slice[trig]}

      return True

#-------------------------------------------------------------------------------
class Particle(pyframe.core.ParticleProxy):
    """
    Variables added to the particle
    """
    #__________________________________________________________________________
    def __init__(self, particle, **kwargs):
        pyframe.core.ParticleProxy.__init__(self, 
             tree_proxy = particle.tree_proxy,
             index      = particle.index,
             prefix     = particle.prefix)   
        self.particle = particle
        self.__dict__ = particle.__dict__.copy() 
    
    #__________________________________________________________________________
    def isMatchedToTrigChain(self):
      return self.isTrigMatched

    # https://svnweb.cern.ch/trac/atlasoff/browser/PhysicsAnalysis/MCTruthClassifier/tags/MCTruthClassifier-00-00-26/MCTruthClassifier/MCTruthClassifierDefs.h
    # https://twiki.cern.ch/twiki/bin/view/AtlasProtected/MCTruthClassifier 
    #__________________________________________________________________________
    def isTrueNonIsoMuon(self):
      matchtype = self.truthType in [5,7,8]
      #return self.isTruthMatchedToMuon and matchtype
      return matchtype
    #__________________________________________________________________________
    def isTrueIsoMuon(self):
      matchtype = self.truthType in [6]
      #return self.isTruthMatchedToMuon and matchtype
      return matchtype
    #__________________________________________________________________________
    def isTrueHadTau(self):
      matchtype = False
      if hasattr(self, 'isTrueHadronicTau'):
        matchtype = self.isTrueHadronicTau in [1]
      return matchtype

    #__________________________________________________________________________
    def width(self):
      assert "tau" in self.prefix, "ERROR: accessing tracks but particle is not a tau" 
      
      num = den = 0.
      tracks = self.tracks
      for track in tracks:
        num += self.tlv.DeltaR(track.tlv) * track.tlv.Pt()
        den += track.tlv.Pt()
      return num/ den


#------------------------------------------------------------------------------
class ParticlesBuilder(pyframe.core.Algorithm):
    #__________________________________________________________________________
    def __init__(self, name="ParticlesBuilder", key=""):
        pyframe.core.Algorithm.__init__(self, name=name)
        self.key  = key
    #__________________________________________________________________________
    def initialize(self):
        log.info('initialize single particles for %s ...' % self.key)
    #__________________________________________________________________________
    def execute(self,weight):
        self.store[self.key] = [Particle(copy(l)) for l in self.store[self.key]]


#------------------------------------------------------------------------------
class MuTauVars(pyframe.core.Algorithm):
          
    """
    computes variables for the di-tau selection
    """
    #__________________________________________________________________________
    def __init__(self, 
                 name        = 'VarsAlg',
                 key_taus    = 'taus',
                 key_muons   = 'muons',
                 key_met     = 'met_trk',
                 ):
        pyframe.core.Algorithm.__init__(self, name)
        self.key_muons = key_muons
        self.key_taus = key_taus
        self.key_met = key_met

    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)
        """
        computes variables and puts them in the store
        """

        ## get objects from event candidate
        ## --------------------------------------------------
        taus  = self.store[self.key_taus] 
        muons = self.store[self.key_muons]
        met   = self.store[self.key_met]
       
        # ---------------------------
        # at least a lepton and a jet
        # ---------------------------

        self.store['mutau_dphi'] = muons[0].tlv.DeltaPhi(taus[0].tlv)
        scdphi = 0.0
        scdphi += ROOT.TMath.Cos(met.tlv.Phi() - muons[0].tlv.Phi())
        scdphi += ROOT.TMath.Cos(met.tlv.Phi() - taus[0].tlv.Phi())
        self.store['mutau_scdphi'] = scdphi
       
        self.store['mutau_ptratio'] = muons[0].tlv.Pt() / taus[0].tlv.Pt()

        muon = muons[0]
        tau = taus[0] 
        muonT = ROOT.TLorentzVector()
        muonT.SetPtEtaPhiM( muon.tlv.Pt(), 0., muon.tlv.Phi(), muon.tlv.M() )
        tauT = ROOT.TLorentzVector()
        tauT.SetPtEtaPhiM( tau.tlv.Pt(), 0., tau.tlv.Phi(), tau.tlv.M() )
        
        self.store['mVisMT']     = (tau.tlv+muon.tlv).M()
        self.store['mTtotMT']    = (muonT + tauT + met.tlv).M()  

        return True



#------------------------------------------------------------------------------
class DiTauVars(pyframe.core.Algorithm):
          
    """
    computes variables for the di-tau selection
    """
    #__________________________________________________________________________
    def __init__(self, 
                 name        = 'VarsAlg',
                 key_leptons = 'taus',
                 key_jets    = 'jets',
                 key_met     = 'met_trk',
                 ):
        pyframe.core.Algorithm.__init__(self, name)
        self.key_leptons = key_leptons
        self.key_jets = key_jets
        self.key_met = key_met

    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)
        """
        computes variables and puts them in the store
        """

        ## get objects from event candidate
        ## --------------------------------------------------
        assert self.store.has_key(self.key_leptons), "leptons key: %s not found in store!" % (self.key_leptons)
        taus = self.store[self.key_leptons] # well duh ...
        met = self.store[self.key_met]
        jets = self.store[self.key_jets]
       
        prefix = ""
        if self.key_leptons == "taus": prefix = "tau"

        # ---------------------------
        # at least a lepton and a jet
        # ---------------------------

        self.store['ditau_dphi'] = taus[0].tlv.DeltaPhi(taus[1].tlv)
        scdphi = 0.0
        scdphi += ROOT.TMath.Cos(met.tlv.Phi() - taus[0].tlv.Phi())
        scdphi += ROOT.TMath.Cos(met.tlv.Phi() - taus[1].tlv.Phi())
        self.store['ditau_scdphi'] = scdphi
       
        self.store['ditau_ptratio'] = taus[0].tlv.Pt() / taus[1].tlv.Pt()

        tau1 = taus[0]
        tau2 = taus[1] 
        tau1T = ROOT.TLorentzVector()
        tau1T.SetPtEtaPhiM( tau1.tlv.Pt(), 0., tau1.tlv.Phi(), tau1.tlv.M() )
        tau2T = ROOT.TLorentzVector()
        tau2T.SetPtEtaPhiM( tau2.tlv.Pt(), 0., tau2.tlv.Phi(), tau2.tlv.M() )
        
        self.store['mVisTT']           = (tau2.tlv+tau1.tlv).M()
        self.store['mTtotTT']          = (tau1T + tau2T + met.tlv).M()  

        return True


#------------------------------------------------------------------------------
class JetsBuilder(pyframe.core.Algorithm):
          
    """
    builds tight jet collection
    """
    #__________________________________________________________________________
    def __init__(self, 
                 name        = 'BuildJets',
                 key_met     = 'met_trk',
                 build_trigger_jets = False,
                 ):
        pyframe.core.Algorithm.__init__(self, name)
        self.key_met = key_met
        self.build_trigger_jets = build_trigger_jets

    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)
        """
        computes variables and puts them in the store
        """
        jets_tight = []
        jets_nontight = []
        
        met = self.store[self.key_met]
        jets = self.store['jets']
        
        # -------------------------
        # build tight jets
        # -------------------------
        for jet in jets:
          if jet.JvtPass_Medium and jet.fJvtPass_Medium and abs(jet.eta) <= 2.8:
            jets_tight += [jet]
          else:
            jets_nontight += [jet]
        
        jets_tight.sort(key=lambda x: x.tlv.Pt(), reverse=True )
        jets_nontight.sort(key=lambda x: x.tlv.Pt(), reverse=True )
        
        if len(jets_tight) > 1:
          assert jets_tight[0].tlv.Pt() >= jets_tight[1].tlv.Pt(), "jets_tight not sorted.."
          jet1 = jets[0]
          jet2 = jets[1] 
          jet1T = ROOT.TLorentzVector()
          jet1T.SetPtEtaPhiM( jet1.tlv.Pt(), 0., jet1.tlv.Phi(), jet1.tlv.M() )
          jet2T = ROOT.TLorentzVector()
          jet2T.SetPtEtaPhiM( jet2.tlv.Pt(), 0., jet2.tlv.Phi(), jet2.tlv.M() )
          
          self.store['mVisJJ']           = (jet2.tlv+jet1.tlv).M()
          self.store['mTtotJJ']          = (jet1T + jet2T + met.tlv).M()  

        if len(jets_nontight) > 1:
          assert jets_nontight[0].tlv.Pt() >= jets_nontight[1].tlv.Pt(), "jets_nontight not sorted.."
        self.store['jets_tight'] = jets_tight        
        self.store['jets_nontight'] = jets_nontight        
        
        # -------------------------
        # build trigger jets
        # -------------------------
        if self.build_trigger_jets:
          if len(self.store['trigJetsISFS']) > 0: 
            self.store['trigJets'] = self.store['trigJetsISFS']
          elif len(self.store['trigJetsFS']) > 0: 
            self.store['trigJets'] = self.store['trigJetsFS']

          if 'trigJets' in self.store:
            self.store['jetTrigJet_ptratio'] = self.store['jets'][0].tlv.Pt() / self.store['trigJets'][0].tlv.Pt()
            self.store['jetTrigJet_deltaR'] = self.store['jets'][0].tlv.DeltaR(self.store['trigJets'][0].tlv)

        return True

#------------------------------------------------------------------------------
class DiJetVars(pyframe.core.Algorithm):
          
    """
    computes variables for the di-jet selection used for
    tau fake-factor measurement
    """
    #__________________________________________________________________________
    def __init__(self, 
                 name        = 'VarsAlg',
                 key_leptons = 'taus',
                 key_jets    = 'jets',
                 key_met     = 'met_trk',
                 build_trigger_jets = False,
                 ):
        pyframe.core.Algorithm.__init__(self, name)
        self.key_leptons = key_leptons
        self.key_jets = key_jets
        self.key_met = key_met
        self.build_trigger_jets = build_trigger_jets

    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)
        """
        computes variables and puts them in the store
        """

        ## get objects from event candidate
        ## --------------------------------------------------
        assert self.store.has_key(self.key_leptons), "leptons key: %s not found in store!" % (self.key_leptons)
        leptons = self.store[self.key_leptons]
        met = self.store[self.key_met]
        jets = self.store[self.key_jets]
       
        prefix = ""
        if self.key_leptons == "muons": prefix = "mu"
        if self.key_leptons == "taus": prefix = "tau"

        # ---------------------------
        # at least a lepton and a jet
        # ---------------------------
        
        if bool(len(jets)) and bool(len(leptons)):
          self.store['%sjet_dphi'%prefix] = leptons[0].tlv.DeltaPhi(jets[0].tlv)
          scdphi = 0.0
          scdphi += ROOT.TMath.Cos(met.tlv.Phi() - leptons[0].tlv.Phi())
          scdphi += ROOT.TMath.Cos(met.tlv.Phi() - jets[0].tlv.Phi())
          self.store['%sjet_scdphi'%prefix] = scdphi
       
          self.store['%sjet_ptratio'%prefix] = leptons[0].tlv.Pt() / jets[0].tlv.Pt()
      

        # ---------------------------
        # at least two leptons
        # ---------------------------

        if len(leptons)>1:
          self.store['%ssubleadlead_ptratio'%prefix] = leptons[1].tlv.Pt() / leptons[0].tlv.Pt()

        return True

       

#------------------------------------------------------------------------------
class DiMuVars(pyframe.core.Algorithm):
    """
    computes variables for the di-muon selection
    """
    #__________________________________________________________________________
    def __init__(self, 
                 name      = 'DiMuVars',
                 key_muons = 'muons',
                 key_met   = 'met_trk',
                 ):
        pyframe.core.Algorithm.__init__(self, name)
        self.key_muons = key_muons
        self.key_met   = key_met

    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)
        """
        computes variables and puts them in the store
        """

        ## get objects from event candidate
        ## --------------------------------------------------
        assert self.store.has_key(self.key_muons), "muons key: %s not found in store!" % (self.key_muons)
        muons = self.store[self.key_muons]
        met = self.store[self.key_met]
        
        # ------------------
        # at least two muons
        # ------------------
        
        # dict containing pair 
        # and significance
        ss_pairs = {} 
        if len(muons)>=2:
          muon1 = self.store['muons'][0]
          muon2 = self.store['muons'][1] 
          muon1T = ROOT.TLorentzVector()
          muon1T.SetPtEtaPhiM( muon1.tlv.Pt(), 0., muon1.tlv.Phi(), muon1.tlv.M() )
          muon2T = ROOT.TLorentzVector()
          muon2T.SetPtEtaPhiM( muon2.tlv.Pt(), 0., muon2.tlv.Phi(), muon2.tlv.M() )
        
          #self.store['charge_product'] = muon2.trkcharge*muon1.trkcharge
          self.store['mVisMM']           = (muon2.tlv+muon1.tlv).M()
          self.store['mTtotMM']          = (muon1T + muon2T + met.tlv).M()  
          #self.store['muons_dphi']     = muon2.tlv.DeltaPhi(muon1.tlv)
          #self.store['muons_deta']     = muon2.tlv.Eta()-muon1.tlv.Eta()
          #self.store['muons_pTH']      = (muon2.tlv+muon1.tlv).Pt()
          #self.store['muons_dR']       = math.sqrt(self.store['muons_dphi']**2 + self.store['muons_deta']**2)

          """
          for p in combinations(muons,2):
            if p[0].trkcharge * p[1].trkcharge > 0.:
              ss_pairs[p] = abs(p[0].trkd0sig) + abs(p[1].trkd0sig)
          
          max_sig  = 1000.
          for pair,sig in ss_pairs.iteritems():
            if sig < max_sig: 
              if pair[0].tlv.Pt() > pair[1].tlv.Pt():
                self.store['muon1'] = pair[0]
                self.store['muon2'] = pair[1]
              else: 
                self.store['muon1'] = pair[1]
                self.store['muon2'] = pair[0]
              max_sig = sig 
          """
        
        """ 
        if ss_pairs:
          muon1 = self.store['muon1'] 
          muon2 = self.store['muon2'] 
          muon1T = ROOT.TLorentzVector()
          muon1T.SetPtEtaPhiM( muon1.tlv.Pt(), 0., muon1.tlv.Phi(), muon1.tlv.M() )
          muon2T = ROOT.TLorentzVector()
          muon2T.SetPtEtaPhiM( muon2.tlv.Pt(), 0., muon2.tlv.Phi(), muon2.tlv.M() )
        
          self.store['charge_product'] = muon2.trkcharge*muon1.trkcharge
          self.store['mVis']           = (muon2.tlv+muon1.tlv).M()
          self.store['mTtot']          = (muon1T + muon2T + met.tlv).M()  
          self.store['muons_dphi']     = muon2.tlv.DeltaPhi(muon1.tlv)
          self.store['muons_deta']     = muon2.tlv.Eta()-muon1.tlv.Eta()
          self.store['muons_pTH']      = (muon2.tlv+muon1.tlv).Pt()
          self.store['muons_dR']       = math.sqrt(self.store['muons_dphi']**2 + self.store['muons_deta']**2)
        """ 
        """  
        # puts additional muons in the store
        if ss_pairs and len(muons)>2:
           i = 2
           for m in muons:
             if m==self.store['muon1'] or m==self.store['muon2']: continue
             i = i + 1
             self.store['muon%d'%i] = m
        """
        return True


#------------------------------------------------------------------------------
class MultiMuVars(pyframe.core.Algorithm):
    """
    computes variables for the di-muon selection
    """
    #__________________________________________________________________________
    def __init__(self, 
                 name      = 'MultiMuVars',
                 key_muons = 'muons',
                 key_met   = 'met_trk',
                 ):
        pyframe.core.Algorithm.__init__(self, name)
        self.key_muons = key_muons
        self.key_met   = key_met

    #__________________________________________________________________________
    def execute(self, weight):
        pyframe.core.Algorithm.execute(self, weight)
        """
        computes variables and puts them in the store
        """

        ## get objects from event candidate
        ## --------------------------------------------------
        assert self.store.has_key(self.key_muons), "muons key: %s not found in store!" % (self.key_muons)
        muons = self.store[self.key_muons]

        #--------------------
        # two same-sign pairs
        #--------------------
        two_pairs = {}
        if len(muons)>=4:
          for q in combinations(muons,4):
            if q[0].trkcharge * q[1].trkcharge * q[2].trkcharge * q[3].trkcharge > 0.0:
              two_pairs[q] = abs(q[0].trkd0sig) + abs(q[1].trkd0sig) + abs(q[2].trkd0sig) + abs(q[3].trkd0sig)

          max_sig  = 1000.
          for quad,sig in two_pairs.iteritems():

            if sig < max_sig:
              max_sig = sig 

              #Case 1: total charge 0
              if quad[0].trkcharge + quad[1].trkcharge + quad[2].trkcharge + quad[3].trkcharge == 0:
                for p in combinations(quad,2):
                  if (p[0].trkcharge + p[1].trkcharge) == 2:
                    if p[0].tlv.Pt() > p[1].tlv.Pt():
                      self.store['muon1'] = p[0]
                      self.store['muon2'] = p[1]
                    else:
                      self.store['muon1'] = p[1]
                      self.store['muon2'] = p[0]
                  elif (p[0].trkcharge + p[1].trkcharge) == -2:
                    if p[0].tlv.Pt() > p[1].tlv.Pt():
                      self.store['muon3'] = p[0]
                      self.store['muon4'] = p[1]
                    else:
                      self.store['muon3'] = p[1]
                      self.store['muon4'] = p[0]

              #Case 2: Total Charge = +/- 4
              elif abs(quad[0].trkcharge + quad[1].trkcharge + quad[2].trkcharge + quad[3].trkcharge) == 4:
                print("This event has charge 4!\n") #print for debugging purposes 
                self.store['muon1'] = quad[0]
                self.store['muon2'] = quad[1]
                self.store['muon3'] = quad[2]
                self.store['muon4'] = quad[3]

              #Failsafe
              else:
                print("Error: Something has gone horribly wrong with this event!\n")
                self.store['muon1'] = quad[0]
                self.store['muon2'] = quad[1]
                self.store['muon3'] = quad[2]
                self.store['muon4'] = quad[3]

        if two_pairs:
          muon1 = self.store['muon1']
          muon2 = self.store['muon2']
          muon1T = ROOT.TLorentzVector()
          muon1T.SetPtEtaPhiM( muon1.tlv.Pt(), 0., muon1.tlv.Phi(), muon1.tlv.M() )
          muon2T = ROOT.TLorentzVector()
          muon2T.SetPtEtaPhiM( muon2.tlv.Pt(), 0., muon2.tlv.Phi(), muon2.tlv.M() )

          self.store['charge_product1'] = muon2.trkcharge*muon1.trkcharge
          self.store['charge_sum1']     = muon1.trkcharge + muon2.trkcharge
          self.store['mVis1']           = (muon2.tlv+muon1.tlv).M()
          self.store['muons_dphi1']     = muon2.tlv.DeltaPhi(muon1.tlv)
          self.store['muons_deta1']     = muon2.tlv.Eta()-muon1.tlv.Eta()
          self.store['pTH1']            = (muon2.tlv+muon1.tlv).Pt()
          self.store['muons_dR1']       = math.sqrt(self.store['muons_dphi1']**2 + self.store['muons_deta1']**2)

          muon3 = self.store['muon3']
          muon4 = self.store['muon4']
          muon3T = ROOT.TLorentzVector()
          muon3T.SetPtEtaPhiM( muon3.tlv.Pt(), 0., muon3.tlv.Phi(), muon3.tlv.M() )
          muon4T = ROOT.TLorentzVector()
          muon4T.SetPtEtaPhiM( muon4.tlv.Pt(), 0., muon4.tlv.Phi(), muon4.tlv.M() )

          self.store['charge_product2'] = muon4.trkcharge*muon3.trkcharge
          self.store['charge_sum2']     = muon3.trkcharge + muon4.trkcharge
          self.store['mVis2']           = (muon4.tlv+muon3.tlv).M()
          self.store['muons_dphi2']     = muon4.tlv.DeltaPhi(muon3.tlv)
          self.store['muons_deta2']     = muon4.tlv.Eta()-muon3.tlv.Eta()
          self.store['pTH2']            = (muon4.tlv+muon3.tlv).Pt()
          self.store['muons_dR2']       = math.sqrt(self.store['muons_dphi2']**2 + self.store['muons_deta2']**2)

          self.store['charge_product'] = muon4.trkcharge * muon3.trkcharge * muon2.trkcharge * muon1.trkcharge
          self.store['charge_sum']     = muon1.trkcharge + muon2.trkcharge + muon3.trkcharge + muon4.trkcharge
          self.store['mTtot']          = (muon1T + muon2T + muon3T + muon4T + met.tlv).M()
          self.store['mVis']           = (self.store['mVis1']+self.store['mVis2'])/2
          self.store['dmVis']          = self.store['mVis1'] - self.store['mVis2']
          self.store['pairs_dphi']     = (muon3.tlv+muon4.tlv).DeltaPhi(muon1.tlv+muon2.tlv)
          self.store['pairs_deta']     = (muon3.tlv+muon4.tlv).Eta()-(muon1.tlv+muon2.tlv).Eta()
          self.store['pairs_dR']       = math.sqrt(self.store['pairs_dphi']**2 + self.store['pairs_deta']**2)

        return True


# EOF 


