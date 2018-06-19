from histconfig import *


hist_list = []


# -------
# event
# -------
hist_list.append(h_averageIntPerXing)
hist_list.append(h_njets)

hist_list.append(h_tausubleadlead_ptratio)


# -------
# jets
# -------

# jetlead
hist_list.append(h_jetlead_pt)
hist_list.append(h_jetlead_eta)
hist_list.append(h_jetlead_phi)

# -------
# taus
# -------

# taulead
hist_list.append(h_taulead_pt)
hist_list.append(h_taulead_eta)
hist_list.append(h_taulead_phi)


# tausublead
hist_list.append(h_tausublead_pt)
hist_list.append(h_tausublead_eta)
hist_list.append(h_tausublead_phi)


# -------
# MET
# -------
hist_list.append(h_met_trk_et)


# EOF






