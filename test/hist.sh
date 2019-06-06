#!/bin/bash

#INPATH="/coepp/cephfs/share/atlas/MLA/SUSY11Data.v3/group/nominal"
#INPATH="/coepp/cephfs/share/atlas/MLA/SUSY11MC.v3/group/nominal"

#INPATH="/coepp/cephfs/share/atlas/MLA/SUSY11Data.v2/merged/nominal"
#INPATH="/coepp/cephfs/share/atlas/MLA/SUSY11MC.v3/merged/nominal"

#INPATH="/coepp/cephfs/share/atlas/MLA/SUSY3MC.v3/merged/nominal"
#INPATH="/coepp/cephfs/share/atlas/MLA/SUSY3Data.v3/group/nominal"
INPATH="/coepp/cephfs/share/atlas/MLA/SUSY3MC.v3/group/nominal"
#INPATH="/coepp/cephfs/share/atlas/MLA/SUSY3DCH.v1/merged/nominal"

#INPATH="/coepp/cephfs/share/atlas/MLA/EXOT22Data.v1/merged/nominal"
#INPATH="/coepp/cephfs/share/atlas/MLA/EXOT22MC.v1/merged/nominal"

INSCRIPT="../ssdilep/run"

# ---------------------------
# migrated to read v3 ntuples
# ---------------------------
#SCRIPT="j.plotter_FF_OneTau.py"
#SCRIPT="j.plotter_SR_OnePair.py"
#SCRIPT="j.plotter_VR_OnePair.py"
#SCRIPT="j.plotter_CF_MuTau.py"
SCRIPT="j.plotter_FF_MultiLeptons.py"

#SCRIPT="j.plotter_SIG_OnePair.py"
#SCRIPT="j.plotter_SIG_TwoPairs.py"
#SCRIPT="j.plotter_SR_TwoPairs.py"
#SCRIPT="j.plotter_TEST.py"

# ---------------------------
# ---------------------------

#SCRIPT="j.plotter_QG_OneTau.py"
#SCRIPT="j.plotter_FF_OneMu.py"
#SCRIPT="j.plotter_VR_OneMuPair.py"
#SCRIPT="j.plotter_VR_MuTau.py"

# ---------------------------
# ---------------------------

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/data.root --sampletype="data" --samplename="data"  --minentry=0 --maxentry=200000  #--config="sys:FF_DN" 

python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Wtaunu.root --sampletype="mc" --samplename="Wtaunu" --minentry=0 --maxentry=200000   #--config="sys:FF_DN" 

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/data15_13TeV_periodD.root --sampletype="data" --samplename="data15_13TeV_periodD"  --minentry=0 --maxentry=10000  #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/data17_13TeV_periodK.root --sampletype="data" --samplename="data17_13TeV_periodK"  --minentry=0 --maxentry=5000  #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00300345.root --sampletype="data" --samplename="physics_Main_00300345"  --minentry=0 --maxentry=5000  #--config="sys:FF_DN" 

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/PhPy8EG_A14_ttbar_hdamp258p75_dil.root --sampletype="mc" --samplename="PhPy8EG_A14_ttbar_hdamp258p75_dil" --minentry=0 --maxentry=100000   #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CVetoBVeto.root --sampletype="mc" --samplename="Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CVetoBVeto" --minentry=0 --maxentry=40000   #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ12WithSW.root --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ12WithSW" --minentry=0 --maxentry=5   #--config="sys:FF_DN" 


#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH300.root --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH300" --minentry=0 --maxentry=10000
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH400.root --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH400" --minentry=0 --maxentry=100000
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH500.root --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH500" --minentry=0 --maxentry=100000
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH600.root --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH600" --minentry=0 --maxentry=100000
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH700.root --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH700" --minentry=0 --maxentry=100000
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH800.root --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH800" --minentry=0 --maxentry=100000
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH900.root --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH900" --minentry=0 --maxentry=100000
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH1000.root --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH1000" --minentry=0 --maxentry=100000
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH1100.root --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH1100" --minentry=0 --maxentry=100000
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH1200.root --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH1200" --minentry=0 --maxentry=100000
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH1300.root --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH1300" --minentry=0 --maxentry=100000


#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CVetoBVeto.root --sampletype="mc" --samplename="Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CVetoBVeto" --minentry=0 --maxentry=1000000   #--config="sys:FF_DN" 


# EOF
