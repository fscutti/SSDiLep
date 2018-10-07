import os
import ROOT
from copy import copy

ROOT.gROOT.SetBatch(True)

rcol = [
   ROOT.kRed,
   ROOT.kBlue+1,
   ROOT.kGreen+2,
   ROOT.kYellow+1,
   ROOT.kOrange+7,
   ROOT.kRed+3,
   ROOT.kGray+1,
   ROOT.kYellow+3,
   ROOT.kMagenta+1,
   ROOT.kCyan+2,
   ROOT.kAzure+2,
   ROOT.kPink+10,
   ]

def sep(h1,h2):
  """
  discrimination power: https://arxiv.org/pdf/1405.6583.pdf (pg 6)
  """
  summ = 0.
  for ib in xrange(1,h1.GetNbinsX()):
    num = h1.GetBinContent(ib) - h2.GetBinContent(ib)
    den = h1.GetBinContent(ib) + h2.GetBinContent(ib)
    if den <= 0.: continue
    summ = pow(num,2) / den
  return summ / 2.

# --------------------------
# configure separation tests
# --------------------------
do_KSTest   = True
do_Chi2Test = True
do_SepTest  = True

plotsdir = 'PlotsQGTauTracks'
INPATH   = '/coepp/cephfs/mel/fscutti/ssdilep/'
OUTPATH  = './'
outdir   = plotsdir.replace('Plots','Shapes')
outfile  = outdir.replace('Shapes','study_qg_')

if not os.path.exists(os.path.join(OUTPATH,outdir)):
    os.makedirs(os.path.join(OUTPATH,outdir))

tauvars = []
tauvars.append('taulead_ntracks')
tauvars.append('taulead_trackwidth')
tauvars.append('taulead_angeec0')
tauvars.append('taulead_angeec02')
tauvars.append('taulead_angeec05')
tauvars.append('taulead_angeec1')
tauvars.append('taulead_jetwidth')
tauvars.append('taulead_tracksum')

plotsel = []
plotsel.append('FAKES_QUARKS')
plotsel.append('FAKES_GLUONS')

reg = []
reg.append('F1')
#reg.append('F2')
#reg.append('F3')
#reg.append('F4')
#reg.append('F5')


tag = []
tag.append('incl')

samples = []
samples.append('dijet')
samples.append('Wtaunu')
samples.append('ttbar')

plots = {}

## --------------------------
## configure which feature is 
## to be compared against
## --------------------------
compare = copy(plotsel)


for tv in tauvars:
  for ps in plotsel:
    for rg in reg:
      for tg in tag:
        filename = 'hists_%s_%s_%s_%s'%(tv,ps,rg,tg)
        for sp in samples:
          histname = 'h_%s_%s_nominal_%s'%(ps,rg,sp)
            
          elem = [tv,ps,rg,sp,tg]
          
          for idx, cp in enumerate(compare):
            if cp in filename or cp in histname:
              elem_tmp = copy(elem)
              elem_tmp.remove(cp)
              
              plotname = '_'.join(['plot']+elem_tmp)

              if not plotname in plots: plots[plotname] = []
              f = ROOT.TFile.Open(os.path.join(INPATH,plotsdir,filename+'.root'),'READ')
              h = copy(f.Get(histname))
              
              h.GetYaxis().SetTitle("a.u.")
              h.SetStats(0)
              h.SetNameTitle("_".join(elem),"")
              h.GetYaxis().SetTitleSize(0.045)
              h.GetXaxis().SetTitleSize(0.045)
              h.GetYaxis().SetLabelSize(0.045)
              h.GetXaxis().SetLabelSize(0.045)
              h.GetYaxis().SetTitleOffset(1.25)
              h.GetXaxis().SetTitleOffset(1.25)
              
              h.SetLineColor(rcol[idx])
              h.SetMarkerColor(rcol[idx])
              h.SetLineWidth(4)
              h.SetMarkerSize(0.9)
              #h.SetMaximum(2.0)
              h.SetMinimum(0)
              
              plots[plotname].append(h)


outf = ROOT.TFile.Open(os.path.join(OUTPATH,outdir,outfile+'.root'),"RECREATE")

for plot, hlist in plots.iteritems():
  
  l = ROOT.TLegend(0.56,0.77,0.99,0.9)

  for sp in samples:
    if sp in plot:
      l.SetHeader(sp)
  
  l.SetBorderSize(0)
  l.SetFillColor(0)
  l.SetFillStyle(0)
  
  c = ROOT.TCanvas("c_%s"%plot,"c_%s"%plot,650,600)
  c.SetTopMargin(0.05)
  c.SetBottomMargin(0.13)
  c.SetLeftMargin(0.13)
  c.SetRightMargin(0.05)
  c.SetTickx()
  c.SetTicky()
  
  
  c.cd()
  
  tlatex = ROOT.TLatex()
  tlatex.SetNDC()
  tlatex.SetTextSize(0.036)
  
  tx = 0.66
  ty = 0.6
  th = 0.09
  
  latex_y = ty-2.*th
  
  for h in hlist:
    for cp in compare:
      if cp in h.GetName():
         l.AddEntry(h,cp,"L")
         h.Draw("SAME,E1")
  
  l.Draw()
  
  if do_KSTest: 
    KS_value = hlist[0].KolmogorovTest(hlist[1])
    tlatex.DrawLatex(tx,latex_y,'KS = %lf'%(KS_value) )
    latex_y -= 0.06
  if do_Chi2Test: 
    Chi2_value = hlist[0].Chi2Test(hlist[1],"WW,CHI2/NDF")
    tlatex.DrawLatex(tx,latex_y,'#chi^2/ndf = %lf'%(Chi2_value) )
    latex_y -= 0.06
  if do_SepTest: 
    Sep_value = sep(hlist[0],hlist[1])
    tlatex.DrawLatex(tx,latex_y,'Sum = %lf'%(Sep_value) )
    latex_y -= 0.06
  
  c.SaveAs(os.path.join(OUTPATH,outdir,c.GetName()+'.eps'))
  outf.WriteTObject(c.Clone())


# EOF










































