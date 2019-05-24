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

#indir    = 'HistVROnePair'
#outdir   = 'PlotsVROnePair'

#indir    = 'HistSRTwoPairs'
#outdir   = 'PlotsSRTwoPairs'

#indir    = 'HistFILTEROnePair'
#outdir   = 'PlotsFILTEROnePair'

#indir    = 'HistFILTERTwoPairs'
#outdir   = 'PlotsFILTERTwoPairs'

#indir    = 'HistCF3May'
#outdir   = 'PlotsCF3May'

#indir    = 'HistBASETwoPairs'
#outdir   = 'PlotsBASETwoPairs'

#indir    = 'HistFFTracks'
#outdir   = 'PlotsFFTracks'

#indir    = 'HistFFComposition'
#outdir   = 'PlotsFFComposition'

indir    = 'HistFFgroupV5'
outdir   = 'PlotsFFgroupV5'

#indir    = 'HistSROnePairFullc'
#outdir   = 'PlotsSROnePairFullc'

#indir    = 'HistSRTwoPairsFullc'
#outdir   = 'PlotsSRTwoPairsFullc'

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
#fake_estimate = "MixedRegions"
#fake_estimate = "Subtraction"
fake_estimate = "NoFakes"

#---------------------
# Plotting scheme
#---------------------
renorm = False
makeoverlay = False
makeplot = True

regions = {}
# use it as such:
#regions["FOLDERNAME"]     = [icut, "plot label", "file id"]

# ---------------------------
# Signal regions
# ---------------------------
"""
regions["1SF2L_SignalRegionFiltered"]    = [3, "1SF2L_SignalRegionFiltered", "1SF2L_SignalRegionFiltered"]
regions["1DF2L_SignalRegionFiltered"]    = [3, "1DF2L_SignalRegionFiltered", "1DF2L_SignalRegionFiltered"]

regions["1SF3L_SignalRegionFiltered"]    = [3, "1SF3L_SignalRegionFiltered", "1SF3L_SignalRegionFiltered"]
regions["1DF3L_SignalRegionFiltered"]    = [3, "1DF3L_SignalRegionFiltered", "1DF3L_SignalRegionFiltered"]


regions["1SF2L_SignalRegionNonFiltered"]    = [3, "1SF2L_SignalRegionNonFiltered", "1SF2L_SignalRegionNonFiltered"]
regions["1DF2L_SignalRegionNonFiltered"]    = [3, "1DF2L_SignalRegionNonFiltered", "1DF2L_SignalRegionNonFiltered"]

regions["1SF3L_SignalRegionNonFiltered"]    = [3, "1SF3L_SignalRegionNonFiltered", "1SF3L_SignalRegionNonFiltered"]
regions["1DF3L_SignalRegionNonFiltered"]    = [3, "1DF3L_SignalRegionNonFiltered", "1DF3L_SignalRegionNonFiltered"]
"""

"""
regions["2SF4L_SignalRegionFiltered"]    = [3, "2SF4L_SignalRegionFiltered", "2SF4L_SignalRegionFiltered"]
regions["al1DF4L_SignalRegionFiltered"]  = [2, "al1DF4L_SignalRegionFiltered", "al1DF4L_SignalRegionFiltered"]

regions["2SF4L_SignalRegionNonFiltered"]    = [3, "2SF4L_SignalRegionNonFiltered", "2SF4L_SignalRegionNonFiltered"]
regions["al1DF4L_SignalRegionNonFiltered"]  = [2, "al1DF4L_SignalRegionNonFiltered", "al1DF4L_SignalRegionNonFiltered"]
"""


# ---------------------------
# SideBands
# ---------------------------
"""
regions["1SF2L_SideBandFiltered"]    = [3, "1SF2L_SideBandFiltered", "1SF2L_SideBandFiltered"]
regions["1DF2L_SideBandFiltered"]    = [3, "1DF2L_SideBandFiltered", "1DF2L_SideBandFiltered"]

regions["1SF3L_SideBandFiltered"]    = [3, "1SF3L_SideBandFiltered", "1SF3L_SideBandFiltered"]
regions["1DF3L_SideBandFiltered"]    = [3, "1DF3L_SideBandFiltered", "1DF3L_SideBandFiltered"]


regions["1SF2L_SideBandNonFiltered"]    = [3, "1SF2L_SideBandNonFiltered", "1SF2L_SideBandNonFiltered"]
regions["1DF2L_SideBandNonFiltered"]    = [3, "1DF2L_SideBandNonFiltered", "1DF2L_SideBandNonFiltered"]

regions["1SF3L_SideBandNonFiltered"]    = [3, "1SF3L_SideBandNonFiltered", "1SF3L_SideBandNonFiltered"]
regions["1DF3L_SideBandNonFiltered"]    = [3, "1DF3L_SideBandNonFiltered", "1DF3L_SideBandNonFiltered"]
"""


#regions["2SF4L_SideBandFiltered"]    = [3, "2SF4L_SideBandFiltered", "2SF4L_SideBandFiltered"]
#regions["al1DF4L_SideBandFiltered"]  = [2, "al1DF4L_SideBandFiltered", "al1DF4L_SideBandFiltered"]

#regions["2SF4L_SideBandNonFiltered"]    = [3, "2SF4L_SideBandNonFiltered", "2SF4L_SideBandNonFiltered"]
#regions["al1DF4L_SideBandNonFiltered"]  = [2, "al1DF4L_SideBandNonFiltered", "al1DF4L_SideBandNonFiltered"]



# ---------------------------
# tau CF studies
# ---------------------------
#"""
#regions["BASELINE"]    = [0, "BASELINE", "taucf"]
#regions["OSZ"]         = [3, "OSZMvisWin", "taucf"]
#regions["SSZ"]         = [3, "SSZMvisWin", "taucf"]
#regions["FullOSZ"]     = [2, "OSZFullMVis", "taucf"]
#regions["FullSSZ"]     = [2, "SSZFullMVis", "taucf"]

#regions["OSTTBAR"]     = [3, "OSTTBAR2BJets", "taucf"]
#regions["SSTTBAR"]     = [3, "SSTTBAR2BJets", "taucf"]
#regions["FullOSTTBAR"] = [1, "OSTTBARalOneBJet", "taucf"]
#regions["FullSSTTBAR"] = [1, "SSTTBARalOneBJet", "taucf"]

"""
regions["OSTTBAR_nofil"]         = [4, "OSTTBAR2BJets", "nofiltaucf"]
regions["SSTTBAR_nofil"]         = [4, "SSTTBAR2BJets", "nofiltaucf"]
regions["FullOSTTBAR_nofil"]     = [2, "OSTTBARalOneBJet", "nofiltaucf"]
regions["FullSSTTBAR_nofil"]     = [2, "SSTTBARalOneBJet", "nofiltaucf"]
regions["HiPtFullOSTTBAR_nofil"] = [4, "HiPtOSTTBARalOneBJet", "nofiltaucf"]
regions["HiPtFullSSTTBAR_nofil"] = [4, "HiPtSSTTBARalOneBJet", "nofiltaucf"]

regions["OSTTBAR_fil"]         = [4, "OSTTBAR2BJets", "filtaucf"]
regions["SSTTBAR_fil"]         = [4, "SSTTBAR2BJets", "filtaucf"]
regions["FullOSTTBAR_fil"]     = [2, "OSTTBARalOneBJet", "filtaucf"]
regions["FullSSTTBAR_fil"]     = [2, "SSTTBARalOneBJet", "filtaucf"]
regions["HiPtFullOSTTBAR_fil"] = [4, "HiPtOSTTBARalOneBJet", "filtaucf"]
regions["HiPtFullSSTTBAR_fil"] = [4, "HiPtSSTTBARalOneBJet", "filtaucf"]

regions["OSTTBAR_antifil"]         = [4, "OSTTBAR2BJets", "antifiltaucf"]
regions["SSTTBAR_antifil"]         = [4, "SSTTBAR2BJets", "antifiltaucf"]
regions["FullOSTTBAR_antifil"]     = [2, "OSTTBARalOneBJet", "antifiltaucf"]
regions["FullSSTTBAR_antifil"]     = [2, "SSTTBARalOneBJet", "antifiltaucf"]
regions["HiPtFullOSTTBAR_antifil"] = [4, "HiPtOSTTBARalOneBJet", "antifiltaucf"]
regions["HiPtFullSSTTBAR_antifil"] = [4, "HiPtSSTTBARalOneBJet", "antifiltaucf"]
"""

#"""

#regions["BASELINE"]    = [0, "BASELINE", "optim"]

# ---------------------------
# tau fake factors validation
# ---------------------------
#regions["OSZ_MAINREG"] = [3, "OSZ_MAINREG",   "mixedreg"]
#regions["OSZ_TT"] = [3, "OSZ_TT",   "osz"]
#regions["OSZ_LT"] = [3, "OSZ_LT",   "osz"]
#regions["OSZ_TL"] = [3, "OSZ_TL",   "osz"]
#regions["OSZ_LL"] = [3, "OSZ_LL",   "osz"]


# ----------------
# tau fake factors
# ----------------
#"""
#for wp in ["Loose","Medium","Tight"]:
#for ptbin in ["All","2030","3040","4060","6090","90150","150inf"]:
#for ptbin in ["All","2030","3040","4060","6090","90150","150inf"]:
#"""
for wp in ["Medium"]:
  for prongs in ["1P","3P"]:
    for ptbin in ["All"]:

      regions["FAKES_NUM_%s%s_%s_F1"%(prongs,wp,ptbin)]   = [5,  "num", "%s%s_%s"%(prongs,wp,ptbin)]
      regions["FAKES_DEN_%s%s_%s_F1"%(prongs,wp,ptbin)]   = [5,  "den", "%s%s_%s"%(prongs,wp,ptbin)]
     
      regions["FAKES_NUM_%s%s_%s_F2"%(prongs,wp,ptbin)]   = [5,  "num", "%s%s_%s"%(prongs,wp,ptbin)]
      regions["FAKES_DEN_%s%s_%s_F2"%(prongs,wp,ptbin)]   = [5,  "den", "%s%s_%s"%(prongs,wp,ptbin)]

      regions["FAKES_NUM_%s%s_%s_F10"%(prongs,wp,ptbin)]   = [4,  "num", "%s%s_%s"%(prongs,wp,ptbin)]
      regions["FAKES_DEN_%s%s_%s_F10"%(prongs,wp,ptbin)]   = [4,  "den", "%s%s_%s"%(prongs,wp,ptbin)]
     
      regions["FAKES_NUM_%s%s_%s_F11"%(prongs,wp,ptbin)]   = [4,  "num", "%s%s_%s"%(prongs,wp,ptbin)]
      regions["FAKES_DEN_%s%s_%s_F11"%(prongs,wp,ptbin)]   = [4,  "den", "%s%s_%s"%(prongs,wp,ptbin)]

      #regions["FAKES_QNUM_%s%s_%s_F1"%(prongs,wp,ptbin)]   = [6,  "num", "%s%s_%s"%(prongs,wp,ptbin)]
      #regions["FAKES_QDEN_%s%s_%s_F1"%(prongs,wp,ptbin)]   = [6,  "den", "%s%s_%s"%(prongs,wp,ptbin)]

      #regions["FAKES_GNUM_%s%s_%s_F1"%(prongs,wp,ptbin)]   = [6,  "num", "%s%s_%s"%(prongs,wp,ptbin)]
      #regions["FAKES_GDEN_%s%s_%s_F1"%(prongs,wp,ptbin)]   = [6,  "den", "%s%s_%s"%(prongs,wp,ptbin)]

      #regions["FAKES_UNUM_%s%s_%s_F1"%(prongs,wp,ptbin)]   = [6,  "num", "%s%s_%s"%(prongs,wp,ptbin)]
      #regions["FAKES_UDEN_%s%s_%s_F1"%(prongs,wp,ptbin)]   = [6,  "den", "%s%s_%s"%(prongs,wp,ptbin)]
#""" 
#"""


"""
regions["FAKES_QUARKS_F1"]     = [3,  "quarks", "incl"]
regions["FAKES_QUARKS_1PF1"]   = [4,  "quarks", "1prong"]
regions["FAKES_QUARKS_3PF1"]   = [4,  "quarks", "3prong"]

regions["FAKES_GLUONS_F1"]     = [3,  "gluons", "incl"]
regions["FAKES_GLUONS_1PF1"]   = [4,  "gluons", "1prong"]
regions["FAKES_GLUONS_3PF1"]   = [4,  "gluons", "3prong"]

regions["FAKES_TRUETAUHAD_F1"]     = [3,  "truetaus", "incl"]
regions["FAKES_TRUETAUHAD_1PF1"]   = [4,  "truetaus", "1prong"]
regions["FAKES_TRUETAUHAD_3PF1"]   = [4,  "truetaus", "3prong"]

regions["FAKES_NOFILTER_F1"]     = [2,  "nofil", "incl"]
regions["FAKES_NOFILTER_1PF1"]   = [3,  "nofil", "1prong"]
regions["FAKES_NOFILTER_3PF1"]   = [3,  "nofil", "3prong"]

regions["FAKES_UNKNOWN_F1"]     = [3,  "unknown", "incl"]
regions["FAKES_UNKNOWN_1PF1"]   = [4,  "unknown", "1prong"]
regions["FAKES_UNKNOWN_3PF1"]   = [4,  "unknown", "3prong"]
"""


"""
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

# ------------
# tracks study
# ------------
"""
regions["FAKES_QUARKS_F1"] = [3,  "nominal",       "incl"]
regions["FAKES_QUARKS_F2"] = [4,  "PTratio>1",     "incl"]
regions["FAKES_QUARKS_F3"] = [4,  "PTratio<1",     "incl"]
regions["FAKES_QUARKS_F4"] = [2,  "TwoJets",       "incl"]
regions["FAKES_QUARKS_F5"] = [1,  "AtLeastOneJet", "incl"]

regions["FAKES_GLUONS_F1"] = [3,  "nominal",       "incl"]
regions["FAKES_GLUONS_F2"] = [4,  "PTratio>1",     "incl"]
regions["FAKES_GLUONS_F3"] = [4,  "PTratio<1",     "incl"]
regions["FAKES_GLUONS_F4"] = [2,  "TwoJets",       "incl"]
regions["FAKES_GLUONS_F5"] = [1,  "AtLeastOneJet", "incl"]
"""

# -------------
# overlay study
# -------------

# shape comparison
# ----------------
"""
for trigger in ['NoTrig']:
  for ntau in ['1']:
    
    ovregions = "BASELINE:3"
    
    # for shapes comparison
    regions[ovregions] = [ovregions,  "%s_1SSPair_al%sTau"%(trigger,ntau), "shapes"]
    #regions[ovregions] = [ovregions,  "%s_2SSPair_al%sTau"%(trigger,ntau), "shapes"]
"""

# yield comparison
# ----------------
"""
for trigger in ['STT','DTT','SET','SMT','MTT','ETT']:
  #for ntau in ['1','2','3','4']:
  for ntau in ['1']:
    
    ovregions = "BASELINE:3"
    
    for idwp in ['Loose','Medium','Tight']:
      for ewp in ['Loose','Medium','Tight']:
        ovregions += ";%s_al%sTAU_BDT%s_eBDT%s:6"%(trigger,ntau,idwp,ewp)
    
    #regions[ovregions] = [ovregions,  "%s_1SSPair_al%sTau"%(trigger,ntau), "mH400"]
    #regions[ovregions] = [ovregions,  "%s_1SSPair_al%sTau"%(trigger,ntau), "mH700"]
    #regions[ovregions] = [ovregions,  "%s_1SSPair_al%sTau"%(trigger,ntau), "mH1100"]
    
    
    #regions[ovregions] = [ovregions,  "%s_2SSPair_al%sTau"%(trigger,ntau), "mH400"]
    #regions[ovregions] = [ovregions,  "%s_2SSPair_al%sTau"%(trigger,ntau), "mH700"]
    regions[ovregions] = [ovregions,  "%s_2SSPair_al%sTau"%(trigger,ntau), "mH1100"]

"""

"""
for sreg in ['1P2L','1P3L']:
#for sreg in ['2P4L']:
 # signal regions
 for trigger in ['STT','DTT','SET','SMT','MTT','ETT']:
      for ntau in ['1']:
        
        ovregions = "BASELINE:0"
        
        for idwp in ['Loose','Medium','Tight']:
          for ewp in ['Loose','Medium','Tight']:
            ovregions += ";%s_%s_al%sTAU_BDT%s_eBDT%s:4"%(trigger,sreg,ntau,idwp,ewp)
        
        regions[ovregions] = [ovregions,  "%s_%s_al%sTau"%(trigger,sreg,ntau), "shapes"]
        regions[ovregions] = [ovregions,  "%s_%s_al%sTau"%(trigger,sreg,ntau), "mH400"]
        regions[ovregions] = [ovregions,  "%s_%s_al%sTau"%(trigger,sreg,ntau), "mH700"]
        regions[ovregions] = [ovregions,  "%s_%s_al%sTau"%(trigger,sreg,ntau), "mH1100"]

"""



"""
for wp in ["Medium"]:
  for prongs in ["1P","3P"]:
    for ptbin in ["All","2030","3040","4060","6090","90150","150inf"]:
      
      ovregions = "FAKES_UDEN_%s%s_%s_F10:5"%(prongs,wp,ptbin)
      ovregions += ";FAKES_QDEN_%s%s_%s_F10:5"%(prongs,wp,ptbin)
      ovregions += ";FAKES_GDEN_%s%s_%s_F10:5"%(prongs,wp,ptbin)

      regions[ovregions]   = [ovregions,  "den_%s%s_%s"%(prongs,wp,ptbin), "shapes"]

      ovregions = "FAKES_UNUM_%s%s_%s_F10:5"%(prongs,wp,ptbin)
      ovregions += ";FAKES_QNUM_%s%s_%s_F10:5"%(prongs,wp,ptbin)
      ovregions += ";FAKES_GNUM_%s%s_%s_F10:5"%(prongs,wp,ptbin)

      regions[ovregions]   = [ovregions,  "num_%s%s_%s"%(prongs,wp,ptbin), "shapes"]
"""

"""
for wp in ["Medium"]:
  for prongs in ["1P","3P"]:
    for ptbin in ["All","2030","3040","4060","6090","90150","150inf"]:
      
      ovregions = "FAKES_QDEN_%s%s_%s_F1:6"%(prongs,wp,ptbin)
      ovregions += ";FAKES_QDEN_%s%s_%s_F10:5"%(prongs,wp,ptbin)

      regions[ovregions]   = [ovregions,  "den_%s%s_%s"%(prongs,wp,ptbin), "shapes"]

      ovregions = "FAKES_GDEN_%s%s_%s_F1:6"%(prongs,wp,ptbin)
      ovregions += ";FAKES_GDEN_%s%s_%s_F10:5"%(prongs,wp,ptbin)

      regions[ovregions]   = [ovregions,  "den_%s%s_%s"%(prongs,wp,ptbin), "shapes"]

      ovregions = "FAKES_QNUM_%s%s_%s_F1:6"%(prongs,wp,ptbin)
      ovregions += ";FAKES_QNUM_%s%s_%s_F10:5"%(prongs,wp,ptbin)

      regions[ovregions]   = [ovregions,  "num_%s%s_%s"%(prongs,wp,ptbin), "shapes"]

      ovregions = "FAKES_GNUM_%s%s_%s_F1:6"%(prongs,wp,ptbin)
      ovregions += ";FAKES_GNUM_%s%s_%s_F10:5"%(prongs,wp,ptbin)

      regions[ovregions]   = [ovregions,  "num_%s%s_%s"%(prongs,wp,ptbin), "shapes"]
"""

"""
for wp in ["Medium"]:
  for prongs in ["1P","3P"]:
    for ptbin in ["All","2030","3040","4060","6090","90150","150inf"]:
      
      ovregions = "FAKES_DEN_%s%s_%s_F1:5"%(prongs,wp,ptbin)
      ovregions += ";FAKES_DEN_%s%s_%s_F10:4"%(prongs,wp,ptbin)

      regions[ovregions]   = [ovregions,  "den_%s%s_%s"%(prongs,wp,ptbin), "shapes"]

      ovregions = "FAKES_NUM_%s%s_%s_F1:5"%(prongs,wp,ptbin)
      ovregions += ";FAKES_NUM_%s%s_%s_F10:4"%(prongs,wp,ptbin)

      regions[ovregions]   = [ovregions,  "num_%s%s_%s"%(prongs,wp,ptbin), "shapes"]
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

vars_list = []
#vars_list += plots.vars_mumu.vars_list
vars_list += plots.vars_tau.vars_list
#vars_list += plots.vars_onepair.vars_list
#vars_list += plots.vars_multipairs.vars_list

for REG,OPT in regions.iteritems():
  
  for var in vars_list:
    
    REG = REG.split(":")[0]
    
    job_vars['VAR']         = var.name
    job_vars['REG']         = str(REG)
    job_vars['OVREG']       = str(OPT[0])
    job_vars['ICUT']        = str(OPT[0])
    job_vars['LAB']         = str(OPT[1])
    job_vars['TAG']         = str(OPT[2])
    job_vars['MAKEPLOT']    = makeplot
    job_vars['MAKEOVERLAY'] = makeoverlay
    job_vars['RENORM']      = renorm
    job_vars['FAKEST']      = fake_estimate
    
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

