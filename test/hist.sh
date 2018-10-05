#!/bin/bash

#INPATH="/coepp/cephfs/share/atlas/MLA/SUSY11Data.v1/merged/nominal"
INPATH="/coepp/cephfs/share/atlas/MLA/SUSY11MC.v1/merged/nominal"
#INPATH="/coepp/cephfs/share/atlas/MLA/SUSY3MC.v1/merged/nominal"
#INPATH="/coepp/cephfs/share/atlas/MLA/SUSY3Data.v1/merged/nominal"

#INPATH="/coepp/cephfs/share/atlas/MLA/EXOT22Data.v1/merged/nominal"
#INPATH="/coepp/cephfs/share/atlas/MLA/EXOT22MC.v1/merged/nominal"

INSCRIPT="../ssdilep/run"

SCRIPT="j.plotter_FF_OneTau.py"
#SCRIPT="j.plotter_FF_OneMu.py"
#SCRIPT="j.plotter_VR_OneMuPair.py"
#SCRIPT="j.plotter_CF_MuTau.py"
#SCRIPT="j.plotter_VR_MuTau.py"
#SCRIPT="j.plotter_TEST.py"

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/data15_13TeV_periodD.root --sampletype="data" --samplename="data15_13TeV_periodD"  --minentry=0 --maxentry=10000  #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/data17_13TeV_periodK.root --sampletype="data" --samplename="data17_13TeV_periodK"  --minentry=0 --maxentry=10000  #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/PhPy8EG_A14_ttbar_hdamp258p75_dil.root --sampletype="mc" --samplename="PhPy8EG_A14_ttbar_hdamp258p75_dil" --minentry=0 --maxentry=100000   #--config="sys:FF_DN" 
python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CVetoBVeto.root --sampletype="mc" --samplename="Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CVetoBVeto" --minentry=0 --maxentry=100000   #--config="sys:FF_DN" 

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ6W.root --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ6W" --minentry=0 --maxentry=200000   #--config="sys:FF_DN" 


#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CVetoBVeto.root --sampletype="mc" --samplename="Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CVetoBVeto" --minentry=0 --maxentry=1000000   #--config="sys:FF_DN" 


# EOF
