# encoding: utf-8
'''
vars_multipair.py
description:
variables for multipairs
'''

## modules
from var import Var
from itertools import combinations_with_replacement

sspairs_pt = Var(name = 'sspairs_pt',
              path   = 'pairs',
              xmin   = 0.,
              xmax   = 2000.,
              rebin  = 20,
              log    = False,
              )

sspairs_phi = Var(name = 'sspairs_phi',
              path   = 'pairs',
              xmin   = -3.2,
              xmax   = 3.2,
              rebin  = 4,
              log    = False,
              )

sspairs_eta = Var(name = 'sspairs_eta',
              path   = 'pairs',
              xmin   = -2.5,
              xmax   = 2.5,
              rebin  = 5,
              log    = False,
              )

sspairs_DR = Var(name = 'sspairs_DR',
              path   = 'pairs',
              xmin   = 0.,
              xmax   = 6.,
              rebin  = 2,
              invert_z = True,
              log    = False,
              )

sspairs_charge = Var(name = 'sspairs_charge',
              path   = 'pairs',
              xmin   = -3.,
              xmax   = 4.,
              rebin  = 1,
              log    = False,
              )

sspairs_mTtot = Var(name = 'sspairs_mTtot',
              path   = 'pairs',
              xmin   = 0.,
              xmax   = 2000.,
              rebin  = 20,
              log    = False,
              )

sspairs_mVis = Var(name = 'sspairs_mVis',
              path   = 'pairs',
              xmin   = 0.,
              xmax   = 2000.,
              rebin  = 20,
              log    = False,
              )

sspairs_avgM = Var(name = 'sspairs_avgM',
              path   = 'pairs',
              xmin   = 0.,
              xmax   = 2000.,
              rebin  = 20,
              log    = False,
              )

sspairs_DM = Var(name = 'sspairs_DM',
              path   = 'pairs',
              xmin   = -3.,
              xmax   = 3.,
              rebin  = 4,
              log    = False,
              )

sspairs_ID = Var(name = 'sspairs_ID',
              path   = 'pairs',
              anbins = [ pair[0]+pair[1] for pair in combinations_with_replacement([ lep[0]+lep[1] for lep in combinations_with_replacement(['El','Mu','Tau'],2)],2)],
              log    = False,
              )


vars_list = []
vars_list.append(sspairs_pt)
vars_list.append(sspairs_eta)
vars_list.append(sspairs_phi)
vars_list.append(sspairs_DR)
vars_list.append(sspairs_charge)
vars_list.append(sspairs_mTtot)
vars_list.append(sspairs_mVis)
vars_list.append(sspairs_avgM)
vars_list.append(sspairs_DM)
vars_list.append(sspairs_ID)


vars_dict = {}
for var in vars_list: vars_dict[var.name] = var.__dict__


## EOF


