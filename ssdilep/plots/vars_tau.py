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

tausubleadlead_ptratio = Var(name = 'tausubleadlead_ptratio',
              path    = 'event',
              xmin    = 0.,
              xmax    = 1.,
              rebin   = 4,
              log     = False,
              )




## Single muon variables
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


vars_list.append(taujet_ptratio)
vars_list.append(taujet_dphi)

vars_list.append(taulead_JetBDTScore)
vars_list.append(taulead_JetBDTScoreSigTrans)

# ---------------
# Two taus
# ---------------

#vars_list.append(tausublead_pt)
#vars_list.append(tausublead_eta)
#vars_list.append(tausublead_phi)
#vars_list.append(tausubleadlead_ptratio)


vars_dict = {}
for var in vars_list: vars_dict[var.name] = var.__dict__


## EOF


