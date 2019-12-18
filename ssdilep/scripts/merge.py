## modules
import ROOT

import histmgr
import funcs
import os

from ssdilep.samples import samples
from ssdilep.plots   import vars_mumu
from ssdilep.plots   import vars_tau
from ssdilep.plots   import vars_onepair
from ssdilep.plots   import vars_multipairs
from systematics     import *

from optparse import OptionParser


#-----------------
# input
#-----------------
parser = OptionParser()
parser.add_option('-v', '--var', dest='vname',
                  help='varable name',metavar='VAR',default=None)
parser.add_option('-r', '--reg', dest='region',
                  help='region name',metavar='REG',default="")
parser.add_option('-g', '--ovreg', dest='ovregions',
                  help='overlay regions',metavar='OVREG',default=None)
parser.add_option('-l', '--lab', dest='label',
                  help='region label',metavar='LAB',default=None)
parser.add_option('-c', '--icut', dest='icut',
                  help='number of cuts',metavar='ICUT',default=None)
parser.add_option('-p', '--makeplot', dest='makeplot',
                  help='make plot',metavar='MAKEPLOT',default=False)
parser.add_option('-m', '--makeoverlay', dest='makeoverlay',
                  help='make overlay',metavar='MAKEOVERLAY',default="False")
parser.add_option('-n', '--renorm', dest='renorm',
                  help='renormalise hists',metavar='RENORM',default=None)
parser.add_option('-i', '--input', dest='indir',
                  help='input directory',metavar='INDIR',default=None)
parser.add_option('-o', '--output', dest='outdir',
                  help='output directory',metavar='OUTDIR',default=None)
parser.add_option('-f', '--fakest', dest='fakest',
                  help='choose fake estimate',metavar='FAKEST',default="NoFakes")
parser.add_option('-t', '--tag', dest='tag',
                  help='outfile tag',metavar='TAG',default=None)


(options, args) = parser.parse_args()

#-----------------
# Configuration
#-----------------
#lumi = 79800.  / 10e6
#lumi = 79800. 
#lumi = 0. 
lumi  = 1.

ncuts = 1
if options.icut and not options.makeoverlay=="True":
  ncuts = int(options.icut)

# Control regions
plotsfile = []

if options.makeplot == "False":
  plotsfile.append("hists")
if options.makeoverlay == "True":
  plotsfile.append("overlay")

plotsfile.append(options.vname)
if options.region:
  plotsfile.append(options.region)

plotsfile.append(options.tag)

if options.makeoverlay == "True":
  plotsfile.append(options.label)

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
data    = samples.data
mc_bkg  = samples.mc_bkg
mc_fakes_bkg  = samples.mc_fakes_bkg
fakes   = samples.fakes

# recombined samples
recom_data     = data.copy()
recom_mc_bkg  = [ b.copy() for b in mc_bkg ]
#recom_mc_fakes_bkg  = [ b.copy() for b in mc_fakes_bkg ]

## signals
signals = []
#"""
#signals.append(samples.samples_DCH.Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH300)
#signals.append(samples.samples_DCH.Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH700)
#signals.append(samples.samples_DCH.Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH1100)
#"""
#signals.append(samples.DCH800)

"""
signals += [samples.samples_DCH.Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH300]
signals += [samples.samples_DCH.Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH700]
signals += [samples.samples_DCH.Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH1100]
"""

#--------------
# Estimators
#--------------
#for s in mc_bkg + mc_fakes_bkg + signals + [data]: 
for s in mc_bkg + signals + [data]: 
    histmgr.load_base_estimator(hm,s)

main_addition_regions    = []
fake_addition_regions    = []
fake_subtraction_regions = []

reg_prefix, reg_suffix = funcs.get_pref_and_suff(options.region)


if reg_suffix == "ValRegionFiltered" or reg_suffix == "SignalRegionFiltered" or reg_suffix == "CFRegionFiltered":
  
  # including all regions for fake-factor method
  # ---------------------------------------------
  if options.fakest == "AllRegions":
    main_addition_regions = [options.region]
    
    fake_addition_regions = [options.region.replace(reg_suffix, "SideBandFiltered")]
    fake_addition_regions += []
    fake_subtraction_regions = []

if options.fakest in [ "Subtraction", "NoFakes" ]:
  main_addition_regions =  fake_addition_regions = [""]
  reg_prefix            =  options.region

if options.fakest in [ "Simulation"]:
  main_addition_regions =  fake_addition_regions = [""]
  reg_prefix            =  options.region


# -------------------------------------------------------
# Estimation is always performed with the AddRegEstimator
# -------------------------------------------------------

fakes.estimator = histmgr.AddRegEstimator(
      hm                  = hm, 
      sample              = fakes,
      data_sample         = data,
      mc_samples          = mc_bkg, 
      #addition_regions    = ["_".join([reg_prefix]+[suffix]).rstrip("_") for suffix in fake_addition_regions],
      #subtraction_regions = ["_".join([reg_prefix]+[suffix]).rstrip("_") for suffix in fake_subtraction_regions]
      addition_regions    = fake_addition_regions,
      subtraction_regions = fake_subtraction_regions
      )

for s in recom_mc_bkg + [recom_data]:
  s.estimator = histmgr.AddRegEstimator(
      hm               = hm, 
      sample           = s,
      data_sample      = data,
      mc_samples       = mc_bkg, 
      #addition_regions = ["_".join([reg_prefix]+[suffix]).rstrip("_") for suffix in main_addition_regions]
      addition_regions = main_addition_regions
      )
"""
if options.fakest in ["Simulation"]:
 for s in recom_mc_fakes_bkg:
   print ["_".join([reg_prefix.replace("fil","antifil")]+[suffix]).rstrip("_") for suffix in main_addition_regions]
   s.estimator = histmgr.AddRegEstimator(
       hm               = hm, 
       sample           = s,
       data_sample      = data,
       mc_samples       = mc_fakes_bkg, 
       addition_regions = ["_".join([reg_prefix.replace("fil","antifil")]+[suffix]).rstrip("_") for suffix in main_addition_regions]
       )
"""

#-----------------
# Systematics       
#-----------------
# just an example ...
mc_sys = [
    SYS1, 
    SYS2,
    ]

## set mc systematics
#for s in mc_bkg + signals:
#    s.estimator.add_systematics(mc_sys)

#fakes.estimator.add_systematics(FF)

vardict = {}
#vardict  = vars_mumu.vars_dict
vardict.update(vars_tau.vars_dict)
vardict.update(vars_onepair.vars_dict)
#vardict.update(vars_multipairs.vars_dict)


#-----------------
# Plotting 
#-----------------

## order backgrounds for plots
plot_ord_bkg = []

if not options.fakest in [ "NoFakes", "Simulation" ]:
  plot_ord_bkg.append( fakes )

plot_ord_bkg += recom_mc_bkg

#if options.fakest in [ "Simulation" ]:
#  plot_ord_bkg += recom_mc_fakes_bkg



# for overlay studies the configuration is one of these two:
# ----------------------------------------------------------

# overlay shapes from different samples
# -------------------------------------
"""
refsample       = samples.diboson
refregion       = options.region
overlay_samples = [refsample]
overlay_samples += [samples.samples_DCH.Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH300]
overlay_samples += [samples.samples_DCH.Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH700]
overlay_samples += [samples.samples_DCH.Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH1100]
"""


# overlay regions of the same sample
# ----------------------------------
#refsample       = samples.samples_DCH.Pythia8EvtGen_A14NNPDF23LO_AtLeastOneTauFilter_DCH1100
#refregion       = options.region
#overlay_samples = [refsample]

refsample       = samples.dijet
refregion       = options.region
overlay_samples = [refsample]


if options.makeplot == "True":
 funcs.plot_hist(
    backgrounds   = plot_ord_bkg,
    signal        = signals, 
    data          = recom_data,
    #data          = None,
    region        = options.region,
    label         = options.label,
    histname      = os.path.join(vardict[options.vname]['path'],vardict[options.vname]['hname']),
    xmin          = vardict[options.vname]['xmin'],
    xmax          = vardict[options.vname]['xmax'],
    rebin         = vardict[options.vname]['rebin'],
    log           = vardict[options.vname]['log'],
    icut          = ncuts,
    sys_dict      = sys_dict,
    #sys_dict      = None,
    do_ratio_plot = True,
    invert_z      = vardict[options.vname]['invert_z'],
    do_z_plot     = False,
    save_eps      = True,
    plotsfile     = plotsfile,
    #sig_rescale   = "B/S"
    )

elif options.makeplot == "False" and options.makeoverlay=="False":
 funcs.write_hist(
         backgrounds = plot_ord_bkg,
         signal      = signals, # This can be a list
         data        = recom_data,
         #data        = None,
         region      = options.region,
         icut        = ncuts,
         histname    = os.path.join(vardict[options.vname]['path'],vardict[options.vname]['hname']),
         #rebin       = vardict[options.vname]['rebin'],
         rebin       = 1,
         sys_dict    = None,
         renorm      = options.renorm,
         outname     = plotsfile
         )

elif options.makeoverlay == "True":
 funcs.plot_overlay(
    overlay_samples = overlay_samples,
    overlay_regions = options.ovregions, 
    refsample       = refsample,
    refregion       = refregion,
    renorm          = options.renorm,
    label           = options.label,
    histname        = os.path.join(vardict[options.vname]['path'],vardict[options.vname]['hname']),
    xmin            = vardict[options.vname]['xmin'],
    xmax            = vardict[options.vname]['xmax'],
    rebin           = vardict[options.vname]['rebin'],
    log             = vardict[options.vname]['log'],
    anbins          = vardict[options.vname]['anbins'],
    sys_dict        = sys_dict,
    do_ratio_plot   = True,
    log_ratio       = False,
    save_eps        = True,
    plotsfile       = plotsfile,
    )




## EOF



