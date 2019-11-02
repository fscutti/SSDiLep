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

#indir   = "/coepp/cephfs/mel/carri/ssdilep/PlotsFFDCH-3p-loose"
indir   = "/coepp/cephfs/mel/fscutti/Analysis/ssdilep/scripts/FakeFactorsMultilepSepTalk"

#wp = "Medium"

#tauType = "3P%s"%wp


#tag       = "onetau"
#tag       = "twotau"
#tag       = "3P%s"%wp
#name      = "data"

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

nprongs = "3P"

'''
# eta
new_bins = array('d', [-2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5,])
var       = "mulead_eta"
'''

#infile    = "hists_"+var+"_FAKES_%s_"+tauType+"_All_F%s_"+tag+".root"
infile    = "hists_"+var+"_%s_inv%s_TrueTauHadFilter_"+nprongs+"_%s_"+nprongs+"_%s.root"
#outfile   = "ff_"+var+"_"+name+"_"+tag+"_"+tauType+"_All_F%s_%s.root"
outfile   = "ff_"+var+"_%s_%s_%s.root"
#outmerged = "merged_ff_"+var+"_"+name+"_"+tag+"_"+tauType+".root"
outmerged = "merged_ff_"+var+".root"

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
#samples =  ["fakes"]
#samples =  ["data"]

merged_ff_file = ROOT.TFile.Open(os.path.join(indir,outmerged),"UPDATE")

#for i in [1,10]:
#for i in xrange(1,10):
#for i in xrange(1,2):
#for i in [1,2,10,11]:
#for i in xrange(1,12):
  #for s in samples:


col = 0
for SR in ["1DF2L", "1DF3L"]:
    for vrCut in ["ANTIZVeto","ANTIPairPt150","ANTImTtot300"]:
        PTPL_file = ROOT.TFile.Open(os.path.join(indir,infile%(SR,vrCut,"PassTau_PassLeps",vrCut)),"READ")
        PTFL_file = ROOT.TFile.Open(os.path.join(indir,infile%(SR,vrCut,"PassTau_FailLeps",vrCut)),"READ")
        FTPL_file = ROOT.TFile.Open(os.path.join(indir,infile%(SR,vrCut,"FailTau_PassLeps",vrCut)),"READ")
        FTFL_file = ROOT.TFile.Open(os.path.join(indir,infile%(SR,vrCut,"FailTau_FailLeps",vrCut)),"READ")
        #num_file = ROOT.TFile.Open(os.path.join(indir,infile%("NUM",i)),"READ")
        #den_file = ROOT.TFile.Open(os.path.join(indir,infile%("DEN",i)),"READ")

        h_PTPL_name = "h_%s_inv%s_TrueTauHadFilter_%s_%s_nominal_fakes"%(SR,vrCut,nprongs,"PassTau_PassLeps")
        h_PTFL_name = "h_%s_inv%s_TrueTauHadFilter_%s_%s_nominal_fakes"%(SR,vrCut,nprongs,"PassTau_FailLeps")
        h_FTPL_name = "h_%s_inv%s_TrueTauHadFilter_%s_%s_nominal_fakes"%(SR,vrCut,nprongs,"FailTau_PassLeps")
        h_FTFL_name = "h_%s_inv%s_TrueTauHadFilter_%s_%s_nominal_fakes"%(SR,vrCut,nprongs,"FailTau_FailLeps")
        #h_num_name = "h_FAKES_NUM_"+tauType+"_All_F%s_nominal_%s"%(i,s)
        #h_den_name = "h_FAKES_DEN_"+tauType+"_All_F%s_nominal_%s"%(i,s)

        #print h_num_name
        #print h_den_name


        """
        if i == 10 or i == 11:
         h_num_name = "h_FAKES_NUM_F1_nominal_%s"%(s)
         h_den_name = "h_FAKES_DEN_F1_nominal_%s"%(s)
        """

        h_PTPL = PTPL_file.Get(h_PTPL_name).Clone()
        h_PTFL = PTFL_file.Get(h_PTFL_name).Clone()
        h_FTPL = FTPL_file.Get(h_FTPL_name).Clone()
        h_FTFL = FTFL_file.Get(h_FTFL_name).Clone()

        h_new_PTPL = h_PTPL.Rebin(len(new_bins)-1,"h_new_PTPL",new_bins)
        h_new_PTFL = h_PTFL.Rebin(len(new_bins)-1,"h_new_PTFL",new_bins)
        h_new_FTPL = h_FTPL.Rebin(len(new_bins)-1,"h_new_FTPL",new_bins)
        h_new_FTFL = h_FTFL.Rebin(len(new_bins)-1,"h_new_FTFL",new_bins)
        
        h_new_num = h_new_PTPL.Clone()
        h_new_num.Add(h_new_PTFL,-1)
        #h_num = num_file.Get(h_num_name).Clone()
        h_new_num.SetNameTitle("h_num","h_num")

        h_new_den = h_new_FTPL.Clone()
        h_new_den.Add(h_new_FTFL,-1)
        #h_den = den_file.Get(h_den_name).Clone()
        h_new_den.SetNameTitle("h_den","h_den")
        
   
        #h_new_num = h_num.Rebin(len(new_bins)-1,"h_new_num",new_bins)
        #h_new_den = h_den.Rebin(len(new_bins)-1,"h_new_den",new_bins)
        
        """
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
        """

        h_ff = h_new_num.Clone()
        h_ff.Divide(h_new_den)
   
        h_ff.SetNameTitle("h_ff_"+var+"_%s_%s"%(SR,vrCut),"")
        #h_ff.SetNameTitle("h_ff_"+tauType+"_F%s"%i,"")
        h_ff.GetYaxis().SetTitle("Fake-factor")
        
        h_ff.GetYaxis().SetTitleSize(0.045)
        h_ff.GetXaxis().SetTitleSize(0.045)
        h_ff.GetYaxis().SetLabelSize(0.045)
        h_ff.GetXaxis().SetLabelSize(0.045)
        h_ff.GetYaxis().SetTitleOffset(1.2)
        h_ff.GetXaxis().SetTitleOffset(1.2)
        
        h_ff.GetXaxis().SetRangeUser(min(new_bins),max(new_bins))
        h_ff.SetLineColor(rcol[col])
        h_ff.SetMarkerColor(rcol[col])
        #col += 1
        h_ff.SetMarkerSize(0.01)

        n_bins = h_ff.GetNbinsX()
        ymax = 0.
        for ibin in xrange(1,n_bins+1):
            y = h_ff.GetBinContent(ibin)
            if ymax < y:
                ymax = 1.2*y

        h_ff.SetMaximum(ymax)
        h_ff.SetMinimum(0)
        
        #c_all.cd()
        #if i==1: h_ff.Draw("E1 SAME")
        #else: h_ff.Draw("E1 SAME")
        
        c = ROOT.TCanvas("c_ff_"+var+"_%s_%s"%(SR,vrCut),"c_ff_"+var+"_%s_%s"%(SR,vrCut),650,600)
        #c = ROOT.TCanvas("c_ff_"+tauType+"_F%s"%i,"c_ff_"+tauType+"_F%s"%i,650,600)
        c.SetTopMargin(0.05)
        c.SetBottomMargin(0.13)
        c.SetLeftMargin(0.13)
        c.SetRightMargin(0.05)
        c.SetTickx()
        c.SetTicky()

        l = ROOT.TLegend(0.7,0.7,0.9,0.9)
        l.SetHeader("%s_%s"%(SR,vrCut))
        l.SetBorderSize(0)

        c.cd() 
        
        h_ff.SetStats(0)
        h_ff.Draw("E1")

        l.Draw()
        c.RedrawAxis()
       
        """
        if s=="fakes":
          merged_ff_file.WriteTObject(h_ff.Clone())
          merged_ff_file.WriteTObject(c.Clone())
        """
        c.SaveAs(os.path.join(indir,c.GetName()+"_%s_%s_%s.eps"%(SR,vrCut,nprongs)))

        ff_file = ROOT.TFile.Open(os.path.join(indir,outfile%(SR,vrCut,nprongs)),"RECREATE")
        ##ff_file = ROOT.TFile.Open(os.path.join(indir,outfile%(i,s)),"RECREATE")
        ff_file.WriteTObject(h_ff.Clone())
        ff_file.WriteTObject(c.Clone())
 
# EOF
    
