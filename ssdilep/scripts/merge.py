## modules
import ROOT

import histmgr
import funcs
import os

from ssdilep.samples import samples
from ssdilep.plots   import vars_mumu
from systematics     import *

from optparse import OptionParser


#-----------------
# input
#-----------------
parser = OptionParser()
parser.add_option('-v', '--var', dest='vname',
                  help='varable name',metavar='VAR',default=None)
parser.add_option('-r', '--reg', dest='region',
                  help='region name',metavar='REG',default=None)
parser.add_option('-l', '--lab', dest='label',
                  help='region label',metavar='LAB',default=None)
parser.add_option('-c', '--icut', dest='icut',
                  help='number of cuts',metavar='ICUT',default=None)
parser.add_option('-p', '--makeplot', dest='makeplot',
                  help='make plot',metavar='MAKEPLOT',default=None)
parser.add_option('-i', '--input', dest='indir',
                  help='input directory',metavar='INDIR',default=None)
parser.add_option('-o', '--output', dest='outdir',
                  help='output directory',metavar='OUTDIR',default=None)
parser.add_option('-f', '--fakest', dest='fakest',
                  help='choose fake estimate',metavar='FAKEST',default=None)
parser.add_option('-t', '--tag', dest='tag',
                  help='outfile tag',metavar='TAG',default=None)


(options, args) = parser.parse_args()

#-----------------
# Configuration
#-----------------
lumi =  18232.8
#lumi =  33257.2 + 3212.96

# Control regions
plotsfile = []
if options.makeplot == "False":
  plotsfile.append("hists")
plotsfile.append(options.vname)
plotsfile.append(options.region)
plotsfile.append(options.tag)

for s in plotsfile:
  if not s: plotsfile.remove(s)

plotsfile = "_".join(plotsfile)+".root"
plotsfile = os.path.join(options.outdir,plotsfile)

ROOT.gROOT.SetBatch(True)
hm = histmgr.HistMgr(basedir=options.indir,target_lumi=lumi)

#-----------------
# Samples        
#-----------------

# base samples
data           = samples.data
mc_backgrounds = samples.mc_backgrounds
fakes          = samples.addon_fakes

# recombined samples
addon_data     = samples.addon_data
addon_samples  = samples.addon_samples

## signals
mumu_signals = []
#mumu_signals.append(samples.all_DCH)
#mumu_signals.append(samples.DCH800)


#--------------
# Estimators
#--------------
for s in mc_backgrounds + mumu_signals + [data]: 
    histmgr.load_base_estimator(hm,s)

main_addition_regions    = []
fake_addition_regions    = []
fake_subtraction_regions = []

reg_prefix, reg_suffix = funcs.get_pref_and_suff(options.region)

if reg_suffix == "MAINREG":
  fake_subtraction_regions = ["LL"]
  
  if options.fakest == "FullRegions":
    main_addition_regions = ["TT","TTT","TTTT"]
    fake_addition_regions = ["TL","LT","TTL","TLT","LTT","TTTL","TTLT","TLTT","LTTT"]
  
  if options.fakest == "ReducedRegions":
    main_addition_regions = ["TT"]
    fake_addition_regions = ["TL","LT"]
else:
  
  if options.fakest == "Subtraction":
    main_addition_regions =  fake_addition_regions = [""]
    reg_prefix            =  options.region

fakes.estimator = histmgr.AddRegEstimator(
      hm                  = hm, 
      sample              = fakes,
      data_sample         = data,
      mc_samples          = mc_backgrounds, 
      addition_regions    = ["_".join([reg_prefix]+[suffix]).rstrip("_") for suffix in fake_addition_regions],
      subtraction_regions = ["_".join([reg_prefix]+[suffix]).rstrip("_") for suffix in fake_subtraction_regions]
      )

for s in addon_samples + [addon_data]:
  s.estimator = histmgr.AddRegEstimator(
      hm               = hm, 
      sample           = s,
      data_sample      = data,
      mc_samples       = mc_backgrounds, 
      addition_regions = ["_".join([reg_prefix]+[suffix]).rstrip("_") for suffix in main_addition_regions]
      )

#-----------------
# Systematics       
#-----------------
# just an example ...
mc_sys = [
    SYS1, 
    SYS2,
    ]

## set mc systematics
#for s in mc_backgrounds + mumu_signals:
#    s.estimator.add_systematics(mc_sys)

#fakes.estimator.add_systematics(FF)

mumu_vdict  = vars_mumu.vars_dict

#-----------------
# Plotting 
#-----------------

## order backgrounds for plots
plot_ord_bkg = []
plot_ord_bkg.append( fakes )
plot_ord_bkg += addon_samples


if options.makeplot == "True":
 funcs.plot_hist(
    backgrounds   = plot_ord_bkg,
    signal        = mumu_signals, 
    data          = addon_data,
    region        = options.region,
    label         = options.label,
    histname      = os.path.join(mumu_vdict[options.vname]['path'],mumu_vdict[options.vname]['hname']),
    xmin          = mumu_vdict[options.vname]['xmin'],
    xmax          = mumu_vdict[options.vname]['xmax'],
    rebin         = mumu_vdict[options.vname]['rebin'],
    log           = mumu_vdict[options.vname]['log'],
    icut          = int(options.icut),
    sys_dict      = sys_dict,
    #sys_dict      = None,
    do_ratio_plot = True,
    save_eps      = True,
    plotsfile     = plotsfile,
    )

else:
 funcs.write_hist(
         backgrounds = plot_ord_bkg,
         signal      = mumu_signals, # This can be a list
         data        = addon_data,
         region      = options.region,
         icut        = int(options.icut),
         histname    = os.path.join(mumu_vdict[options.vname]['path'],mumu_vdict[options.vname]['hname']),
         #rebin       = mumu_vdict[options.vname]['rebin'],
         rebin       = 1,
         sys_dict    = None,
         outname     = plotsfile
         )
 ## EOF



