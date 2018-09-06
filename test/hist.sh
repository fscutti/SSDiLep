#!/bin/bash

## Batch

#INPATH="/coepp/cephfs/mel/fscutti/ssdilep/EXOT12_common_v1Ntuples/merged/nominal"
#INPATH="/coepp/cephfs/mel/fscutti/ssdilep/EXOT12_common_v2Ntuples/nominal"
#INPATH="/coepp/cephfs/mel/fscutti/ssdilep/EXOT12_common_v3Ntuples/merged/nominal"

#INPATH="/coepp/cephfs/mel/fscutti/ssdilep/HIGG3D3_v7/merged/nominal"
#INPATH="/coepp/cephfs/mel/fscutti/ssdilep/HIGG3D3_v8/merged/nominal"
#INPATH="/coepp/cephfs/mel/fscutti/ssdilep/nHIGG3D3_v9/merged/nominal"
#INPATH="/coepp/cephfs/mel/fscutti/ssdilep/HIGG3D3_v11/merged/nominal"
#INPATH="/coepp/cephfs/mel/fscutti/ssdilep/HIGG3D3_v12/merged/nominal"


#INPATH="/coepp/cephfs/share/atlas/SSDiLep/SUSY11Data.v4.r2/merged/nominal"

#INPATH="/coepp/cephfs/share/atlas/Tau/SUSY11MC.v1.r10210.r2/merged/nominal"
#INPATH="/coepp/cephfs/share/atlas/Tau/SUSY11Data.v1.r2/merged/nominal"

#INPATH="/coepp/cephfs/share/atlas/MLA/SUSY11Data.v1/merged/nominal"
INPATH="/coepp/cephfs/share/atlas/MLA/SUSY3MC.v1/merged/nominal"

# EXOT22 v3
#INPATH="/coepp/cephfs/share/atlas/SSDiLep/EXOT22Data.v3/merged/nominal"
#INPATH="/coepp/cephfs/share/atlas/SSDiLep/EXOT22MC.v3/merged/nominal"


# EXOT22 v1
#INPATH="/coepp/cephfs/share/atlas/SSDiLep/EXOT22Data.v1a.r1/merged/nominal"
#INPATH="/coepp/cephfs/share/atlas/SSDiLep/EXOT22MC.v1a/merged/nominal"

#INPATH="/data/fscutti/ORstudy/ORtest"


INSCRIPT="../ssdilep/run"

#SCRIPT="j.plotter_MuVal.py"
#SCRIPT="j.plotter_MuFF.py"
#SCRIPT="j.plotter_FF.py"

SCRIPT="j.plotter_VR_OneTauPair.py"

#SCRIPT="j.plotter_TwoTauFF.py"
#SCRIPT="j.plotter_OneTauFF.py"
#SCRIPT="j.plotter_TEST.py"
#SCRIPT="j.plotter_VR_OneMuPair.py"
#SCRIPT="j.plotter_TAndP.py"


#SCRIPT="j.plotter_VR1.py"
#SCRIPT="j.plotter_VR2.py"
#SCRIPT="j.plotter_VR3.py"
#SCRIPT="j.plotter_VR4.py"
#SCRIPT="j.plotter_VR5.py"

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/data16_13TeV_periodG.root --sampletype="data" --samplename="data16_13TeV_periodG"  --minentry=0 --maxentry=200000  #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/data15_13TeV_periodD.root --sampletype="data" --samplename="data15_13TeV_periodD"  --minentry=0 --maxentry=200000  #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/PhPy8EG_A14_ttbar_hdamp258p75_dil.root --sampletype="mc" --samplename="PhPy8EG_A14_ttbar_hdamp258p75_dil" --minentry=0 --maxentry=100000   #--config="sys:FF_DN" 

python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CFilterBVeto.root --sampletype="mc" --samplename="Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CFilterBVeto" --minentry=0 --maxentry=100000   #--config="sys:FF_DN" 



#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CFilterBVeto.root --sampletype="mc" --samplename="Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CFilterBVeto" --minentry=0 --maxentry=10000   #--config="sys:FF_DN" 

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_BFilter.root --sampletype="mc" --samplename="Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_BFilter" --minentry=0 --maxentry=10000

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CFilterBVeto.root --sampletype="mc" --samplename="Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CFilterBVeto_slice4" --minentry=800001 --maxentry=1000000  #--config="sys:FF_DN" 


#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_222_NNPDF30NNLO_llll.root --sampletype="mc" --samplename="Sherpa_222_NNPDF30NNLO_llll_slice2" --minentry=400001 --maxentry=600000 #--config="sys:FF_DN" 

##../ssdilep/run/j.plotter_MuFF.py --input /coepp/cephfs/share/atlas/SSDiLep/EXOT22MC.v2/merged/nominal/PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.root --samplename PhPy8EG_A14_ttbar_hdamp258p75_nonallhad_slice49 --sampletype mc --minentry 19600001 --maxentry 20000000 

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00280273.root --sampletype="data"  #--events=20000
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00302393.root --sampletype="data"  --events=20000

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00282992.root --sampletype="data" --events=20000 #--config="sys:FF_DN"
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00304008.root --sampletype="data" --samplename="physics_Main_00304008" --events=50000 #--config="sys:FF_DN" # example of triglist probs


#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CFilterBVeto.root --sampletype="mc" --samplename="Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CFilterBVeto_WithTriggerMatching" #--events=20000   #--config="sys:FF_DN" 

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00298690.root  --samplename="physics_Main_00298690_WithTriggerMatching" --sampletype="data" #--events=2000 #--config="sys:FF_DN" # example of triglist probs


#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00282631.root  --samplename="physics_Main_00282631" --sampletype="data" --events=2000 #--config="sys:FF_DN" # example of triglist probs
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_BFilter.root --sampletype="mc" --samplename="Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_BFilter" --events=20000   #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_NNPDF30NNLO_Zmumu_Pt0_70_BFilter.root  --sampletype="mc" --events=4000   #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_CT10_VV_muvmuv_2000M3000.root  --sampletype="mc" --events=20000   #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_CT10_llvv.root  --sampletype="mc" --events=20000   #--config="sys:FF_DN" 

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_221_NNPDF30NNLO_llll.root  --samplename="Sherpa_221_NNPDF30NNLO_llll" --sampletype="mc" --events=10000   #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ0W.root  --sampletype="mc" #--events=4000   #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.root --samplename="PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad" --sampletype="mc" --events=20000   #--config="sys:FF_DN" 

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/DCH300.root  --sampletype="mc" --samplename="DCH300_HRMpMp_HRMmMm" --events=10000   #--config="sys:FF_DN" 


#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00304008_BTagOR.root --samplename="physics_Main_00304008_BTagOR" --sampletype="data" > physics_Main_00304008_BTagOR.log 2>&1
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00304008_NewOR.root --samplename="physics_Main_00304008_NewOR" --sampletype="data" > physics_Main_00304008_NewOR.log 2>&1
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00304008_OldOR.root --samplename="physics_Main_00304008_OldOR" --sampletype="data" > physics_Main_00304008_OldOR.log 2>&1


#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00298633.root --sampletype="data" --samplename="physics_Main_00298633" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00300655.root --sampletype="data" --samplename="physics_Main_00300655" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00300687.root --sampletype="data" --samplename="physics_Main_00300687" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00307306.root --sampletype="data" --samplename="physics_Main_00307306" 


#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00279867.root --sampletype="data" --samplename="physics_Main_00279867" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00279515.root --sampletype="data" --samplename="physics_Main_00279515" 



