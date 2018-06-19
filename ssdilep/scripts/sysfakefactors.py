import os
import ROOT
from array import array

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0000)

# -------------------------------------------------------------------------------------
# config
# -------------------------------------------------------------------------------------
#indir   = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakesOneTau"

indir   = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakesTau1PRevThr"
#indir   = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakesTau3PWin"
#indir   = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakesTau3PWinRed"

tag     = "1prong"
#tag     = "final"
name    = "data"

# pt
#var     = "mulead_pt"
var     = "taulead_pt"
#var     = "tausublead_pt"

#axislab = "p_{T}(#mu_{lead}) [GeV]"
axislab = "p_{T}(#tau_{lead}) [GeV]"
#axislab = "p_{T}(#tau_{sublead}) [GeV]"

# muon fakes
#new_bins = array('d', [0.,25.,28.,30.,32.,36.,300.])

# tau fakes (one tau)


new_bins = array('d', [0.,20.,30.,40.,60.,90.,150.,250.,400.,800.])

# tau fakes (two tau)
#new_bins = array('d', [0.,50.,60.,70.,80.,120.,160.,260.,460.,700.])


'''
# eta
var     = "mulead_eta"
axislab = "#eta(#mu_{lead})"
new_bins = array('d', [-2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5,])
'''


infile  = "merged_ff_"+var+"_"+name+"_"+tag+".root"
outfile = "sys_ff_"+var+"_"+name+"_"+tag+".root"
inf     = ROOT.TFile.Open(os.path.join(indir,infile),"READ")


# -------------------------------------------------------------------------------------

hdict = {}

hdict["NOM"] = inf.Get("h_ff_F1").Clone()
n_bins = hdict["NOM"].GetNbinsX()
for i in [2,3,4,5,6,7,8,9,]: 
  hdict["SYS%s"%str(i)] = inf.Get("h_ff_F%s"%str(i)).Clone()

slabel = {}

# --------------
# muon FF labels
# --------------
"""
slabel["NOM"]  = "nominal"
#slabel["SYS1"] = "nominal"

slabel["SYS2"] = "E^{miss}_{T} < 50 GeV"
slabel["SYS3"] = "E^{miss}_{T} < 30 GeV"
slabel["SYS4"] = "#Delta#phi(#mu,jet) > 2.9"
slabel["SYS5"] = "#Delta#phi(#mu,jet) > 2.5"
slabel["SYS6"] = "d_{0}/#sigma(d_{0}) < 2"
slabel["SYS7"] = "d_{0}/#sigma(d_{0}) < 4"
slabel["SYS8"] = "p_{T}(jet) > 40 GeV"
slabel["SYS9"] = "One b-jet"
#slabel["SYS10"] = "MC + 30%"
#slabel["SYS11"] = "MC - 30%"
"""

# --------------
# one tau FF labels
# --------------
#"""
slabel["NOM"]  = "tau+jet"

slabel["SYS2"] = "p_{T}(jet) > 50 GeV"
slabel["SYS3"] = "E^{miss}_{T} < 40 GeV"
slabel["SYS4"] = "No #Delta#phi(#tau,jet) cut"
slabel["SYS5"] = "N_{jet}>0"
slabel["SYS6"] = "N_{jet}>1"
slabel["SYS7"] = "N_{jet}>2"
slabel["SYS8"] = "One b-jet"
slabel["SYS9"] = "Veto b-jet"
#"""

# --------------
# two tau FF labels
# --------------
"""
slabel["NOM"]  = "two SS taus + jet"
slabel["SYS2"] = "two OS taus + jet"
slabel["SYS3"] = "two SS taus (no back to back)"
slabel["SYS4"] = "p_{T}(#tau_{lead}) > 170 GeV"
slabel["SYS5"] = "two SS taus ptratio>0.3"
slabel["SYS6"] = "two SS taus ptratio>0.3 p_{T}(#tau_{lead}) > 170 GeV"
slabel["SYS7"] = "two SS taus ptratio>0.3 p_{T}(#tau_{lead}) > 170 GeV N_{jet}>0"
slabel["SYS8"] = "two SS taus ptratio>0.3 p_{T}(#tau_{lead}) > 170 GeV N_{jet}>1"
slabel["SYS9"] = "two SS taus ptratio>0.3 p_{T}(#tau_{lead}) > 170 GeV N_{jet}>2"
"""

g_sys_ff = ROOT.TGraphAsymmErrors(n_bins)
g_nom_ff = ROOT.TGraphAsymmErrors(n_bins)


for ibin in xrange(1,n_bins+1):
    g_sys_ff.SetPoint(ibin,hdict["NOM"].GetBinCenter(ibin),hdict["NOM"].GetBinContent(ibin))  
    g_nom_ff.SetPoint(ibin,hdict["NOM"].GetBinCenter(ibin),hdict["NOM"].GetBinContent(ibin))  

    g_sys_ff.SetPointEYlow(ibin, hdict["NOM"].GetBinErrorLow(ibin))
    g_sys_ff.SetPointEYhigh(ibin, hdict["NOM"].GetBinErrorUp(ibin))
    
    g_nom_ff.SetPointEYlow(ibin, hdict["NOM"].GetBinErrorLow(ibin))
    g_nom_ff.SetPointEYhigh(ibin, hdict["NOM"].GetBinErrorUp(ibin))

    g_sys_ff.SetPointEXlow(ibin, hdict["NOM"].GetBinWidth(ibin)/2.)
    g_sys_ff.SetPointEXhigh(ibin, hdict["NOM"].GetBinWidth(ibin)/2.)
    
    g_nom_ff.SetPointEXlow(ibin, hdict["NOM"].GetBinWidth(ibin)/2.)
    g_nom_ff.SetPointEXhigh(ibin, hdict["NOM"].GetBinWidth(ibin)/2.)

g_nom_ff.SetNameTitle("g_ff_stat","")
g_sys_ff.SetNameTitle("g_ff_stat_sys","")

for sys,hist in hdict.iteritems():
  if sys == "NOM": continue
  for ibin in xrange(1,n_bins+1):
    
    nom_minus_sys = hdict["NOM"].GetBinContent(ibin)-hdict[sys].GetBinContent(ibin)
    
    if nom_minus_sys>0. and nom_minus_sys > hdict[sys].GetBinErrorUp(ibin):
     g_sys_ff.SetPointEYlow(ibin, max(g_sys_ff.GetErrorYlow(ibin),abs(nom_minus_sys)))

    if nom_minus_sys<0. and abs(nom_minus_sys) > hdict[sys].GetBinErrorLow(ibin):
     g_sys_ff.SetPointEYhigh(ibin, max(g_sys_ff.GetErrorYhigh(ibin),abs(nom_minus_sys)))
    
c = ROOT.TCanvas("c_ff","c_ff",650,600)
c.SetTopMargin(0.05)
c.SetBottomMargin(0.13)
c.SetLeftMargin(0.13)
c.SetRightMargin(0.05)
c.SetTickx()
c.SetTicky()

l = ROOT.TLegend(0.15,0.65,0.55,0.9)
l.SetBorderSize(0)
l.SetFillColor(0)
l.SetFillStyle(0)


g_sys_ff.GetYaxis().SetTitle("Fake-factor")
g_sys_ff.GetXaxis().SetTitle(axislab)
g_sys_ff.GetYaxis().SetTitleSize(0.045)
g_sys_ff.GetXaxis().SetTitleSize(0.045)
g_sys_ff.GetYaxis().SetLabelSize(0.045)
g_sys_ff.GetXaxis().SetLabelSize(0.045)
g_sys_ff.GetYaxis().SetTitleOffset(1.2)
g_sys_ff.GetXaxis().SetTitleOffset(1.2)
g_sys_ff.GetXaxis().SetRangeUser(min(new_bins),max(new_bins))
g_sys_ff.SetLineColor(ROOT.kYellow)
g_sys_ff.SetMarkerColor(ROOT.kBlack)
g_sys_ff.SetFillColor(ROOT.kYellow)
g_sys_ff.SetMarkerSize(1.3)
#g_sys_ff.SetMaximum(2.0) # for muons
g_sys_ff.SetMaximum(1.0)  # for taus
g_sys_ff.SetMinimum(0)

g_nom_ff.GetYaxis().SetTitle("Fake-factor")
g_nom_ff.GetXaxis().SetTitle(axislab)
g_nom_ff.GetYaxis().SetTitleSize(0.045)
g_nom_ff.GetXaxis().SetTitleSize(0.045)
g_nom_ff.GetYaxis().SetLabelSize(0.045)
g_nom_ff.GetXaxis().SetLabelSize(0.045)
g_nom_ff.GetYaxis().SetTitleOffset(1.2)
g_nom_ff.GetXaxis().SetTitleOffset(1.2)
g_nom_ff.GetXaxis().SetRangeUser(min(new_bins),max(new_bins))
g_nom_ff.SetLineColor(ROOT.kBlack)
g_nom_ff.SetLineWidth(2)
g_nom_ff.SetMarkerColor(ROOT.kBlack)
g_nom_ff.SetMarkerStyle(20)
g_nom_ff.SetMarkerSize(0.9)
#g_nom_ff.SetMaximum(2.0)   # for muons
g_nom_ff.SetMaximum(1.0)   # for taus
g_nom_ff.SetMinimum(0)

c.cd() 

g_sys_ff.Draw("APE2")
g_nom_ff.Draw("SAME,P")
l.SetHeader("Nominal Fake-factor")
l.AddEntry(g_sys_ff,"stat.+sys.","F")
l.AddEntry(g_nom_ff,"stat.","PL")
l.Draw()
c.RedrawAxis()

c2 = ROOT.TCanvas("c_sys","c_sys",650,600)
c2.SetTopMargin(0.05)
c2.SetBottomMargin(0.13)
c2.SetLeftMargin(0.13)
c2.SetRightMargin(0.05)
c2.SetTickx()
c2.SetTicky()

l2 = ROOT.TLegend(0.15,0.5,0.45,0.9)
l2.SetBorderSize(0)
l2.SetFillColor(0)
l2.SetFillStyle(0)

c2.cd()

hdict["NOM"].SetStats(0)
hdict["NOM"].SetLineWidth(2)
hdict["NOM"].Draw()
#l2.SetHeader("Systematics")  # for muons
l2.SetHeader("N_{tracks}=1")  # for one taus
#l2.SetHeader("N_{tracks}=3")  # for one taus
#l2.SetHeader("N_{#tau}=2")  # for two taus

#l2.AddEntry(hdict["NOM"],"nominal","PL")
l2.AddEntry(hdict["NOM"],"tau+jet","PL")
#l2.AddEntry(hdict["NOM"],"two SS taus + jet","PL")

for sys,hist in hdict.iteritems():
    if sys == "NOM": continue
    hist.Draw("SAME,E1")
    l2.AddEntry(hist,slabel[sys],"PL")

hdict["NOM"].Draw("SAME,PE1")

l2.Draw()

c.SaveAs(os.path.join(indir,c.GetName()+"_%s.eps"%tag))
c2.SaveAs(os.path.join(indir,c2.GetName()+"_%s.eps"%tag))

outfile = ROOT.TFile.Open(os.path.join(indir,outfile),"RECREATE")

outfile.WriteTObject(g_sys_ff)
outfile.WriteTObject(g_nom_ff)
outfile.WriteTObject(c)
outfile.WriteTObject(c2)

