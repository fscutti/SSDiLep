from histconfig import *


hist_list = []


# -------
# event
# -------
hist_list.append(h_nmuons)
hist_list.append(h_njets)
hist_list.append(h_ntaus)
hist_list.append(h_mutau_mVis)
hist_list.append(h_mutau_mTtot)


# -------
# muons
# -------

# mulead
hist_list.append(h_mulead_pt)
hist_list.append(h_mulead_eta)
hist_list.append(h_mulead_phi)
hist_list.append(h_mulead_trkd0)
hist_list.append(h_mulead_trkd0sig)
hist_list.append(h_mulead_trkz0)
hist_list.append(h_mulead_trkz0sintheta)


# -------
# taus
# -------
hist_list.append(h_taulead_pt)
hist_list.append(h_taulead_eta)
hist_list.append(h_taulead_phi)
hist_list.append(h_taulead_JetBDTScore)
hist_list.append(h_taulead_JetBDTScoreSigTrans)

# -------
# MET
# -------
hist_list.append(h_met_trk_et)
