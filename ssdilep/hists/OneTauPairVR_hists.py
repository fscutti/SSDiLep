from histconfig import *


hist_list = []


# -------
# event
# -------

hist_list.append(h_ditau_ptratio)
hist_list.append(h_ditau_scdphi)
hist_list.append(h_taus_mVis)
hist_list.append(h_taus_mTtot)
hist_list.append(h_ntaus)


# -------
# taus
# -------

# taulead
hist_list.append(h_taulead_pt)
hist_list.append(h_taulead_eta)
hist_list.append(h_taulead_phi)
hist_list.append(h_taulead_JetBDTScore)
hist_list.append(h_taulead_JetBDTScoreSigTrans)

# tausublead
hist_list.append(h_tausublead_pt)
hist_list.append(h_tausublead_eta)
hist_list.append(h_tausublead_phi)
hist_list.append(h_tausublead_JetBDTScore)
hist_list.append(h_tausublead_JetBDTScoreSigTrans)

# -------
# MET
# -------
hist_list.append(h_met_trk_et)


# EOF
