# encoding: utf-8
'''
tools.py

description:

'''

## modules
import ROOT
from pyplot import histutils
from math import sqrt, log
from decimal import Decimal
from array import array


#import sys_conv


# - - - - - - - - - - - class defs  - - - - - - - - - - - - #




# - - - - - - - - - - function defs - - - - - - - - - - - - #


#____________________________________________________________
def strTobool(s):
  return s=="True"


#____________________________________________________________
def Z(s,b,invert_z=False):
  s_nbins = s.GetNbinsX()
  b_nbins = b.GetNbinsX()
  assert s_nbins == b_nbins, "ERROR: cannot compute Z. Different # bins for sig and bkg"
 
  z = s.Clone()
  z.SetNameTitle(s.GetName()+"_Z",s.GetName()+"_Z")
  
  bins = xrange(1,s_nbins+1)
  if invert_z: bins = list(reversed(bins)) 
  
  for ibin in bins:
    min_int = ibin
    max_int = s_nbins
    if invert_z: 
      min_int = 1
      max_int = ibin
    max_int = ibin
    S = s.Integral(min_int,max_int)
    B = b.Integral(min_int,max_int)
    Z = 0.
    if B>0 and S>0.: 
      arg = ((S+B) * log(1+S/B) - S)
      if  arg > 10e-2:
        Z = sqrt(2 * arg)
    z.SetBinContent(ibin,Z)
  
  return z



#____________________________________________________________
def get_pref_and_suff(region):
  
  if not region:
    return "",""
  
  reg_prefix = region.split("_")[:1]
  reg_suffix = region.split("_")[-1:]
  
  for p,s in zip(reg_prefix,reg_suffix): 
    if p in reg_suffix: reg_suffix.remove(p)
  
  reg_prefix = reg_prefix[0]

  if reg_suffix: reg_suffix = reg_suffix[0]
  else:          reg_suffix = ""

  return reg_prefix,reg_suffix

#____________________________________________________________
def apply_blind(h,blind_min):
    for i in range(1,h.GetNbinsX()+1):
        if h.GetBinLowEdge(i)>=blind_min: 
            h.SetBinContent(i,0.)
            h.SetBinError(i,0.)

#____________________________________________________________
def get_hists(
        region    = None,
        icut      = None,
        histname  = None,
        samples   = None,
        rebin     = None,
        sys_dict  = None,
        ):
    '''
    if sys_dict is passed, hists for all systematics will be appended in a dict. 
    '''
    
    hists = {} 
    for s in samples:
      if not s.hist(region=region,icut=icut,histname=histname): 
        print "Histogram %s not found for %s in region %s ..." % (histname,s.name,region)
        print "continue"
        continue
      h = s.hist(region=region,icut=icut,histname=histname).Clone()
      if rebin and h: h.Rebin(rebin)
      hists[s] = h
      assert h, 'failed to gen hist for %s'%s.name
      h.SetName('h_%s_%s'%(region,s.name))
      
      if sys_dict: 
         h.sys_hists = get_sys_hists(region    = region,
                                     icut      = icut,
                                     histname  = histname,
                                     sample    = s,
                                     rebin     = rebin,
                                     sys_dict  = sys_dict,
                                     )

    for s in samples: s.estimator.flush_hists()
    return hists

#____________________________________________________________
def get_sys_hists(
        region   = None,
        icut     = None,
        histname = None,
        sample   = None,
        rebin    = None,
        sys_dict = None,
        ):
    
    '''
    TODO: put description here
    '''

    hist_dict = {}
    for name,sys in sys_dict.items():
        h_up = h_dn = None
        if sample.estimator.is_affected_by_systematic(sys):
          if not h_up:
            h_up = sample.hist(region=region,icut=icut,histname=histname,sys=sys,mode='up').Clone() 
          else:  h_up.Add(sample.hist(region=region,icut=icut,histname=histname,sys=sys,mode='up').Clone())
          if not h_dn: h_dn = sample.hist(region=region,icut=icut,histname=histname,sys=sys,mode='dn').Clone() 
          else:  h_dn.Add(sample.hist(region=region,icut=icut,histname=histname,sys=sys,mode='dn').Clone())
          h_up.SetName('h_%s_%s_up_%s'%(region,sys.name,sample.name))
          h_dn.SetName('h_%s_%s_dn_%s'%(region,sys.name,sample.name))
          
          if rebin:
           if h_up: h_up.Rebin(rebin)
           if h_dn: h_dn.Rebin(rebin)
             
        hist_dict[sys] = (h_up,h_dn)
    return hist_dict 


#____________________________________________________________
def make_stat_hist(h):
    '''
    makes histogram with fractional bin uncertainty as entries
    ie. new bin content = old bin error/old bin content
    (used for making stat. ratio bands)
    '''
    h_stat = h.Clone('%s_stat'%(h.GetName()))
    for i in range(1,h.GetNbinsX()+1): 
        n = h.GetBinContent(i)
        en = h.GetBinError(i)
        stat = en / n if n else 0.0
        h_stat.SetBinContent(i,stat) 
    return h_stat

#____________________________________________________________
def make_band_graph_from_hist(h_UP,h_DN=None):
    '''
    makes band graph from hist.
    anti-symmetric if h_DN supplied, otherwise symmetric
    '''
    graph = ROOT.TGraphAsymmErrors()
    # added following line
    #graph.GetXaxis().SetRangeUser(h_UP.GetXaxis().GetXmin(),h_UP.GetXaxis().GetXmax()) 
    for i in range(1,h_UP.GetNbinsX()+1):
        eUP = abs(h_UP.GetBinContent(i))
        eDN = abs(h_UP.GetBinContent(i))
        if h_DN: eDN = abs(h_DN.GetBinContent(i))
        ex = h_UP.GetBinWidth(i)/2.
        graph.SetPoint(i-1,h_UP.GetBinCenter(i),1.)
        graph.SetPointError(i-1,ex,ex,eUP,eDN)
    return graph

#____________________________________________________________
def get_total_stat_sys_hists(hists,sys_dict):
    """
    first make total hist for each systematic. 
    then sum deviations in quadrature bin-by-bin to make band.
    """

    ## make total sys hists
    h_total = histutils.add_hists(hists)
    h_total_stat = make_stat_hist(h_total)
    sys_hists_total = {}
    for sys in sys_dict.values():
        hists_up = []
        hists_dn = []
        for h in hists: 
            ## if hist not found, take nominal
            if not h.sys_hists.has_key(sys):
                hists_up.append(h)
                hists_dn.append(h)
            else:
                hists_up.append(h.sys_hists[sys][0] or h)
                hists_dn.append(h.sys_hists[sys][0] or h)

        h_up = histutils.add_hists(hists_up)
        h_dn = histutils.add_hists(hists_dn)
        sys_hists_total[sys] = (h_up,h_dn)

    ## sum bin-by-bin deviations in quadrature
    h_sys_UP = h_total.Clone('%s_sys_UP'%(h_total.GetName()))
    h_sys_DN = h_total.Clone('%s_sys_DN'%(h_total.GetName()))
    h_total_UP = h_total.Clone('%s_total_UP'%(h_total.GetName()))
    h_total_DN = h_total.Clone('%s_total_DN'%(h_total.GetName()))
    for i in range(1,h_total.GetNbinsX()+1):
        n = h_total.GetBinContent(i)
        tot_sys_UP2 = 0.0
        tot_sys_DN2 = 0.0
        for sys in sys_dict.values():
            (h_UP,h_DN) = sys_hists_total[sys]
            n_UP = h_UP.GetBinContent(i)
            n_DN = h_DN.GetBinContent(i)
            v_UP = (n_UP-n)/n if (n_UP!=None and n) else 0.0
            v_DN = (n_DN-n)/n if (n_DN!=None and n) else 0.0

            tot_sys_UP2 += pow(v_UP,2)
            tot_sys_DN2 += pow(v_DN,2)
        tot_sys_UP = sqrt(tot_sys_UP2)            
        tot_sys_DN = sqrt(tot_sys_DN2)            
        h_sys_UP.SetBinContent(i,tot_sys_UP)
        h_sys_DN.SetBinContent(i,tot_sys_DN)
        
        stat = h_total_stat.GetBinContent(i)
        tot_UP = sqrt(pow(tot_sys_UP,2)+pow(stat,2))
        tot_DN = sqrt(pow(tot_sys_DN,2)+pow(stat,2))
        h_total_UP.SetBinContent(i,tot_UP)
        h_total_DN.SetBinContent(i,tot_DN)

    return (h_total_stat,h_sys_UP,h_sys_DN,h_total_UP,h_total_DN)



#____________________________________________________________
def plot_hist( 
    backgrounds   = None,
    signal        = None,   
    data          = None,
    region        = None,
    label         = None,
    icut          = None,
    histname      = None,
    log           = False,
    logx          = False,
    blind         = None,
    xmin          = None,
    xmax          = None,
    rebin         = None,
    sys_dict      = None,
    do_ratio_plot = False,
    invert_z      = False,
    do_z_plot     = False,
    save_eps      = False,
    plotsfile     = None,
    sig_rescale   = None,
    ):
    
    '''
    TODO: 
        * move this to a new module when finished
        * write description for this function

    '''
    print 'making plot: ', histname, ' in region', region
    
    #assert signal, "ERROR: no signal provided for plot_hist"
    assert backgrounds, "ERROR: no background provided for plot_hist"
    
    samples = backgrounds + signal
    
    if data: samples += [data] 

    ## generate nominal hists
    hists = get_hists(
        region=region,
        icut=icut,
        histname=histname,
        samples=samples,
        rebin=rebin,
        sys_dict=sys_dict,
        )
    ## sum nominal background
    h_bkg_list = []
    for b in backgrounds:
      if not b in hists.keys(): continue
      h_bkg_list.append(hists[b])
    
    h_total = histutils.add_hists(h_bkg_list)

    ## get stat / sys bands
    if sys_dict: 
        total_hists = get_total_stat_sys_hists(h_bkg_list,sys_dict)
        
        g_stat = make_band_graph_from_hist(total_hists[0])
        g_stat.SetFillColor(ROOT.kGray+1)
        g_tot  = make_band_graph_from_hist(total_hists[3],total_hists[4])
        g_tot.SetFillColor(ROOT.kRed)

    else:
        h_total_stat = make_stat_hist(h_total)
        g_stat = make_band_graph_from_hist(h_total_stat)
        g_stat.SetFillColor(ROOT.kGray+1)
        g_tot = None

    ## blind data and create ratio 
    h_data  = None
    h_ratio = None
    
    bin_labels = None

    if data: 
        h_data = hists[data]
        if blind: apply_blind(h_data,blind)
        h_ratio = h_data.Clone('%s_ratio'%(h_data.GetName()))
        h_ratio.Divide(h_total)

    yaxistitle = None
    for b in reversed(backgrounds):
      if not b in hists.keys(): continue
      else : 
        yaxistitle = hists[b].GetYaxis().GetTitle()
        if "cutflow" in histname:
          bin_labels = [str(bl) for bl in hists[b].GetXaxis().GetLabels()]
        break
   
    bkg_int = 0

    ## create stack
    h_stack = ROOT.THStack()
    #for s in reversed(signal+backgrounds):
    for b in reversed(backgrounds):
      if not b in hists.keys(): continue
     
      # something is fucky with samples 
      # with no daughters
      hists[b].SetLineColor(b.line_color)
      hists[b].SetFillColor(b.fill_color)
      hists[b].SetMarkerColor(b.marker_color)
      
      bkg_int += hists[b].Integral()

      h_stack.Add(hists[b])
   
    nLegend = len(signal+backgrounds) + 1
    x_legend = 0.63
    x_leg_shift = -0.055
    y_leg_shift = 0.0 
    legYCompr = 8.0
    legYMax = 0.85
    legYMin = legYMax - (legYMax - (0.55 + y_leg_shift)) / legYCompr * nLegend
    legXMin = x_legend + x_leg_shift
    legXMax = legXMin + 0.4
  
    ## create legend (could use metaroot functionality?)
    if not do_ratio_plot or do_z_plot:
      legXMin -= 0.005
      legXMax -= 0.058
    leg = ROOT.TLegend(legXMin,legYMin,legXMax,legYMax)
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    if data: leg.AddEntry(h_data,data.tlatex,'PL')
    
    
    z_plots = []

    if signal:
     for s in signal:
       sig_tag = s.tlatex
       if sig_rescale: sig_tag = "{} x ".format(sig_rescale) + sig_tag
       if not s in hists.keys(): continue
       leg.AddEntry(hists[s],sig_tag,'F')
       
       if do_z_plot:
         z_plots += [Z(hists[s],h_total,invert_z)]

    for b in backgrounds: 
      if not b in hists.keys(): continue
      leg.AddEntry(hists[b],b.tlatex,'F')


    ## create canvas
    reg = region
    if not reg: reg = ""
    name = '_'.join([reg,histname]).replace('/','_') 
    cname = "c_final_%s"%name
    if do_ratio_plot or do_z_plot: c = ROOT.TCanvas(cname,cname,800,800)
    else: c = ROOT.TCanvas(cname,cname,800,800)
    if xmin==None: xmin = h_total.GetBinLowEdge(1)
    if xmax==None: xmax = h_total.GetBinLowEdge(h_total.GetNbinsX()+1)
    ymin = 1.e-3
    ymax = h_total.GetMaximum()
    for b in backgrounds:
      if not b in hists.keys(): continue
      ymax = max([ymax,hists[b].GetMaximum()])
    if data: ymax = max([ymax,h_data.GetMaximum()])
    if log: ymax *= 100000.
    else:   ymax *= 1.8
    xtitle = h_total.GetXaxis().GetTitle()

    if do_ratio_plot or do_z_plot: rsplit = 0.3
    else: rsplit = 0.
    pad1 = ROOT.TPad("pad1","top pad",0.,rsplit,1.,1.)
    pad1.SetLeftMargin(0.15)
    pad1.SetTicky()
    pad1.SetTickx()
    if do_ratio_plot or do_z_plot: pad1.SetBottomMargin(0.04)
    else: pad1.SetBottomMargin(0.15)

    pad1.Draw()
    if do_ratio_plot or do_z_plot:
      pad2 = ROOT.TPad("pad2","bottom pad",0,0,1,rsplit)
      pad2.SetTopMargin(0.04)
      pad2.SetBottomMargin(0.40)
      pad2.SetLeftMargin(0.15)
      pad2.SetTicky()
      pad2.SetTickx()
      pad2.SetGridy()
    #if do_ratio_plot: pad2.Draw()
      pad2.Draw()
    pad1.cd()

    ytitle = "Events" 
    if not rebin: ytitle = yaxistitle
    elif rebin!=1 and "GeV" in xtitle:
      ytitle += " / %s GeV"%rebin

    fr1 = pad1.DrawFrame(xmin,ymin,xmax,ymax,';%s;%s'%(xtitle,ytitle))
    
    if do_ratio_plot or do_z_plot:
      fr1.GetXaxis().SetTitleSize(0)
      fr1.GetXaxis().SetLabelSize(0)
    xaxis1 = fr1.GetXaxis()
    yaxis1 = fr1.GetYaxis()
    scale = (1.3+rsplit)

    if not do_ratio_plot or do_z_plot:
      xaxis1.SetTitleSize( xaxis1.GetTitleSize() * scale )
      xaxis1.SetLabelSize( 0.9 * xaxis1.GetLabelSize() * scale )
      xaxis1.SetTickLength( xaxis1.GetTickLength() * scale )
      xaxis1.SetTitleOffset( 1.3* xaxis1.GetTitleOffset() / scale  )
      xaxis1.SetLabelOffset( 1.* xaxis1.GetLabelOffset() / scale )

    yaxis1.SetTitleSize( yaxis1.GetTitleSize() * scale )
    yaxis1.SetTitleOffset( 2.1 * yaxis1.GetTitleOffset() / scale )
    yaxis1.SetLabelSize( 0.8 * yaxis1.GetLabelSize() * scale )
    yaxis1.SetLabelOffset( 1. * yaxis1.GetLabelOffset() / scale )
    xaxis1.SetNdivisions(510)
    yaxis1.SetNdivisions(510)

    
    if bin_labels:
      width = int(fr1.GetNbinsX() / len(bin_labels))
      for ibin, binlabel in enumerate(bin_labels):
        fr1.GetXaxis().SetBinLabel(ibin * width + int(width / 2), binlabel)
      xaxis1.SetTickLength( 0 )
      xaxis1.LabelsOption( "hd" )

    h_stack.Draw("SAME,HIST")

    if signal:
     for s in reversed(signal):
       if not s in hists.keys(): continue
       if sig_rescale=="B/S": 
         sig_int = hists[s].Integral()
         hists[s].Scale(bkg_int / sig_int)
         print hists[s].Integral()
       hists[s].Draw("SAME,HIST")

    if data: 
      h_data.Draw("SAME")
    pad1.SetLogy(log)
    pad1.SetLogx(logx)
    
    if do_z_plot:
      pad1.SetLogy(True)
      pad2.SetLogy(True)

    leg.Draw()
    pad1.RedrawAxis()

    tlatex = ROOT.TLatex()
    tlatex.SetNDC()
    tlatex.SetTextSize(0.05)
    lx = 0.6 # for ATLAS internal
    ly = 0.845
    tlatex.SetTextFont(42)
    
    ty = 0.96
    th = 0.07
    tx = 0.18
    lumi = backgrounds[0].estimator.hm.target_lumi/1000.
    textsize = 0.8
    if not do_ratio_plot or not do_z_plot: textsize = 0.8
    latex_y = ty-2.*th
    tlatex.DrawLatex(tx,latex_y,'#scale[%lf]{#scale[%lf]{#int}L dt = %2.1f fb^{-1}, #sqrt{s} = 13 TeV}'%(textsize,0.8*textsize,140.5) )
    if label:
      latex_y -= 0.06
      #for i,line in enumerate(label):
      #  tlatex.DrawLatex(tx,latex_y-i*0.06,"#scale[%lf]{%s}"%(textsize,line))
      tlatex.DrawLatex(tx,latex_y - 0.06,"#scale[%lf]{%s}"%(textsize,label))
    if blind:
        line = ROOT.TLine()
        line.SetLineColor(ROOT.kBlack)
        line.SetLineStyle(2)
        line.DrawLine(blind,ymin,blind,ymax)
        bltext = ROOT.TLatex()
        bltext.SetTextFont(42)
        bltext.SetTextSize(0.04)
        bltext.SetTextAngle(90.)
        bltext.SetTextAlign(31)
        bltext.DrawLatex(blind,ymax, 'Blind   ')

    if do_ratio_plot or do_z_plot:
      pad2.cd()
      ymin2 = 0.49
      ymax2 = 1.51
      if do_z_plot:
        ymin2 = 0.1
        ymax2 = 100.
      yaxis2title = "Data / Bkg_{SM}"
      if do_z_plot: yaxis2title = "Z"
      fr2 = pad2.DrawFrame(xmin,ymin2,xmax,ymax2,';%s;%s'%(xtitle,yaxis2title))
      xaxis2 = fr2.GetXaxis()
      yaxis2 = fr2.GetYaxis()
      #scale = (1. / rsplit)
      
      yaxis2.SetTitleSize( 1.9 * yaxis2.GetTitleSize() * scale )
      yaxis2.SetLabelSize( 1.9 * yaxis2.GetLabelSize() * scale )
      #yaxis2.SetTitleOffset( 0.005 * yaxis2.GetTitleOffset() / scale  )
      yaxis2.SetTitleOffset( 0.65 )
      yaxis2.SetLabelOffset( 1.9 * yaxis1.GetLabelOffset() / scale )
      
      xaxis2.SetTitleSize( 1.9 * xaxis2.GetTitleSize() * scale )
      xaxis2.SetLabelSize( 1.9 * xaxis2.GetLabelSize() * scale )
      xaxis2.SetTickLength( xaxis2.GetTickLength() * scale )
      xaxis2.SetTitleOffset( 2.0* xaxis2.GetTitleOffset() / scale  )
      xaxis2.SetLabelOffset( 2.1* xaxis2.GetLabelOffset() / scale )
      if "cutflow" in histname: 
        xaxis2.SetLabelOffset( 1.5 * xaxis2.GetLabelOffset() )
      if do_z_plot: yaxis2.SetNdivisions(505)
      else: yaxis2.SetNdivisions(510)
      xaxis2.SetNdivisions(510)


      if bin_labels:
        width = int(fr2.GetNbinsX() / len(bin_labels))
        for ibin, binlabel in enumerate(bin_labels):
          fr2.GetXaxis().SetBinLabel(ibin * width + int(width / 2), binlabel)
        xaxis2.SetTickLength( 0 )
        xaxis2.LabelsOption( "hd" )


      if logx: 
        pad2.SetLogx(logx) 
        xaxis2.SetMoreLogLabels()
      else: 
        pass
      
      if not do_z_plot: 
        if g_tot: 
           g_tot.Draw("E2")
           g_stat.Draw("SAME,E2")
        
        else: g_stat.Draw("E2")

      if data and not do_z_plot: h_ratio.Draw("SAME") 
      
      if signal and do_z_plot and not do_ratio_plot:
        for z in z_plots: z.Draw("SAME")
      
      pad2.RedrawAxis()

    print 'saving plot...'
    if save_eps:
     eps_file = plotsfile.replace(".root",".eps")
     if not log: c.SaveAs(eps_file)
     else: c.SaveAs(eps_file.replace(".eps","_LOG.eps"))
    
    fout = ROOT.TFile.Open(plotsfile,'UPDATE')
    fout.WriteTObject(c)
    fout.Close()

#____________________________________________________________
def write_hist(
        backgrounds = None,
        signal      = None,
        data        = None,
        region      = None,
        icut        = None,
        histname    = None,
        rebin       = None,
        renorm      = None,
        sys_dict    = None,
        outname     = None,
        ):
    """
    write hists for backgrounds, signals and data to file.
    will also write sys hists if sys_dict passed. 
    also write smtot hists for summed background.
    No folder structure is provided
    """
    samples = backgrounds + signal
    if data: samples += [data]
    ## generate nominal hists
    hists = get_hists(
        region=region,
        icut=icut,
        histname=histname,
        samples=samples, 
        rebin=rebin,
        sys_dict=sys_dict,
        )

    #histnamestr = histname.replace('/','_')
    fname = outname
    fout = ROOT.TFile.Open(fname,'RECREATE')
    for s,h in hists.items():
        hname = 'h_%s_nominal_%s' % (region,s.name)
        h.SetNameTitle(hname,hname)
        
        if strTobool(renorm): h.Scale(1./h.Integral())
        
        fout.WriteTObject(h,hname)
        ## systematics
        if hasattr(h,'sys_hists'):
         if sys_dict:
            for sys,hsys in h.sys_hists.items():
                
                s_name = sys.name

                hname_sys_up = hname.replace('nominal','%s_%s' % (s_name,'UP'))
                hname_sys_dn = hname.replace('nominal','%s_%s' % (s_name,'DN'))

                if hsys[0]: hsys[0].SetNameTitle(hname_sys_up,hname_sys_up)
                if hsys[1]: hsys[1].SetNameTitle(hname_sys_dn,hname_sys_dn)
                fout.WriteTObject(hsys[0],hname_sys_up)
                fout.WriteTObject(hsys[1],hname_sys_dn)

    ## create total background hists
    #h_total = histutils.add_hists([ hists[s] for s in backgrounds ])
    #fout.WriteTObject(h_total,'h_%s_nominal_smtot'%region)
    
    fout.Close()


#____________________________________________________________
def plot_overlay( 
    overlay_samples = None,
    overlay_regions = None,
    refsample       = None,
    refregion       = None,
    renorm          = None,
    label           = None,
    histname        = None,
    log             = False,
    logx            = False,
    xmin            = None,
    xmax            = None,
    rebin           = None,
    anbins          = None,
    sys_dict        = None,
    do_ratio_plot   = False,
    log_ratio       = False,
    save_eps        = False,
    plotsfile       = None,
    ):
    print '\nOnly supports MC atm\n' 
    print 'Making overlays of regions:\n%s '%("  ".join(overlay_regions.split(";")))
    print 'Samples: %s\n' % " ".join([x.name for x in overlay_samples])

    samples = overlay_samples

    ovregions = {}
    for r in overlay_regions.split(";"):
      ovregions[r.split(":")[0]] = int(r.split(":")[1])

    ovhists = {}
    for region,icut in ovregions.iteritems():
      ovhists[region] = get_hists(
          region   = region,
          icut     = icut,
          histname = histname,
          samples  = samples,
          rebin    = rebin,
          sys_dict = sys_dict,
          )
    
    h_ratios = []
    h_hists  = []
    
    yaxistitle = None
    xtitle = None

    ymin = ymax = 1.e-3
   
    basic_colors = [ROOT.kRed,ROOT.kBlue,ROOT.kGreen,ROOT.kYellow,ROOT.kMagenta,ROOT.kCyan]
    colors = []
    for shade in xrange(4):
      for c in basic_colors: colors.append(c+shade)
    
    iter_colors = iter(colors)

    for s in samples:
      for r in ovregions.keys():
        hden = ovhists[refregion][refsample]
        xtitle = hden.GetXaxis().GetTitle()
        hnum = ovhists[r][s]

        if strTobool(renorm):
          hnum.Scale(1./hnum.Integral())
          hden.Scale(1./hden.Integral())

        hratio = hnum.Clone()
        yaxistitle = hnum.GetYaxis().GetTitle()
        hratio.SetName('%s_%s_ratio'%(hnum.GetName(),hden.GetName()))
        hratio.Divide(hden)

        # set style
        
        color = ROOT.kBlack
        if not (s==refsample and r==refregion): 
          
          if len(ovregions.keys())>1:  color = next(iter_colors)
          elif len(overlay_samples)>1: 
            if hasattr(s,"line_color"): 
              color = s.line_color

        hnum.SetLineColor(color)
        hratio.SetLineColor(color)
        
        hnum.SetFillColor(color)
        hratio.SetFillColor(color)

        hnum.SetMarkerColor(color)
        hratio.SetMarkerColor(color)

        hnum.SetFillStyle(0)
        hratio.SetFillStyle(0)

        hnum.SetLineWidth(2)
        hratio.SetLineWidth(2)

        if xmin==None: xmin = hden.GetBinLowEdge(1)
        if xmax==None: xmax = hden.GetBinLowEdge(hnum.GetNbinsX()+1)
        
        ymax = max([ymax,hden.GetMaximum()])

        h_ratios.append(hratio)
    
    nLegend = len(samples+ovregions.keys()) - 1
    x_legend    = 0.74
    x_leg_shift = -0.12
    y_leg_shift = 0.0 
    legYCompr   = 4.5
    legYMax     = 0.9
    legYMin     = legYMax - (legYMax - (0.55 + y_leg_shift)) / legYCompr * nLegend
    legXMin     = x_legend + x_leg_shift
    legXMax     = legXMin + 0.4
  
    ## create legend (could use metaroot functionality?)
    if not do_ratio_plot==True:
      legXMin -= 0.005
      legXMax -= 0.058
    leg = ROOT.TLegend(legXMin,legYMin,legXMax,legYMax)
    leg.SetBorderSize(0)
    leg.SetMargin(0.08)
    leg_head = ""
    if len(ovregions.keys())>1: 
      leg_head += refsample.tlatex
    elif len(overlay_samples)>1: 
      leg_head += refregion
    if strTobool(renorm):
      leg_head += " (unit area)"
    leg.SetHeader(leg_head)
    leg.SetTextFont(42)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    
    #if data: leg.AddEntry(h_data,data.tlatex,'PL')
    for s in samples:
      for r in ovregions.keys():
        #if r==refregion and s==refsample: continue
        if len(ovregions.keys())>1: leg.AddEntry(ovhists[r][s],r,'L')
        elif len(overlay_samples)>1: leg.AddEntry(ovhists[r][s],s.tlatex,'L')

    ## create canvas
    reg = region
    if not reg: reg = ""
    cname = "c_%s"%(plotsfile.strip(".root")).split("/")[-1]
    if do_ratio_plot: c = ROOT.TCanvas(cname,cname,800,600)
    else: c = ROOT.TCanvas(cname,cname,800,700)
    
    if log: ymax *= 100000.
    else:   ymax *= 1.8

    if do_ratio_plot: rsplit = 0.3
    else: rsplit = 0.
    pad1 = ROOT.TPad("pad1","top pad",0.,rsplit,1.,1.)
    pad1.SetLeftMargin(0.08)
    pad1.SetRightMargin(0.4)
    pad1.SetTicky()
    pad1.SetTickx()
    if anbins: pad1.SetGridx()
    if do_ratio_plot: pad1.SetBottomMargin(0.04)
    else: pad1.SetBottomMargin(0.15)

    pad1.Draw()
    if do_ratio_plot:
      pad2 = ROOT.TPad("pad2","bottom pad",0,0,1,rsplit)
      pad2.SetTopMargin(0.04)
      pad2.SetBottomMargin(0.40)
      pad2.SetLeftMargin(0.08)
      pad2.SetRightMargin(0.4)
      pad2.SetTicky()
      pad2.SetTickx()
      pad2.SetGridy()
      if anbins: pad2.SetGridx()
      pad2.Draw()
    pad1.cd()

    ytitle = "Events" 
    if not rebin: ytitle = yaxistitle
    elif rebin!=1 and "GeV" in xtitle:
      ytitle += " / %s GeV"%rebin

    fr1 = pad1.DrawFrame(xmin,ymin,xmax,ymax,';%s;%s'%(xtitle,ytitle))
   
    
    if do_ratio_plot:
      fr1.GetXaxis().SetTitleSize(0)
      fr1.GetXaxis().SetLabelSize(0)
    xaxis1 = fr1.GetXaxis()
    yaxis1 = fr1.GetYaxis()
    
    scale = (1.3+rsplit)
    
    if not do_ratio_plot:
      xaxis1.SetTitleSize( xaxis1.GetTitleSize() * scale )
      xaxis1.SetLabelSize( 0.9 * xaxis1.GetLabelSize() * scale )
      xaxis1.SetTickLength( xaxis1.GetTickLength() * scale )
      xaxis1.SetTitleOffset( 1.3* xaxis1.GetTitleOffset() / scale  )
      xaxis1.SetLabelOffset( 1.* xaxis1.GetLabelOffset() / scale )

    
    yaxis1.SetTitleSize( yaxis1.GetTitleSize() * scale )
    #yaxis1.SetTitleOffset( 2.1 * yaxis1.GetTitleOffset() / scale )
    yaxis1.SetTitleOffset( 0.6 )
    yaxis1.SetLabelSize( 0.8 * yaxis1.GetLabelSize() * scale )
    yaxis1.SetLabelOffset( 1. * yaxis1.GetLabelOffset() / scale )
    xaxis1.SetNdivisions(510)
    yaxis1.SetNdivisions(510)

    if anbins:
      width = int(fr1.GetNbinsX() / len(anbins))
      for ibin, binlabel in enumerate(anbins):
        fr1.GetXaxis().SetBinLabel(ibin * width + int(width / 2), binlabel)
      xaxis1.SetTickLength( 0 )
      xaxis1.LabelsOption( "hd" )

    for s in samples:
      for r in ovregions.keys():
        ovhists[r][s].Draw("SAME")
    
    
    pad1.SetLogy(log)
    pad1.SetLogx(logx)
    leg.Draw()
    pad1.RedrawAxis()

    tlatex = ROOT.TLatex()
    tlatex.SetNDC()
    tlatex.SetTextSize(0.05)
    lx = 0.6 # for ATLAS internal
    ly = 0.845
    tlatex.SetTextFont(42)
    
    ty = 0.96
    th = 0.07
    tx = 0.18
    lumi = samples[0].estimator.hm.target_lumi/1000.
    textsize = 0.8
    if not do_ratio_plot: textsize = 0.8
    latex_y = ty-2.*th
    tlatex.DrawLatex(tx,latex_y,'#scale[%lf]{#scale[%lf]{#int}L dt = %2.1f fb^{-1}, #sqrt{s} = 13 TeV}'%(textsize,0.8*textsize,140.5) )
    if label:
      latex_y -= 0.06
      #for i,line in enumerate(label):
      #  tlatex.DrawLatex(tx,latex_y-i*0.06,"#scale[%lf]{%s}"%(textsize,line))
      tlatex.DrawLatex(tx,latex_y - 0.06,"#scale[%lf]{%s}"%(textsize,label))
    
    if do_ratio_plot:
      pad2.cd()
      ymin = 0.2
      ymax = 1.8
      
      if log_ratio:
        ymax *= 10
        ymin /= 100
      fr2 = pad2.DrawFrame(xmin,ymin,xmax,ymax,';%s; ratio'%(xtitle))
      
      xaxis2 = fr2.GetXaxis()
      yaxis2 = fr2.GetYaxis()
      
      scale = (1. / rsplit)
      
      yaxis2.SetTitleSize( yaxis2.GetTitleSize() * scale )
      yaxis2.SetLabelSize( 0.6 * yaxis2.GetLabelSize() * scale )
      #yaxis2.SetTitleOffset( 2.1* yaxis2.GetTitleOffset() / scale  )
      yaxis2.SetTitleOffset( 0.35 )
      yaxis2.SetLabelOffset(0.4 * yaxis2.GetLabelOffset() * scale )
      xaxis2.SetTitleSize( xaxis2.GetTitleSize() * scale )
      xaxis2.SetLabelSize( 0.8 * xaxis2.GetLabelSize() * scale )
      xaxis2.SetTickLength( xaxis2.GetTickLength() * scale )
      xaxis2.SetTitleOffset( 3.2* xaxis2.GetTitleOffset() / scale  )
      xaxis2.SetLabelOffset( 2.5* xaxis2.GetLabelOffset() / scale )
      yaxis2.SetNdivisions(510)
      xaxis2.SetNdivisions(510)
     
      if anbins:
        width = int(fr2.GetNbinsX() / len(anbins))
        for ibin, binlabel in enumerate(anbins):
          fr2.GetXaxis().SetBinLabel(ibin * width + int(width / 2), binlabel)
        xaxis2.SetTickLength( 0 )
        xaxis2.LabelsOption( "hd" )

      if log_ratio:
        pad2.SetLogy(log_ratio)
      
      if logx: 
        pad2.SetLogx(logx) 
        xaxis2.SetMoreLogLabels()
      
      else: 
        pass

      if h_ratios:
        for hr in h_ratios:
          hr.Draw("SAME,HIST")

      pad2.RedrawAxis()

    print 'saving plot...'

    if save_eps:
     eps_file = plotsfile.replace(".root",".eps")
     if not log: c.SaveAs(eps_file)
     else: c.SaveAs(eps_file.replace(".eps","_LOG.eps"))

    fout = ROOT.TFile.Open(plotsfile,'UPDATE')
    fout.WriteTObject(c)
    fout.Close()


def list_open_files():
    l = ROOT.gROOT.GetListOfFiles()
    itr = l.MakeIterator()
    obj = itr.Next()
    while obj:
        print obj.GetName()
        obj = itr.Next()


## EOF
