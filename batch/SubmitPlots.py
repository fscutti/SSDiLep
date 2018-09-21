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

indir    = 'HistTEST'
outdir   = 'PlotsTEST'

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
#fake_estimate = "TwoLepRegions"
#fake_estimate = "LeadLepRegions"
fake_estimate = "MixedRegions"
#fake_estimate = "Subtraction"

regions = {}
# use it as such:
#regions["FOLDERNAME"]     = [icut, "plot label"]

regions["OSZ_MAINREG"] = [3, "OSZ_MAINREG",   "mixedreg"]
#regions["OSZ_TT"] = [3, "OSZ_TT",   "osz"]
#regions["OSZ_LT"] = [3, "OSZ_LT",   "osz"]
#regions["OSZ_TL"] = [3, "OSZ_TL",   "osz"]
#regions["OSZ_LL"] = [3, "OSZ_LL",   "osz"]


#"""

"""
regions["FAKES_NUM_F1"]   = [3,  "num", "1prong"]
regions["FAKES_DEN_F1"]   = [3,  "den", "1prong"]

regions["FAKES_NUM_F2"]   = [3,  "num", "1prong"]
regions["FAKES_DEN_F2"]   = [3,  "den", "1prong"]

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

