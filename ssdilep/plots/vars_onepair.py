# encoding: utf-8
'''
vars_leadsspair.py
description:
variables for onepair
'''

## modules
from var import Var
from itertools import combinations_with_replacement

leadsspair_pt = Var(name = 'leadsspair_pt',
              path   = 'pairs',
              xmin   = 0.,
              xmax   = 2000.,
              rebin  = 20,
              log    = False,
              )

leadsspair_phi = Var(name = 'leadsspair_phi',
              path   = 'pairs',
              xmin   = -3.2,
              xmax   = 3.2,
              rebin  = 4,
              log    = False,
              )

leadsspair_eta = Var(name = 'leadsspair_eta',
              path   = 'pairs',
              xmin   = -2.5,
              xmax   = 2.5,
              rebin  = 5,
              log    = False,
              )

leadsspair_DR = Var(name = 'leadsspair_DR',
              path     = 'pairs',
              xmin     = 0.,
              xmax     = 6.,
              rebin    = 2,
              invert_z = True,
              log      = False,
              )

leadsspair_charge = Var(name = 'leadsspair_charge',
              path   = 'pairs',
              xmin   = -3.,
              xmax   = 4.,
              rebin  = 1,
              log    = False,
              )

leadsspair_mTtot = Var(name = 'leadsspair_mTtot',
              path   = 'pairs',
              xmin   = 0.,
              xmax   = 2000.,
              rebin  = 20,
              log    = False,
              )

leadsspair_mVis = Var(name = 'leadsspair_mVis',
              path   = 'pairs',
              xmin   = 0.,
              xmax   = 2000.,
              rebin  = 20,
              log    = False,
              )

leadsspair_ID = Var(name = 'leadsspair_ID',
              path   = 'pairs',
              rebin  = 1,
              anbins = [ lep[0]+lep[1] for lep in combinations_with_replacement(['El','Mu','Tau'],2)],
              log    = False,
              )


vars_list = []
vars_list.append(leadsspair_pt)
vars_list.append(leadsspair_eta)
vars_list.append(leadsspair_phi)
vars_list.append(leadsspair_DR)
vars_list.append(leadsspair_charge)
vars_list.append(leadsspair_mTtot)
vars_list.append(leadsspair_mVis)
vars_list.append(leadsspair_ID)


vars_dict = {}
for var in vars_list: vars_dict[var.name] = var.__dict__


## EOF


