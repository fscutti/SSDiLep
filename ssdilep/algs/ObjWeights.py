#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ObjWeights.py: 
weights applied 
to single objects
"""

from math import sqrt
from array import array
from copy import copy

# logging
import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# ROOT
import ROOT
import metaroot

# pyframe
import pyframe

# pyutils
import rootutils

from units import GeV

#------------------------------------------------------------------------------
class MuAllSF(pyframe.core.Algorithm):
    """
    Single muon efficiencies: reco + iso + ttva
    """
    #__________________________________________________________________________
    def __init__(self, name="MuAllSF",
            mu_index   = None,
            mu_iso     = None,
            mu_reco    = None,
            mu_ttva    = None, # not really any choice here!
            key        = None,
            scale      = None,
            ):
        pyframe.core.Algorithm.__init__(self, name=name)
        self.mu_index  = mu_index
        self.mu_iso    = mu_iso
        self.mu_reco   = mu_reco
        self.mu_ttva   = mu_ttva
        self.key       = key
        self.scale     = scale

        assert key, "Must provide key for storing mu sf"
    
    #_________________________________________________________________________
    def initialize(self): 
      pass
    
    #_________________________________________________________________________
    def execute(self, weight):
        
        sf=1.0
        muons = self.store['muons']
        
        if self.mu_index in ['tag','probe']:
          muon = self.store[self.mu_index]
        
        if self.mu_index < len(muons): 
          muon = muons[self.mu_index]
        
          if "mc" in self.sampletype: 
            
            if muon.isTrueIsoMuon():
              if not ("Not" in self.mu_iso):
                sf *= getattr(muon,"_".join(["IsoEff","SF","Iso"+self.mu_iso])).at(0)
                # EXOT12 v1 ntuples 
                #sf *= getattr(muon,"_".join(["IsoEff","SF",self.mu_iso])).at(0)
              if not ("Not" in self.mu_reco):
                sf *= getattr(muon,"_".join(["RecoEff","SF","Reco"+self.mu_reco])).at(0)
                # EXOT12 v1 ntuples 
                #sf *= getattr(muon,"_".join(["RecoEff","SF",self.mu_reco])).at(0)
              
              sf *= getattr(muon,"_".join(["TTVAEff","SF"])).at(0)
          
              if self.scale: pass

        if self.key: 
          self.store[self.key] = sf
        return True


#------------------------------------------------------------------------------
class TauAllSF(pyframe.core.Algorithm):
    """
    Single tau efficiencies: reco + eleOLR + ID 
    """
    #__________________________________________________________________________
    def __init__(self, name="TauAllSF",
            tau_index = None,
            tau_eolr  = None,
            tau_id    = None,
            key       = None,
            scale     = None,
            ):
        pyframe.core.Algorithm.__init__(self, name=name)
        self.tau_index = tau_index
        self.tau_eolr  = tau_eolr
        self.tau_id    = tau_id
        self.key       = key
        self.scale     = scale

        assert key, "Must provide key for storing tau sf"
    
    #_________________________________________________________________________
    def initialize(self): 
      pass
    
    #_________________________________________________________________________
    def execute(self, weight):
        
        sf=1.0
        taus = self.store['taus']
        
        if self.tau_index < len(taus): 
          tau = taus[self.tau_index]
        
          if "mc" in self.sampletype: 
            sf *= getattr(tau,"_".join(["TauEff","SF","EleOLRElectronEleBDT"+self.tau_eolr,"TauID"+self.tau_id])).at(0)
          
            if self.scale: pass

        if self.key: 
          self.store[self.key] = sf
        return True



#------------------------------------------------------------------------------
class MuFakeFactorGraph(pyframe.core.Algorithm):
    """
    Applies the fake-factors to muon pairs
    """
    #__________________________________________________________________________
    def __init__(self, name="MuFakeFactor",config_file=None,mu_index=None,key=None,scale=None):
        pyframe.core.Algorithm.__init__(self,name=name)
        self.config_file    = config_file
        self.mu_index       = mu_index
        self.key            = key
        self.scale          = scale
        
        assert config_file, "Must provide config file!"
        assert key, "Must provide key for storing fakefactor"
    #_________________________________________________________________________
    def initialize(self):
        f = ROOT.TFile.Open(self.config_file)
        assert f, "Failed to open fake-factor config file: %s"%(self.config_file)

        g_ff = f.Get("g_ff_stat_sys")
        assert g_ff, "Failed to get 'g_ff' from %s"%(self.config_file)
        
        self.g_ff = g_ff.Clone()
        f.Close()
    #_________________________________________________________________________
    def execute(self, weight):
        
        ff_mu = 1.0 
        muons = self.store['muons']
         
        if self.mu_index < len(muons): 
        
          mu = muons[self.mu_index]
          pt_mu = mu.tlv.Pt()/GeV  
          
          for ibin_mu in xrange(1,self.g_ff.GetN()):
            edlow = self.g_ff.GetX()[ibin_mu] - self.g_ff.GetEXlow()[ibin_mu]
            edhi  = self.g_ff.GetX()[ibin_mu] + self.g_ff.GetEXhigh()[ibin_mu]
            if pt_mu>=edlow and pt_mu<edhi: break
          
          # error bars are asymmetric
          ff_mu = self.g_ff.GetY()[ibin_mu]
          eff_up_mu = self.g_ff.GetEYhigh()[ibin_mu]
          eff_dn_mu = self.g_ff.GetEYlow()[ibin_mu]
          
          if self.scale == 'up': ff_mu +=eff_up_mu
          if self.scale == 'dn': ff_mu -=eff_dn_mu
       
        if self.key: 
          self.store[self.key] = ff_mu

        return True



#------------------------------------------------------------------------------
class TauFakeFactorGraph(pyframe.core.Algorithm):
    """
    Applies the fake-factors to tau pairs
    """
    #__________________________________________________________________________
    def __init__(self, name="TauFakeFactor",config_file=None,tau_index=None,key=None,scale=None):
        pyframe.core.Algorithm.__init__(self,name=name)
        self.config_file    = config_file
        self.tau_index      = tau_index
        self.key            = key
        self.scale          = scale

        assert config_file, "Must provide config file!"
        assert key, "Must provide key for storing fakefactor"
    #_________________________________________________________________________
    def initialize(self):
        f1P = ROOT.TFile.Open(self.config_file[0])
        f3P = ROOT.TFile.Open(self.config_file[1])
        
        assert f1P, "Failed to open fake-factor config file: %s"%(self.config_file[0])
        assert f3P, "Failed to open fake-factor config file: %s"%(self.config_file[1])
        
        g_ff_1P = f1P.Get("g_ff_stat_sys")
        g_ff_3P = f3P.Get("g_ff_stat_sys")
        
        assert g_ff_1P, "Failed to get 'g_ff' from %s"%(self.config_file)
        assert g_ff_3P, "Failed to get 'g_ff' from %s"%(self.config_file)

        self.g_ff_1P = g_ff_1P.Clone()
        self.g_ff_3P = g_ff_3P.Clone()

        f1P.Close()
        f3P.Close()
    #_________________________________________________________________________
    def execute(self, weight):

        ff_tau = 1.0
        taus = self.store['taus']

        if self.tau_index < len(taus):

          tau = taus[self.tau_index]
          pt_tau = tau.tlv.Pt() / GeV
          if tau.ntrk == 1:
            self.g_ff = self.g_ff_1P
          if tau.ntrk == 3:
            self.g_ff = self.g_ff_3P
          for ibin_tau in xrange(1,self.g_ff.GetN()):
            edlow = self.g_ff.GetX()[ibin_tau] - self.g_ff.GetEXlow()[ibin_tau]
            edhi  = self.g_ff.GetX()[ibin_tau] + self.g_ff.GetEXhigh()[ibin_tau]
            if pt_tau>=edlow and pt_tau<edhi: break

          # error bars are asymmetric
          ff_tau = self.g_ff.GetY()[ibin_tau]
          eff_up_tau = self.g_ff.GetEYhigh()[ibin_tau]
          eff_dn_tau = self.g_ff.GetEYlow()[ibin_tau]

          if self.scale == 'up': ff_tau +=eff_up_tau
          if self.scale == 'dn': ff_tau -=eff_dn_tau

        if self.key:
          self.store[self.key] = ff_tau

        return True

#------------------------------------------------------------------------------
class JetPtWeightHist(pyframe.core.Algorithm):
    """
    Applies pt re-weighting of the jet pt
    """
    #__________________________________________________________________________
    def __init__(self, name="JetPtWeight",config_file=None,key=None,scale=None):
        pyframe.core.Algorithm.__init__(self,name=name)
        self.config_file    = config_file
        self.key            = key
        self.scale          = scale
        
        assert config_file, "Must provide config file!"
        assert key, "Must provide key for storing weight"
    #_________________________________________________________________________
    def initialize(self):
        f = ROOT.TFile.Open(self.config_file)
        assert f, "Failed to open weights config file: %s"%(self.config_file)

        h_weights = copy(f.Get("weights_reb").Clone())
        f.Close()
        assert h_weights, "Failed to get 'h_weights' from %s"%(self.config_file)
        self.h_weights = h_weights
    #_________________________________________________________________________
    def execute(self, weight):
        
        w_jet = 1.0 
        jet = self.store['jets'][0]
         
        pt_jet = jet.tlv.Pt()/GeV  
        if pt_jet < 250.:
          w_jet = self.h_weights.GetBinContent( self.h_weights.FindBin(pt_jet) )
        else: pass 
        
        if self.scale == 'up': pass
        if self.scale == 'dn': pass
       
        if self.key: 
          self.store[self.key] = w_jet

        return True


#------------------------------------------------------------------------------
class FakeFactor(pyframe.core.Algorithm):
    """
    Applies the fake-factors to muon pairs
    """
    #__________________________________________________________________________
    def __init__(self, 
                 name                     = "FakeFactor",
                 config_file_light_lepton = None,
                 config_file_tau_lepton   = [],
                 exclude_obj              = [],
                 key                      = None,
                 scale                    = None
                 ):
        pyframe.core.Algorithm.__init__(self,name=name)
        
        self.config_file_light_lepton  = config_file_light_lepton
        self.config_file_tau_lepton    = config_file_tau_lepton
        self.exclude_obj               = exclude_obj
        self.key                       = key
        self.scale                     = scale
        
        assert config_file_light_lepton, "Must provide config file for light leptons!"
        assert config_file_tau_lepton,   "Must provide config file for tau leptons!"
        assert key, "Must provide key for storing fakefactor"
    #_________________________________________________________________________
    def initialize(self):
        f_lep = ROOT.TFile.Open(self.config_file_light_lepton)
        f_tau_1p = ROOT.TFile.Open(self.config_file_tau_lepton[0])
        f_tau_3p = ROOT.TFile.Open(self.config_file_tau_lepton[1])

        assert f_lep, "Failed to open fake-factor config file: %s"%(self.config_file_light_lepton)
        assert f_tau_1p, "Failed to open fake-factor config file: %s"%(self.config_file_tau_lepton[0])
        assert f_tau_3p, "Failed to open fake-factor config file: %s"%(self.config_file_tau_lepton[1])
        
        H_ff = dict()
       
        tau_ff_name_1p = ""
        tau_ff_name_3p = ""

        if "FFDijet" in self.key:
          tau_ff_name_1p = "h_ff_1PMedium_F10"
          tau_ff_name_3p = "h_ff_3PMedium_F10"
        
        elif "FFMultilep2L" in self.key:
          tau_ff_name_1p = "h_ff_taulead_pt_1DF2L_ANTImTtot300"
          tau_ff_name_3p = "h_ff_taulead_pt_1DF2L_ANTImTtot300"
        
        elif "FFMultilep3L" in self.key:
          tau_ff_name_1p = "h_ff_taulead_pt_1DF3L_ANTImTtot300"
          tau_ff_name_3p = "h_ff_taulead_pt_1DF3L_ANTImTtot300"


        H_ff["muon"]   = f_lep.Get("m/highPt_anyjet/FF")
        H_ff["el"]     = f_lep.Get("e/highPt_anyjet/FF")
        H_ff["tau_1p"] = f_tau_1p.Get(tau_ff_name_1p)
        H_ff["tau_3p"] = f_tau_3p.Get(tau_ff_name_3p)

        assert H_ff["muon"],   "Failed to get 'H_ff_mu' from %s"%(self.config_file_light_lepton)
        assert H_ff["el"],     "Failed to get 'H_ff_el' from %s"%(self.config_file_light_lepton)
        assert H_ff["tau_1p"], "Failed to get 'H_ff_tau_1p' from %s"%(self.config_file_tau_lepton[0])
        assert H_ff["tau_3p"], "Failed to get 'H_ff_tau_3p' from %s"%(self.config_file_tau_lepton[1])
        
        self.H_ff = dict()
        self.H_ff["muon"]   = copy(H_ff["muon"])
        self.H_ff["el"]     = copy(H_ff["el"])
        self.H_ff["tau_1p"] = copy(H_ff["tau_1p"])
        self.H_ff["tau_3p"] = copy(H_ff["tau_3p"])

        f_lep.Close()
        f_tau_1p.Close()
        f_tau_3p.Close()
    
    #_________________________________________________________________________
    def execute(self, weight):
        ff_lep  = 1.0 
        ff_sign = -1.
        
        leptons = []
        for obj in ['muons','taus','electrons']:
          if obj in self.exclude_obj: continue
          leptons += self.store[obj]
        
        met = self.store["met_trk"].tlv.Pt() / GeV
        
        for lep in leptons:
          if lep.isFail():
            
            ff_sign *= -1.
            
            lep_pt = lep.tlv.Pt() / GeV
            lep_eta = lep.tlv.Eta()
            
            if "tau" in lep.prefix:
              bin_idx = self.H_ff["tau_"+str(lep.ntrk)+"p"].FindBin(lep_pt)
              ff_lep *= self.H_ff["tau_"+str(lep.ntrk)+"p"].GetBinContent(bin_idx)
            
            else:
              
              maxPt = self.H_ff[lep.prefix.strip("_")].GetXaxis().GetBinCenter(self.H_ff[lep.prefix.strip("_")].GetNbinsX())
              minMet = self.H_ff[lep.prefix.strip("_")].GetZaxis().GetBinCenter(1)
              maxMet = self.H_ff[lep.prefix.strip("_")].GetZaxis().GetBinCenter(self.H_ff[lep.prefix.strip("_")].GetNbinsZ())
              
              bin_idx = self.H_ff[lep.prefix.strip("_")].FindBin(min(lep_pt,maxPt), lep_eta, max(min(met, maxMet), minMet))
              ff_lep *= self.H_ff[lep.prefix.strip("_")].GetBinContent(bin_idx)

            ff_lep *= ff_sign

        if self.key: 
          self.store[self.key] = ff_lep

        return True


#EOF
