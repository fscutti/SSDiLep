#!/usr/bin/python

import os
import subprocess
import time
from ssdilep import plots

def make_tag(cat,var):
  return '_'.join([cat,var])

#---------------------
# Set environment
#---------------------
# Environment variables defined in batchsetup.sh

ana      = 'ssdilep'

indir    = 'HistFF1PTESTMatch'
outdir   = 'PlotsFF1PTESTMatch'

USER    = os.getenv('USER')
MAIN    = os.getenv('MAIN')

inpath  = os.path.join("/coepp/cephfs/mel",USER,ana)
INDIR   = os.path.join(inpath,indir)  
OUTDIR  = os.path.join(inpath,outdir)

if not os.path.isdir(OUTDIR): os.makedirs(OUTDIR)
if not os.path.isdir(OUTDIR+"/"+"log"): os.makedirs(OUTDIR+"/"+"log")

#---------------------
# Batch jobs options
#---------------------
AUTOBUILD = True
QUEUE     = 'long'
BEXEC     = 'Plots.sh'
JOBDIR    = "/coepp/cephfs/mel/%s/jobdir" % USER

#---------------------
# Batch jobs variables
#---------------------
INTARBALL = os.path.join(JOBDIR,'plotstarball_%s.tar.gz' % (time.strftime("d%d_m%m_y%Y_H%H_M%M_S%S")) )
SCRIPT    = os.path.join("./",ana,"scripts",'merge.py')

job_vars={}
job_vars['INTARBALL'] = INTARBALL
job_vars['OUTDIR']    = OUTDIR
job_vars['INDIR']     = INDIR
job_vars['SCRIPT']    = SCRIPT

#fake_estimate = "AllRegions"
fake_estimate = "Subtraction"

regions = {}
# use it as such:
#regions["FOLDERNAME"]     = [icut, "plot label"]

"""
#regions["OSZ_TT"] = [7, "OSZ_TT",   "oszFilter"]
regions["OSZ_LT"] = [7, "OSZ_LT",   "oszFilter"]
regions["OSZ_TL"] = [7, "OSZ_TL",   "oszFilter"]
regions["OSZ_LL"] = [7, "OSZ_LL",   "oszFilter"]

#regions["OSW_TT"] = [7, "OSW_TT",   "oswFilter"]
regions["OSW_LT"] = [7, "OSW_LT",   "oswFilter"]
regions["OSW_TL"] = [7, "OSW_TL",   "oswFilter"]
regions["OSW_LL"] = [7, "OSW_LL",   "oswFilter"]

#regions["OSTop_TT"] = [7, "OSTop_TT",   "ostopFilter"]
regions["OSTop_LT"] = [7, "OSTop_LT",   "ostopFilter"]
regions["OSTop_TL"] = [7, "OSTop_TL",   "ostopFilter"]
regions["OSTop_LL"] = [7, "OSTop_LL",   "ostopFilter"]

#regions["OSSig_TT"] = [7, "OSSig_TT",   "ossigFilter"]
regions["OSSig_LT"] = [7, "OSSig_LT",   "ossigFilter"]
regions["OSSig_TL"] = [7, "OSSig_TL",   "ossigFilter"]
regions["OSSig_LL"] = [7, "OSSig_LL",   "ossigFilter"]


#regions["SSZ_TT"] = [7, "SSZ_TT",   "sszFilter"]
regions["SSZ_LT"] = [7, "SSZ_LT",   "sszFilter"]
regions["SSZ_TL"] = [7, "SSZ_TL",   "sszFilter"]
regions["SSZ_LL"] = [7, "SSZ_LL",   "sszFilter"]

#regions["SSW_TT"] = [7, "SSW_TT",   "sswFilter"]
regions["SSW_LT"] = [7, "SSW_LT",   "sswFilter"]
regions["SSW_TL"] = [7, "SSW_TL",   "sswFilter"]
regions["SSW_LL"] = [7, "SSW_LL",   "sswFilter"]

#regions["SSSig_TT"] = [7, "SSSig_TT",   "sssigFilter"]
regions["SSSig_LT"] = [7, "SSSig_LT",   "sssigFilter"]
regions["SSSig_TL"] = [7, "SSSig_TL",   "sssigFilter"]
regions["SSSig_LL"] = [7, "SSSig_LL",   "sssigFilter"]
"""


#regions["FAKES_NUM_F0"]   = [3,  "tight", "final"]
#regions["FAKES_DEN_F0"]   = [3,  "loose", "final"]

"""
regions["FAKES_NUM_F1"]   = [7,  "tight", "final"]
regions["FAKES_DEN_F1"]   = [7,  "loose", "final"]
regions["FAKES_NUM_F2"]   = [7,  "tight", "final"]
regions["FAKES_DEN_F2"]   = [7,  "loose", "final"]

regions["FAKES_NUM_F3"]   = [7,  "tight", "final"]
regions["FAKES_DEN_F3"]   = [7,  "loose", "final"]

regions["FAKES_NUM_F4"]   = [7,  "tight", "final"]
regions["FAKES_DEN_F4"]   = [7,  "loose", "final"]

regions["FAKES_NUM_F5"]   = [7,  "tight", "final"]
regions["FAKES_DEN_F5"]   = [7,  "loose", "final"]

regions["FAKES_NUM_F6"]   = [7,  "tight", "final"]
regions["FAKES_DEN_F6"]   = [7,  "loose", "final"]

regions["FAKES_NUM_F7"]   = [7,  "tight", "final"]
regions["FAKES_DEN_F7"]   = [7,  "loose", "final"]

regions["FAKES_NUM_F8"]   = [7,  "tight", "final"]
regions["FAKES_DEN_F8"]   = [7,  "loose", "final"]

regions["FAKES_NUM_F9"]   = [7,  "tight", "final"]
regions["FAKES_DEN_F9"]   = [7,  "loose", "final"]
"""

#"""
regions["FAKES_NUM_F1"]   = [3,  "num", "1prong"]
regions["FAKES_DEN_F1"]   = [3,  "den", "1prong"]

regions["FAKES_NUM_F2"]   = [3,  "num", "1prong"]
regions["FAKES_DEN_F2"]   = [3,  "den", "1prong"]

"""
regions["FAKES_NUM_F2"]   = [2,  "num", "1prong"]
regions["FAKES_DEN_F2"]   = [2,  "den", "1prong"]

regions["FAKES_NUM_F3"]   = [3,  "num", "1prong"]
regions["FAKES_DEN_F3"]   = [3,  "den", "1prong"]

regions["FAKES_NUM_F4"]   = [1,  "num", "1prong"]
regions["FAKES_DEN_F4"]   = [1,  "den", "1prong"]

regions["FAKES_NUM_F5"]   = [2,  "num", "1prong"]
regions["FAKES_DEN_F5"]   = [2,  "den", "1prong"]

regions["FAKES_NUM_F6"]   = [2,  "num", "1prong"]
regions["FAKES_DEN_F6"]   = [2,  "den", "1prong"]

regions["FAKES_NUM_F7"]   = [2,  "num", "1prong"]
regions["FAKES_DEN_F7"]   = [2,  "den", "1prong"]

regions["FAKES_NUM_F8"]   = [3,  "num", "1prong"]
regions["FAKES_DEN_F8"]   = [3,  "den", "1prong"]

regions["FAKES_NUM_F9"]   = [3,  "num", "1prong"]
regions["FAKES_DEN_F9"]   = [3,  "den", "1prong"]
"""
#"""

"""
regions["FAKES_NUM_F1"]   = [3,  "num", "twotau"]
regions["FAKES_DEN_F1"]   = [3,  "den", "twotau"]

regions["FAKES_NUM_F2"]   = [3,  "num", "twotau"]
regions["FAKES_DEN_F2"]   = [3,  "den", "twotau"]

regions["FAKES_NUM_F3"]   = [2,  "num", "twotau"]
regions["FAKES_DEN_F3"]   = [2,  "den", "twotau"]

regions["FAKES_NUM_F4"]   = [2,  "num", "twotau"]
regions["FAKES_DEN_F4"]   = [2,  "den", "twotau"]

regions["FAKES_NUM_F5"]   = [4,  "num", "twotau"]
regions["FAKES_DEN_F5"]   = [4,  "den", "twotau"]

regions["FAKES_NUM_F6"]   = [5,  "num", "twotau"]
regions["FAKES_DEN_F6"]   = [5,  "den", "twotau"]

regions["FAKES_NUM_F7"]   = [6,  "num", "twotau"]
regions["FAKES_DEN_F7"]   = [6,  "den", "twotau"]

regions["FAKES_NUM_F8"]   = [6,  "num", "twotau"]
regions["FAKES_DEN_F8"]   = [6,  "den", "twotau"]

regions["FAKES_NUM_F9"]   = [6,  "num", "twotau"]
regions["FAKES_DEN_F9"]   = [6,  "den", "twotau"]
"""

#regions["FAKESVR1_MAINREG"] = [3, "CR_Mvis<200GeV",   "newfull"]
"""
regions["FAKESVR1_TT"]      = [3, "TT_Mvis<200GeV",   "newfull"]
regions["FAKESVR1_LL"]      = [3, "LL_Mvis<200GeV",   "newfull"]
regions["FAKESVR1_TL"]      = [3, "TL_Mvis<200GeV",   "newfull"]
regions["FAKESVR1_LT"]      = [3, "LT_Mvis<200GeV",   "newfull"]
regions["FAKESVR1_TTT"]     = [3, "TTT_Mvis<200GeV",  "newfull"]
regions["FAKESVR1_TTL"]     = [3, "TTL_Mvis<200GeV",  "newfull"]
regions["FAKESVR1_TLT"]     = [3, "TLT_Mvis<200GeV",  "newfull"]
regions["FAKESVR1_LTT"]     = [3, "LTT_Mvis<200GeV",  "newfull"]
"""

#regions["FAKESVR2_MAINREG"] = [3, "VR_MET>30GeV",   "newfull"]
"""
regions["FAKESVR2_TT"]      = [3, "TT_MET>30GeV",   "newfull"]
regions["FAKESVR2_LL"]      = [3, "LL_MET>30GeV",   "newfull"]
regions["FAKESVR2_TL"]      = [3, "TL_MET>30GeV",   "newfull"]
regions["FAKESVR2_LT"]      = [3, "LT_MET>30GeV",   "newfull"]
regions["FAKESVR2_TTT"]     = [3, "TTL_MET>30GeV",  "newfull"]
regions["FAKESVR2_TTL"]     = [3, "TTL_MET>30GeV",  "newfull"]
regions["FAKESVR2_TLT"]     = [3, "TLT_MET>30GeV",  "newfull"]
regions["FAKESVR2_LTT"]     = [3, "LTT_MET>30GeV",  "newfull"]
"""

#regions["FAKESVR3_MAINREG"] = [3, "1_OR_2_bjets",   "newfull"]
"""
regions["FAKESVR3_TT"]      = [3, "TT_1_OR_2_bjets",   "newfull"]
regions["FAKESVR3_LL"]      = [3, "LL_1_OR_2_bjets",   "newfull"]
regions["FAKESVR3_TL"]      = [3, "TL_1_OR_2_bjets",   "newfull"]
regions["FAKESVR3_LT"]      = [3, "LT_1_OR_2_bjets",   "newfull"]
regions["FAKESVR3_TTT"]     = [3, "TTT_1_OR_2_bjets",  "newfull"]
regions["FAKESVR3_TTL"]     = [3, "TTL_1_OR_2_bjets",  "newfull"]
regions["FAKESVR3_TLT"]     = [3, "TLT_1_OR_2_bjets",  "newfull"]
regions["FAKESVR3_LTT"]     = [3, "LTT_1_OR_2_bjets",  "newfull"]
"""

#regions["FAKESVR4_MAINREG"] = [3, "VR_#DeltaR>3.5",   "newfull"]
"""
regions["FAKESVR4_TT"]      = [3, "TT_#DeltaR>3.5",   "newfull"]
regions["FAKESVR4_LL"]      = [3, "LL_#DeltaR>3.5",   "newfull"]
regions["FAKESVR4_TL"]      = [3, "TL_#DeltaR>3.5",   "newfull"]
regions["FAKESVR4_LT"]      = [3, "LT_#DeltaR>3.5",   "newfull"]
regions["FAKESVR4_TTT"]     = [3, "TTT_#DeltaR>3.5",  "newfull"]
regions["FAKESVR4_TTL"]     = [3, "TTL_#DeltaR>3.5",  "newfull"]
regions["FAKESVR4_TLT"]     = [3, "TLT_#DeltaR>3.5",  "newfull"]
regions["FAKESVR4_LTT"]     = [3, "LTT_#DeltaR>3.5",  "newfull"]
"""

#regions["FAKESVR5_MAINREG"] = [3, "VR_pT<80GeV",   "newfull"]
"""
regions["FAKESVR5_TT"]      = [3, "TT_pT<80GeV ",   "newfull"]
regions["FAKESVR5_LL"]      = [3, "LL_pT<80GeV ",   "newfull"]
regions["FAKESVR5_TL"]      = [3, "TL_pT<80GeV ",   "newfull"]
regions["FAKESVR5_LT"]      = [3, "LT_pT<80GeV ",   "newfull"]
regions["FAKESVR5_TTT"]     = [3, "TTT_pT<80GeV",  "newfull"]
regions["FAKESVR5_TTL"]     = [3, "TTL_pT<80GeV",  "newfull"]
regions["FAKESVR5_TLT"]     = [3, "TLT_pT<80GeV",  "newfull"]
regions["FAKESVR5_LTT"]     = [3, "LTT_pT<80GeV",  "newfull"]
"""

#---------------------
# Make input tarball
#---------------------
if os.path.exists(os.path.join(INTARBALL)):
  print 'removing existing tarball %s...'% (INTARBALL)
  cmd = 'rm %s' % (INTARBALL)
  m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
  m.communicate()[0]

print 'building input tarball %s...'% (INTARBALL)
cmd = 'cd %s; make -f Makefile.plots TARBALL=%s' % (MAIN,INTARBALL)
m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
m.communicate()[0]


for REG,OPT in regions.iteritems():
  #vars_list = plots.vars_mumu.vars_list
  #vars_list = plots.vars_fakes.vars_list
  vars_list = plots.vars_tau.vars_list

  for var in vars_list:

    job_vars['VAR']      = var.name
    job_vars['REG']      = REG
    job_vars['ICUT']     = OPT[0]
    job_vars['LAB']      = OPT[1]
    job_vars['TAG']      = OPT[2]
    job_vars['MAKEPLOT'] = True
    job_vars['FAKEST']   = fake_estimate
    
    VARS = []
    
    for vname in job_vars.keys(): VARS += ['%s=%s' % (vname,job_vars[vname])]
    
    cmd = 'qsub'
    cmd += " -q %s" % QUEUE
    cmd += ' -v "%s"' % (','.join(VARS))
    cmd += ' -N j.plots.%s' % (make_tag(REG,job_vars['VAR']))
    cmd += ' -o %s/log' % (OUTDIR)
    cmd += ' -e %s/log' % (OUTDIR)
    cmd += ' %s' % BEXEC
    print cmd
    m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    print m.communicate()[0]
 
 
## EOF

