#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
met.py - For building met.
"""

import math
import os
import pyframe
import ROOT

from units import GeV

import logging
log = logging.getLogger(__name__)

def fatal(message):
    sys.exit("Fatal error in %s: %s" % (__file__, message))

#-------------------------------------------------------------------------------
class MET(object):
    """
    Simple MET class.
    """
    #__________________________________________________________________________
    def __init__(self, et, phi, sumet, sig):
        self.tlv = ROOT.TLorentzVector()
        self.tlv.SetPtEtaPhiM(et, 0.0, phi, 0.0)
        self.sumet = sumet
        self.sig = sig

#-------------------------------------------------------------------------------
class METCLUS(pyframe.core.Algorithm):
    """
    Load the MET directly from the mini-ntuples
    """
    #__________________________________________________________________________
    def __init__(self, name="METCLUS", key="", prefix=""):
        pyframe.core.Algorithm.__init__(self, name=name)
        self.key    = key
        self.prefix = prefix
    #__________________________________________________________________________
    def initialize(self):
        log.info('initialized METCLUS')
    #__________________________________________________________________________
    def execute(self, weight):
        self.store[self.key] = MET(
            getattr(self.chain, self.prefix), 
            getattr(self.chain, self.prefix+"Phi"), 
            getattr(self.chain, self.prefix+"SumEt"), 
            getattr(self.chain, self.prefix+"Significance")
            )


#-------------------------------------------------------------------------------
class METTRK(pyframe.core.Algorithm):
    """
    Load the MET directly from the mini-ntuples
    """
    #__________________________________________________________________________
    def __init__(self, name="METTRK", key="", prefix=""):
        pyframe.core.Algorithm.__init__(self, name=name)
        self.key    = key
        self.prefix = prefix
    #__________________________________________________________________________
    def initialize(self):
        log.info('initialized METTRK')
    #__________________________________________________________________________
    def execute(self, weight):
        self.store[self.key] = MET(
            getattr(self.chain, self.prefix), 
            getattr(self.chain, self.prefix+"Phi"), 
            getattr(self.chain, self.prefix+"SumEt"), 
            getattr(self.chain, self.prefix+"Significance"),
            )




