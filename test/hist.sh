#!/bin/bash

INPATH="/coepp/cephfs/share/atlas/MLA/SUSY11Data.v1/merged/nominal"
#INPATH="/coepp/cephfs/share/atlas/MLA/SUSY11MC.v1/merged/nominal"
#INPATH="/coepp/cephfs/share/atlas/MLA/SUSY3MC.v1/merged/nominal"
#INPATH="/coepp/cephfs/share/atlas/MLA/SUSY3Data.v1/merged/nominal"

INSCRIPT="../ssdilep/run"

SCRIPT="j.plotter_FF_OneTau.py"
#SCRIPT="j.plotter_VR_OneMuPair.py"

python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/data16_13TeV_periodG.root --sampletype="data" --samplename="data16_13TeV_periodG"  --minentry=0 --maxentry=200000  #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/PhPy8EG_A14_ttbar_hdamp258p75_dil.root --sampletype="mc" --samplename="PhPy8EG_A14_ttbar_hdamp258p75_dil" --minentry=0 --maxentry=100000   #--config="sys:FF_DN" 




# EOF
