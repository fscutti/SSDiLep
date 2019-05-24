import os
import ROOT
from array import array


# -------------------------------------------------------------------------------------
# config
# -------------------------------------------------------------------------------------
#indir     = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakesOneTau"
#indir     = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakesTwoTau"
#indir     = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakesSteve"

#indir   = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakesTauTracks"
#indir   = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakesTau3PWin"
#indir   = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakesTau3PWinRed"

indir   = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakesGroupV5"

wp = "Medium"

tauType = "3P%s"%wp


#tag       = "onetau"
#tag       = "twotau"
#tag       = "3P%s"%wp
tag       = "%s_All"%tauType
name      = "data"

# pt 
#var       = "mulead_pt"
var       = "taulead_pt"
#var       = "tausublead_pt"


# muon fakes
#new_bins = array('d', [0.,25.,28.,30.,32.,36.,56.,300.])
#new_bins = array('d', [0.,25.,28.,30.,32.,36.,300.])

# tau fakes (one tau)
#new_bins = array('d', [0.,20.,30.,40.,60.,90.,150.,250.,400.,800.])
new_bins = array('d', [0.,20.,30.,40.,60.,90.,150.,800.])

# tau fakes (two tau)
#new_bins = array('d', [0.,50.,60.,70.,80.,120.,160.,260.,460.,700.])

#new_bins = array('d', [0.]+[50+i*10 for i in xrange(0,60)])


'''
# eta
new_bins = array('d', [-2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5,])
var       = "mulead_eta"
'''

infile    = "hists_"+var+"_FAKES_%s_"+tauType+"_All_F%s_"+tag+".root"
outfile   = "ff_"+var+"_"+name+"_"+tag+"_"+tauType+"_All_F%s_%s.root"
outmerged = "merged_ff_"+var+"_"+name+"_"+tag+"_"+tauType+".root"

# -------------------------------------------------------------------------------------


ROOT.gROOT.SetBatch(True)
rcol = [
   ROOT.kBlack,
   ROOT.kRed,
   ROOT.kYellow+1,
   ROOT.kGreen+2,
   ROOT.kCyan+2,
   ROOT.kGray+1,
   ROOT.kYellow+3,
   ROOT.kMagenta+1,
   ROOT.kAzure+2,
   ROOT.kGreen+1,
   ROOT.kBlue+1,
   ROOT.kRed+3,
   ROOT.kPink+10,
   ]

"""
c_all = ROOT.TCanvas("c_all_ff","c_all_ff",650,600)
c_all.SetTopMargin(0.05)
c_all.SetBottomMargin(0.13)
c_all.SetLeftMargin(0.13)
c_all.SetRightMargin(0.05)
c_all.SetTickx()
c_all.SetTicky()
"""
"""
samples =  [
            "data", 
            "fakes",
            "Wmunu", 
            "Wtaunu", 
            "Zmumu", 
            "Ztautau", 
            "singletop", 
            "ttbar", 
            "diboson",
            ]
"""
samples =  ["fakes"]
#samples =  ["data"]

merged_ff_file = ROOT.TFile.Open(os.path.join(indir,outmerged),"UPDATE")

#for i in [1,10]:
#for i in xrange(1,10):
#for i in xrange(1,2):
for i in [1,2,10,11]:
#for i in xrange(1,12):
  for s in samples:
    num_file = ROOT.TFile.Open(os.path.join(indir,infile%("NUM",i)),"READ")
    den_file = ROOT.TFile.Open(os.path.join(indir,infile%("DEN",i)),"READ")

    h_num_name = "h_FAKES_NUM_"+tauType+"_All_F%s_nominal_%s"%(i,s)
    h_den_name = "h_FAKES_DEN_"+tauType+"_All_F%s_nominal_%s"%(i,s)

    print h_num_name
    print h_den_name


    """
    if i == 10 or i == 11:
     h_num_name = "h_FAKES_NUM_F1_nominal_%s"%(s)
     h_den_name = "h_FAKES_DEN_F1_nominal_%s"%(s)
    """

    h_num = num_file.Get(h_num_name).Clone()
    h_num.SetNameTitle("h_num","h_num")
    h_den = den_file.Get(h_den_name).Clone()
    h_den.SetNameTitle("h_den","h_den")
    
   
    h_new_num = h_num.Rebin(len(new_bins)-1,"h_new_num",new_bins)
    h_new_den = h_den.Rebin(len(new_bins)-1,"h_new_den",new_bins)
    
    print "=="*len(s)
    print s
    print "=="*len(s)
    print
    print "numerator:"
    print h_new_num.Print("all")
    print
    print "denominator:"
    print h_new_den.Print("all")
    print


    h_ff = h_new_num.Clone()
    h_ff.Divide(h_new_den)
   
    h_ff.SetNameTitle("h_ff_"+tauType+"_F%s"%i,"")
    h_ff.GetYaxis().SetTitle("Fake-factor")
    
    h_ff.GetYaxis().SetTitleSize(0.045)
    h_ff.GetXaxis().SetTitleSize(0.045)
    h_ff.GetYaxis().SetLabelSize(0.045)
    h_ff.GetXaxis().SetLabelSize(0.045)
    h_ff.GetYaxis().SetTitleOffset(1.2)
    h_ff.GetXaxis().SetTitleOffset(1.2)
    
    h_ff.GetXaxis().SetRangeUser(min(new_bins),max(new_bins))
    h_ff.SetLineColor(rcol[i-1])
    h_ff.SetMarkerColor(rcol[i-1])
    h_ff.SetMarkerSize(0.01)
    h_ff.SetMaximum(2.0)
    h_ff.SetMinimum(0)
    
    #c_all.cd()
    #if i==1: h_ff.Draw("E1 SAME")
    #else: h_ff.Draw("E1 SAME")
    
    c = ROOT.TCanvas("c_ff_"+tauType+"_F%s"%i,"c_ff_"+tauType+"_F%s"%i,650,600)
    c.SetTopMargin(0.05)
    c.SetBottomMargin(0.13)
    c.SetLeftMargin(0.13)
    c.SetRightMargin(0.05)
    c.SetTickx()
    c.SetTicky()
    c.cd() 
    
    h_ff.SetStats(0)
    h_ff.Draw("E1")
    
    if s=="fakes":
      merged_ff_file.WriteTObject(h_ff.Clone())
      merged_ff_file.WriteTObject(c.Clone())
    
    ff_file = ROOT.TFile.Open(os.path.join(indir,outfile%(i,s)),"RECREATE")
    ff_file.WriteTObject(h_ff.Clone())
    ff_file.WriteTObject(c.Clone())
 
# EOF

