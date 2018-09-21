#!bin/bash

# ------------
# FAKE FACTORS
# ------------

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_F1" --lab="numerator" --tag="3prong" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFF3PTau15Jun" --output="./" --makeplot=True --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_F1" --lab="denominator" --tag="3prong" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFF3PTau15Jun" --output="./" --makeplot=True --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F2" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F2" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F3" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F3" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F4" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F4" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F5" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F5" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F6" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F6" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F7" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F7" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_NUM_F8" --lab="numerator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="mulead_pt" --reg="FAKES_DEN_F8" --lab="denominator" --tag="ltt" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFltt" --output="./" --makeplot=False --fakest="Subtraction"


# ----------
# VALIDATION
# ----------

python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="OSZ_MAINREG" --lab="VR" --tag="val" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistVROneTauPair" --output="./" --makeplot=True --fakest="LeadLepRegions"



