#!bin/bash

# ------------
# FAKE FACTORS
# ------------

#python ../ssdilep/scripts/merge.py --var="jetlead_pt" --reg="FAKES_NUM_F1" --lab="numerator" --tag="1pthr" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFMatchLumiPresc" --output="./" --makeplot=True --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="jetlead_pt" --reg="FAKES_DEN_F1" --lab="denominator" --tag="1pthr" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFMatchLumiPresc" --output="./" --makeplot=True --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="trigJetlead_pt" --reg="FAKES_NUM_F1" --lab="numerator" --tag="1pthr" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFMatchLumiPresc" --output="./" --makeplot=True --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="trigJetlead_pt" --reg="FAKES_DEN_F1" --lab="denominator" --tag="1pthr" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFMatchLumiPresc" --output="./" --makeplot=True --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="taulead_PartonTruthLabelID" --reg="FAKES_NUM_1PMedium_All_F1" --lab="numerator" --tag="hp" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFF24Feb" --output="./" --makeplot=False --fakest="NoFakes"


#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_1PMedium_All_F10" --lab="numerator" --tag="hp" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFF2Jun" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_1PMedium_All_F10" --lab="denominator" --tag="hp" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFF2Jun" --output="./" --makeplot=True --fakest="NoFakes"

python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_3PMedium_All_F10" --lab="numerator" --tag="hp" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFF2Jun" --output="./" --makeplot=True --fakest="NoFakes"
python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_3PMedium_All_F10" --lab="denominator" --tag="hp" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFF2Jun" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_3PMedium_All_F1" --lab="numerator" --tag="hp" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFgroupV5" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_3PMedium_All_F1" --lab="denominator" --tag="hp" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFgroupV5" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_1PMedium_All_F10" --lab="numerator" --tag="hp" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFgroupV5" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_1PMedium_All_F10" --lab="denominator" --tag="hp" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFgroupV5" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_3PMedium_All_F10" --lab="numerator" --tag="hp" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFgroupV5" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_3PMedium_All_F10" --lab="denominator" --tag="hp" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFgroupV5" --output="./" --makeplot=True --fakest="NoFakes"


#python ../ssdilep/scripts/merge.py --var="taulead_PartonTruthLabelID" --reg="FAKES_NUM_1PMedium_All_F1" --lab="numerator" --tag="hp" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFgroupV5" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_PartonTruthLabelID" --reg="FAKES_DEN_1PMedium_All_F1" --lab="numerator" --tag="hp" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFgroupV5" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_PartonTruthLabelID" --reg="FAKES_NUM_3PMedium_All_F1" --lab="numerator" --tag="hp" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFgroupV5" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_PartonTruthLabelID" --reg="FAKES_DEN_3PMedium_All_F1" --lab="numerator" --tag="hp" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFgroupV5" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="taulead_PartonTruthLabelID" --reg="FAKES_NUM_1PMedium_All_F10" --lab="numerator" --tag="hp" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFgroupV5" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_PartonTruthLabelID" --reg="FAKES_DEN_1PMedium_All_F10" --lab="numerator" --tag="hp" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFgroupV5" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_PartonTruthLabelID" --reg="FAKES_NUM_3PMedium_All_F10" --lab="numerator" --tag="hp" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFgroupV5" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_PartonTruthLabelID" --reg="FAKES_DEN_3PMedium_All_F10" --lab="numerator" --tag="hp" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFgroupV5" --output="./" --makeplot=True --fakest="NoFakes"






#python ../ssdilep/scripts/merge.py --var="taulead_truthOrigin" --reg="FAKES_NUM_1PMedium_All_F1" --lab="numerator" --tag="hp" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFF27Feb" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_1PMedium_All_F1" --lab="numerator" --tag="hp" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFF24Feb" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_1PMedium_All_F1" --lab="denominator" --tag="hp" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFDBHarmonPtBins" --output="./" --makeplot=True --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="taulead_seedjetwidth" --reg="FAKES_GDEN_1PMedium_All_F1" --lab="denominator" --tag="hp" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFHarmonPtBins" --output="./" --makeplot=False --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_3PMedium_All_F1" --lab="numerator" --tag="hp" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFHarmonPtBins" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_3PMedium_All_F1" --lab="denominator" --tag="hp" --icut="5" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFHarmonPtBins" --output="./" --makeplot=False --fakest="Subtraction"



#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_F2" --lab="numerator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_F2" --lab="denominator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_F3" --lab="numerator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_F3" --lab="denominator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_F4" --lab="numerator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_F4" --lab="denominator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_F5" --lab="numerator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_F5" --lab="denominator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_F6" --lab="numerator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_F6" --lab="denominator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_F7" --lab="numerator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_F7" --lab="denominator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_F8" --lab="numerator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_F8" --lab="denominator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_F9" --lab="numerator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_DEN_F9" --lab="denominator" --tag="lp" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/Hist1PFFLumiPresc" --output="./" --makeplot=False --fakest="Subtraction"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FAKES_NUM_1PLoose_F10" --lab="numerator" --tag="test" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFTracksR2" --output="./" --makeplot=True --fakest="Subtraction"

# ----------
# VALIDATION
# ----------
#python ../ssdilep/scripts/merge.py --var="leadsspair_mVis" --reg="1DF2L_invANTIPairPt150_ValRegionFiltered" --lab="1DF2L_invANTIPairPt150_ValRegionFiltered" --tag="1df2l_vrfiltered" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistVROnePairNewFF" --output="./" --makeplot=True --fakest="AllRegions"


#python ../ssdilep/scripts/merge.py --var="sspairs_mTtot" --reg="2SF4L_SideBandFiltered" --lab="2SF4L_SideBandFiltered" --tag="2sf4l_filter" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistSRTwoPairsLumi" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="sspairs_mTtot" --reg="2SF4L_SideBandNonFiltered" --lab="2SF4L_SideBandNonFiltered" --tag="2sf4l_nofilter" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistSRTwoPairsLumi" --output="./" --makeplot=True --fakest="NoFakes"


#python ../ssdilep/scripts/merge.py --var="leadsspair_mTtot" --reg="1SF2L_SideBandFiltered" --lab="1SF2L_SideBandFiltered" --tag="1sf2l_filter" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistSROnePairLumi" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="1SF3L_SideBandNonFiltered" --lab="1SF3L_SideBandNonFiltered" --tag="1sf3l_nofilter" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistSROnePairFullc" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="1SF2L_SideBandNonFiltered" --lab="1SF2L_SideBandNonFiltered" --tag="1sf2l_nofilter" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistSROnePairFullc" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="leadsspair_mVis" --reg="1SF3L_SideBandNonFiltered" --lab="1SF3L_SideBandNonFiltered" --tag="1sf3l_nofilter" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistSROnePairFullc" --output="./" --makeplot=True --fakest="NoFakes"


#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FullSSZfil" --lab="SSZ_truth" --tag="ssztruth" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFFilStudy" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FullSSZ" --lab="SSZ_incl" --tag="sszincl" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFStudy" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FullOSZfil" --lab="OSZ_truth" --tag="osztruth" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFFilStudy" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FullOSZ" --lab="OSZ_incl" --tag="oszincl" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFStudy" --output="./" --makeplot=True --fakest="NoFakes"


#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="SSTTBARfil" --lab="SSTTBAR_truth" --tag="ssttbartruth" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFFilStudy" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="SSTTBAR" --lab="SSTTBAR_incl" --tag="ssttbarincl" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFStudy" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="OSTTBARfil" --lab="OSTTBAR_truth" --tag="osttbartruth" --icut="4" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFFilStudy" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="OSTTBAR" --lab="OSTTBAR_incl" --tag="osttbarincl" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFStudy" --output="./" --makeplot=True --fakest="NoFakes"


#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FullSSTTBAR_nofil" --lab="FullSSTTBAR_incl" --tag="fullssttbarincl" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCF3May" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FullSSTTBAR" --lab="FullSSTTBAR_incl" --tag="fullssttbarincl" --icut="1" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFStudy" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="FullOSTTBARfil" --lab="FullOSTTBAR_truth" --tag="fullosttbartruth" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFFilStudy" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="leadsspair_mVis" --reg="1DF3L" --lab="1DF3L" --tag="1DF3L" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistSROnePair" --output="./" --makeplot=True --fakest="NoFakes"


#python ../ssdilep/scripts/merge.py --var="cutflow_presel" --lab="cutflow_preselection" --tag="cfpresel" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFFilStudy" --output="./" --makeplot=False --fakest="NoFakes"



#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="BASELINEfil" --lab="BASELINE_truth" --tag="baseline" --icut="1" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFFilStudy" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="BASELINE" --lab="BASELINE_incl" --tag="baseline" --icut="0" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFFilStudy" --output="./" --makeplot=True --fakest="NoFakes"


#python ../ssdilep/scripts/merge.py --var="taulead_pt" --reg="DJ_MAINREG" --lab="VR" --tag="valiso" --icut="1" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistMuTauVRIsoTrig" --output="./" --makeplot=True --fakest="LeadLepRegions"

#python ../ssdilep/scripts/merge.py --var="mutau_mVis" --reg="OSZ" --lab="OSZ" --tag="osz" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFStudy" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="mutau_mVis" --reg="FullSSZfil" --lab="FullSSZfil" --tag="fullsszfil" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFFilStudy" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="mutau_mVis" --reg="FullOSZ" --lab="FullOSZ" --tag="fullosz" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFStudy" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="mutau_mVis" --reg="FullSSZ" --lab="FullSSZ" --tag="fullssz" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFStudy" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="mutau_mVis" --reg="OSTTBAR" --lab="OSTTBAR" --tag="osttbar" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFStudy" --output="./" --makeplot=True --fakest="NoFakes"
#python ../ssdilep/scripts/merge.py --var="mutau_mVis" --reg="SSTTBAR" --lab="SSTTBAR" --tag="ssttbar" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFStudy" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="mutau_mVis" --reg="FullOSTTBAR" --lab="FullOSTTBAR" --tag="fullosttbar" --icut="1" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFStudy" --output="./" --makeplot=True --fakest="NoFakes"
##python ../ssdilep/scripts/merge.py --var="mutau_mVis" --reg="FullSSTTBAR" --lab="FullSSTTBAR" --tag="fullssttbar" --icut="1" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFStudy" --output="./" --makeplot=True --fakest="NoFakes"

#python ../ssdilep/scripts/merge.py --var="mutau_mVis" --reg="BASELINEfil" --lab="BASELINE" --tag="baseline" --icut="1" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistCFFilStudy" --output="./" --makeplot=True --fakest="Simulation"


# ---------------
# OVERLAY STUDIES
# ---------------

#python ../ssdilep/scripts/merge.py --var="taulead_seedjetjvt" --reg="FAKES_UDEN_1PMedium_All_F1" --ovreg="FAKES_UDEN_1PMedium_All_F1:6;FAKES_QDEN_1PMedium_All_F1:6;FAKES_GDEN_1PMedium_All_F1:6" --lab="denominator" --tag="hp" --icut="6" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFHarmonPtBins" --output="./" --renorm=True --makeplot=False --makeoverlay=True --fakest="NoFakes"



#python ../ssdilep/scripts/merge.py --var=taulead_PartonTruthLabelID --reg=FAKES_DEN_3PMedium_90150_F1 --ovreg="FAKES_DEN_3PMedium_90150_F1:5;FAKES_DEN_3PMedium_90150_F10:4" --lab=den_3PMedium_90150 --tag=shapes --icut="FAKES_DEN_3PMedium_90150_F1:6;FAKES_DEN_3PMedium_90150_F10:5" --makeplot=False --makeoverlay=True --renorm=True --fakest=NoFakes --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFF24Feb" --output="./"




#python ../ssdilep/scripts/merge.py --var="jetlead_pt" --reg="FAKES_QUARKS_F1" --lab="test" --tag="incl" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistQGTauTracksIsClCharged" --output="./" --makeplot=True --fakest="Subtraction" --renorm=False
#python ../ssdilep/scripts/merge.py --var="jetlead_pt" --reg="FAKES_GLUONS_F1" --lab="test" --tag="incl" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistQGTauTracksIsClCharged" --output="./" --makeplot=True --fakest="Subtraction" --renorm=False
#python ../ssdilep/scripts/merge.py --var="jetlead_pt" --reg="FAKES_UNKNOWN_F1" --lab="test" --tag="incl" --icut="3" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistQGTauTracksIsClCharged" --output="./" --makeplot=True --fakest="Subtraction" --renorm=False



#python ../ssdilep/scripts/merge.py --var="taulead_jetwidth" --reg="FAKES_NOFILTER_F1" --lab="test" --tag="nofilter" --icut="2" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistFFComposition" --output="./" --makeplot=False --fakest="NoFakes" --renorm=False





#python ../ssdilep/scripts/merge.py --var=taulead_pt --reg=BASELINE --ovreg=BASELINE:0 --lab=ETT_1SSPair_al4Tau --tag=shapes --icut=BASELINE:0 --makeplot=False --makeoverlay=True --renorm=False --fakest=NoFakes --input=/coepp/cephfs/mel/fscutti/ssdilep/HistBASEOnePair --output="./"

#python ../ssdilep/scripts/merge.py --var="leadsspair_ID" --reg="BASELINE" --ovreg="BASELINE:0;STT_al1TAU_BDTLoose_eBDTLoose:3;STT_al1TAU_BDTMedium_eBDTMedium:3;STT_al1TAU_BDTTight_eBDTTight:3" --lab="STT" --tag="mH700" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistBASEOnePair" --output="./" --makeoverlay=True  --renorm=False

#python ../ssdilep/scripts/merge.py --var="sspairs_pt" --reg="BASELINE" --ovreg="BASELINE:0;STT_1TAU_BDTLoose_eBDTLoose:3;STT_1TAU_BDTMedium_eBDTMedium:3" --lab="TEST" --tag="mH400" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistACCTwoPairs" --output="./" --makeoverlay=True  --renorm=False

#python ../ssdilep/scripts/merge.py --var="sspairs_pt" --reg="STT_al1TAU_BDTLoose_eBDTLoose" --ovreg="STT_al1TAU_BDTLoose_eBDTLoose:3" --lab="TEST" --tag="manySamp" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistBASETwoPairs" --output="./" --renorm=True --makeoverlay=True
#python ../ssdilep/scripts/merge.py --var="leadsspair_pt" --reg="BASELINE" --ovreg="BASELINE:0" --lab="TEST" --tag="manySamp" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistBASEOnePair" --output="./" --makeplot=False --makeoverlay=False  --renorm=False


#python ../ssdilep/scripts/merge.py --var="leadsspair_pt" --reg="BASELINE" --lab="TEST" --tag="manySamp" --icut="0" --input="/coepp/cephfs/mel/fscutti/ssdilep/HistBASEOnePair" --output="./" --makeplot=False --makeoverlay=False  --renorm=False






