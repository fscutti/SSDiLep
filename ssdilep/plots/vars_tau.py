# encoding: utf-8
'''
vars_mumu.py
description:
variables for the mumu channel
'''

## modules
from var import Var


## Event variables
## ---------------------------------------
njets = Var(name = 'njets',
              path  = 'event',
              xmin  = 0,
              xmax  = 6,
              log   = False,
              )
ntaus = Var(name = 'ntaus',
              path  = 'event',
              xmin  = 0,
              xmax  = 6,
              log   = False,
              )

taujet_dphi = Var(name = 'taujet_dphi',
              path    = 'event',
              xmin    = -3.2,
              xmax    = 3.2,
              rebin   = 4,
              log     = False,
              )

taujet_ptratio = Var(name = 'taujet_ptratio',
              path    = 'event',
              xmin    = 0.,
              xmax    = 2.,
              rebin   = 4,
              log     = False,
              )

ditau_ptratio = Var(name = 'ditau_ptratio',
              path    = 'event',
              xmin    = 0.,
              xmax    = 2.,
              rebin   = 4,
              log     = False,
              )

jetTrigJet_ptratio = Var(name = 'jetTrigJet_ptratio',
              path    = 'event',
              xmin    = 0.,
              xmax    = 2.,
              rebin   = 1,
              log     = False,
              )

jetTrigJet_deltaR = Var(name = 'jetTrigJet_deltaR',
              path    = 'event',
              xmin    = 0.,
              xmax    = 5.,
              rebin   = 1,
              log     = False,
              )

taus_mVis = Var(name     = 'taus_mVis',
              path    = 'event',
              xmin    = 100.,
              xmax    = 1800.,
              rebin   = 40,
              log     = False,
              )

taus_mTtot = Var(name     = 'taus_mTtot',
              path    = 'event',
              xmin    = 100.,
              xmax    = 1800.,
              rebin   = 40,
              log     = False,
              )


## Single tau variables
## ---------------------------------------
taulead_JetBDTScore = Var(name = 'taulead_JetBDTScore',
              path   = 'taus',
              xmin   = -1.,
              xmax   = 1.,
              rebin  = 2,
              log    = False,
              )

taulead_JetBDTScoreSigTrans = Var(name = 'taulead_JetBDTScoreSigTrans',
              path   = 'taus',
              xmin   = 0.,
              xmax   = 1.,
              rebin  = 2,
              log    = False,
              )

tausublead_JetBDTScore = Var(name = 'tausublead_JetBDTScore',
              path   = 'taus',
              xmin   = -1.,
              xmax   = 1.,
              rebin  = 2,
              log    = False,
              )

tausublead_JetBDTScoreSigTrans = Var(name = 'tausublead_JetBDTScoreSigTrans',
              path   = 'taus',
              xmin   = 0.,
              xmax   = 1.,
              rebin  = 2,
              log    = False,
              )

taulead_pt = Var(name = 'taulead_pt',
              path   = 'taus',
              xmin   = 0.,
              xmax   = 600.,
              rebin  = 5,
              log    = False,
              )

tausublead_pt = Var(name = 'tausublead_pt',
              path   = 'taus',
              xmin   = 0.,
              xmax   = 400.,
              rebin  = 20,
              log    = False,
              )

taulead_eta = Var(name = 'taulead_eta',
              path    = 'taus',
              xmin    = -2.5,
              xmax    = 2.5,
              rebin   = 5,
              log     = False,
              )

tausublead_eta = Var(name = 'tausublead_eta',
              path    = 'taus',
              xmin    = -2.5,
              xmax    = 2.5,
              rebin   = 5,
              log     = False,
              )

taulead_phi = Var(name = 'taulead_phi',
              path    = 'taus',
              xmin    = -3.2,
              xmax    = 3.2,
              rebin   = 4,
              log     = False,
              )

tausublead_phi = Var(name = 'tausublead_phi',
              path    = 'taus',
              xmin    = -3.2,
              xmax    = 3.2,
              rebin   = 4,
              log     = False,
              )

## Tau track variables
## ---------------------------------------

taulead_ntracks = Var(name = 'taulead_ntracks',
              path   = 'taus',
              xmin   = 0,
              xmax   = 30,
              rebin  = 1,
              log    = False,
              )
taulead_trackwidth = Var(name = 'taulead_trackwidth',
              path   = 'taus',
              xmin   = 0.,
              xmax   = 1.,
              rebin  = 2,
              log    = False,
              )
taulead_angeec0 = Var(name = 'taulead_angeec0',
              path   = 'taus',
              xmin   = 0.,
              xmax   = 1.,
              rebin  = 2,
              log    = False,
              )
taulead_angeec02 = Var(name = 'taulead_angeec02',
              path   = 'taus',
              xmin   = 0.,
              xmax   = 1.,
              rebin  = 2,
              log    = False,
              )
taulead_angeec05 = Var(name = 'taulead_angeec05',
              path   = 'taus',
              xmin   = 0.,
              xmax   = 1.,
              rebin  = 2,
              log    = False,
              )
taulead_angeec1 = Var(name = 'taulead_angeec1',
              path   = 'taus',
              xmin   = 0.,
              xmax   = 1.,
              rebin  = 2,
              log    = False,
              )
taulead_jetwidth = Var(name = 'taulead_jetwidth',
              path   = 'taus',
              xmin   = 0.,
              xmax   = 1.,
              rebin  = 2,
              log    = False,
              )
taulead_tracksum = Var(name = 'taulead_tracksum',
              path   = 'taus',
              xmin   = 0.,
              xmax   = 600.,
              rebin  = 10,
              log    = False,
              )

## jets
## ---------------------------------------
jetlead_pt = Var(name = 'jetlead_pt',
              path   = 'jets',
              xmin   = 0.,
              xmax   = 600.,
              rebin  = 5,
              log    = False,
              )

jetlead_phi = Var(name = 'jetlead_phi',
              path    = 'jets',
              xmin    = -3.2,
              xmax    = 3.2,
              rebin   = 4,
              log     = False,
              )

jetlead_eta = Var(name = 'jetlead_eta',
              path    = 'jets',
              xmin    = -2.5,
              xmax    = 2.5,
              rebin   = 5,
              log     = False,
              )


trigJetlead_pt = Var(name = 'trigJetlead_pt',
              path   = 'jets',
              xmin   = 0.,
              xmax   = 600.,
              rebin  = 5,
              log    = False,
              )

trigJetlead_phi = Var(name = 'trigJetlead_phi',
              path    = 'jets',
              xmin    = -3.2,
              xmax    = 3.2,
              rebin   = 4,
              log     = False,
              )

trigJetlead_eta = Var(name = 'trigJetlead_eta',
              path    = 'jets',
              xmin    = -2.5,
              xmax    = 2.5,
              rebin   = 5,
              log     = False,
              )



## MET variables
## ---------------------------------------
met_trk_et = Var(name = 'met_trk_et',
              path    = 'met',
              xmin    = 0.,
              xmax    = 300.,
              rebin   = 10,
              log     = False,
              )

vars_list = []


# ---------------
# One tau
# ---------------
vars_list.append(taulead_pt)
vars_list.append(taulead_eta)
vars_list.append(taulead_phi)
vars_list.append(met_trk_et)
vars_list.append(jetlead_pt)
vars_list.append(jetlead_eta)
vars_list.append(jetlead_phi)

vars_list.append(trigJetlead_pt)
#vars_list.append(trigJetlead_eta)
#vars_list.append(trigJetlead_phi)

vars_list.append(taujet_ptratio)
vars_list.append(taujet_dphi)

#vars_list.append(jetTrigJet_ptratio)
#vars_list.append(jetTrigJet_deltaR)

vars_list.append(taulead_JetBDTScore)
vars_list.append(taulead_JetBDTScoreSigTrans)


# ---------------
# Two taus
# ---------------
#vars_list.append(tausublead_pt)
#vars_list.append(tausublead_eta)
#vars_list.append(tausublead_phi)
#vars_list.append(ditau_ptratio)
#vars_list.append(tausublead_JetBDTScore)
#vars_list.append(tausublead_JetBDTScoreSigTrans)

#vars_list.append(taus_mVis)
#vars_list.append(taus_mTtot)

#vars_list.append(ntaus)
vars_list.append(njets)


# ---------------
# Tracks study
# ---------------

vars_list.append(taulead_ntracks)
vars_list.append(taulead_trackwidth)
vars_list.append(taulead_angeec0)
vars_list.append(taulead_angeec02)
vars_list.append(taulead_angeec05)
vars_list.append(taulead_angeec1)
vars_list.append(taulead_jetwidth)
vars_list.append(taulead_tracksum)

vars_dict = {}
for var in vars_list: vars_dict[var.name] = var.__dict__


## EOF


