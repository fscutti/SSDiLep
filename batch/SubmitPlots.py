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

#indir    = 'HistFFFullBVeto17May'
#outdir   = 'PlotsFFFullBVeto17May'

#indir    = 'HistFF25Mar'
#outdir   = 'PlotsFF25Mar'

indir    = 'HistFFJustOnePlot'
outdir   = 'PlotsFFJustOnePlot'

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
QUEUE     = 'short'
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
regions["ProbeTight_F1"] = [4, "TruthFilter_SS",   "truthfilter_ss"]
regions["ProbeLoose_F1"] = [4, "TruthFilter_SS",   "truthfilter_ss"]

regions["ProbeTight_F2"] = [4, "TruthFilter_OS",   "truthfilter_os"]
regions["ProbeLoose_F2"] = [4, "TruthFilter_OS",   "truthfilter_os"]

regions["ProbeTight_R1"] = [4, "FakeFilter_SS",   "fakefilter_ss"]
regions["ProbeLoose_R1"] = [4, "FakeFilter_SS",   "fakefilter_ss"]

regions["ProbeTight_R2"] = [4, "AntiTruth_SS",   "antitruth_ss"]
regions["ProbeLoose_R2"] = [4, "AntiTruth_SS",   "antitruth_ss"]

regions["ProbeTight_R3"] = [4, "FakeFilter_OS",   "fakefilter_os"]
regions["ProbeLoose_R3"] = [4, "FakeFilter_OS",   "fakefilter_os"]

regions["ProbeTight_R4"] = [4, "AntiTruth_OS",   "antitruth_os"]
regions["ProbeLoose_R4"] = [4, "AntiTruth_OS",   "antitruth_os"]
"""
#"""
regions["FAKES_NUM_F0"]   = [2,  "tight", "bveto"]
regions["FAKES_DEN_F0"]   = [2,  "loose", "bveto"]

regions["FAKES_NUM_F1"]   = [6,  "tight", "bveto"]
regions["FAKES_DEN_F1"]   = [6,  "loose", "bveto"]
#"""

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
  vars_list = plots.vars_mumu.vars_list
  #vars_list = plots.vars_fakes.vars_list

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

