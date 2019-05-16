#!/bin/bash

python SubmitGet_v3.py -c "15_period" -s "Data"
python SubmitGet_v3.py -c "16_period" -s "Data"
python SubmitGet_v3.py -c "17_period" -s "Data"

#python SubmitGet_v3.py -c "MC16a_fast" -s "DCH"
#python SubmitGet_v3.py -c "MC16d_fast" -s "DCH"
#python SubmitGet_v3.py -c "MC16e_fast" -s "DCH"

<<COMMENT
python SubmitGet_v3.py -c "MC16a" -s "Wjets"
python SubmitGet_v3.py -c "MC16d" -s "Wjets"
python SubmitGet_v3.py -c "MC16e" -s "Wjets"

python SubmitGet_v3.py -c "MC16a" -s "dijet"
python SubmitGet_v3.py -c "MC16d" -s "dijet"
python SubmitGet_v3.py -c "MC16e" -s "dijet"

python SubmitGet_v3.py -c "MC16a" -s "top_inclusive"
python SubmitGet_v3.py -c "MC16d" -s "top_inclusive"
python SubmitGet_v3.py -c "MC16e" -s "top_inclusive"
COMMENT

<<COMMENT
python SubmitGet_v3.py -c "MC16a" -s "Zjets"
python SubmitGet_v3.py -c "MC16d" -s "Zjets"
python SubmitGet_v3.py -c "MC16e" -s "Zjets"

python SubmitGet_v3.py -c "MC16a" -s "Zjets_light"
python SubmitGet_v3.py -c "MC16d" -s "Zjets_light"
python SubmitGet_v3.py -c "MC16e" -s "Zjets_light"


python SubmitGet_v3.py -c "MC16a" -s "diboson"
python SubmitGet_v3.py -c "MC16d" -s "diboson"
python SubmitGet_v3.py -c "MC16e" -s "diboson"

python SubmitGet_v3.py -c "MC16a" -s "top"
python SubmitGet_v3.py -c "MC16d" -s "top"
python SubmitGet_v3.py -c "MC16e" -s "top"

python SubmitGet_v3.py -c "MC16a" -s "raretop"
python SubmitGet_v3.py -c "MC16d" -s "raretop"
python SubmitGet_v3.py -c "MC16e" -s "raretop"

python SubmitGet_v3.py -c "MC16a" -s "multiboson"
python SubmitGet_v3.py -c "MC16d" -s "multiboson"
python SubmitGet_v3.py -c "MC16e" -s "multiboson"
COMMENT
