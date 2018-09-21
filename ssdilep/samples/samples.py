# encoding: utf-8
'''
samples.py

description:
 samples for HIGG3D3 derivations
'''

#------------------------------------------------------------------------------
# All MC xsections can be found here:
# https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/CentralMC15ProductionList
#------------------------------------------------------------------------------

## modules
from sample import Sample
import ROOT


## colors
black = ROOT.kBlack
white = ROOT.kWhite
red   = ROOT.kRed
green = ROOT.kGreen+1



#-------------------------------------------------------------------------------
# data
#-------------------------------------------------------------------------------
periods = []
periods += [
         # 2015
         "data15_13TeV_periodD",
         "data15_13TeV_periodE",
         "data15_13TeV_periodF",
         "data15_13TeV_periodG",
         "data15_13TeV_periodH",
         "data15_13TeV_periodJ",
         # 2016
         "data16_13TeV_periodA",
         "data16_13TeV_periodB",
         "data16_13TeV_periodC",
         "data16_13TeV_periodD",
         "data16_13TeV_periodE",
         "data16_13TeV_periodF",
         "data16_13TeV_periodG",
         "data16_13TeV_periodI",
         "data16_13TeV_periodK",
         "data16_13TeV_periodL",
         # 2017
         "data17_13TeV_periodB",
         "data17_13TeV_periodC",
         "data17_13TeV_periodD",
         "data17_13TeV_periodE",
         "data17_13TeV_periodF",
         "data17_13TeV_periodH",
         "data17_13TeV_periodI",
         "data17_13TeV_periodK",
        ]

for name in periods:
    globals()[name] = Sample(
            name = name,
            type = "data"
            )

list_runs =[globals()[name] for name in periods]

data = Sample(name         = "data",
              tlatex       = "Data 2015+2016+2017",
              fill_color   = white,
              fill_style   = 0,
              line_color   = black,
              line_style   = 1,
              marker_color = black,
              marker_style = 20,
              daughters    = list_runs,
              )


#-------------------------------------------------------------------------------
# data-driven background
#-------------------------------------------------------------------------------
fakes    = Sample( name         = "fakes",
                   tlatex       = "Fakes",
                   fill_color   = ROOT.kGray,
                   line_color   = ROOT.kGray+1,
                   line_style   = 1,
                   marker_color = ROOT.kGray+1,
                   marker_style = 20,
                   daughters    = list_runs,
                   type         = "datadriven",
                   )


#--------------------------------------------------------------------------------------------------------------------
# W + jets (Sherpa 2.2.1)
# Notes:
#       * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryWjetsSherpa221 (all filters)
#--------------------------------------------------------------------------------------------------------------------

#-----
# Wenu
#-----

Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CVetoBVeto",         xsec = 15299.7024868,  ) 
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CVetoBVeto",       xsec = 611.538499092,  )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CVetoBVeto",      xsec = 196.791474684,  )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CVetoBVeto",      xsec = 38.073801577 ,  )
                                                                                                                                                                   
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CFilterBVeto",       xsec = 2418.3583578 ,  )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CFilterBVeto",     xsec = 209.068226178,  )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CFilterBVeto",    xsec = 95.509733804 ,  )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CFilterBVeto",    xsec = 22.165716989 ,  )
                                                                                                                                                                   
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_BFilter",            xsec = 819.467821557, )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_BFilter",          xsec = 94.8253702473, )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_BFilter",         xsec = 35.894033794 , )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_BFilter",         xsec = 9.368883605  , )
                                                                                                                                                                   
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV500_1000",                xsec = 14.7703248   , )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV1000_E_CMS",              xsec = 1.19664468   , )


Wenu = Sample( name =   'Wenu',
                  tlatex = 'W #rightarrow e#nu+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kRed+1,
                  line_color =  ROOT.kRed+2,
                  marker_color =  ROOT.kRed+2,
                  daughters = [
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CVetoBVeto,        
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CVetoBVeto, 
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CFilterBVeto,      
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CFilterBVeto,    
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_BFilter,           
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_BFilter,         
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV500_1000,        
                               Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV1000_E_CMS,       
                              ],
                ) 

#------
# Wmunu
#------

Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CVetoBVeto",         xsec = 15300.0572987, )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CVetoBVeto",       xsec = 618.428915666, ) 
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CVetoBVeto",      xsec = 206.221283425, )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CVetoBVeto",      xsec = 38.208856376 , )
                                                                                                                                                                    
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CFilterBVeto",       xsec = 2419.07572368, )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CFilterBVeto",     xsec = 213.410699631, )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CFilterBVeto",    xsec = 95.503740588 , )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CFilterBVeto",    xsec = 22.234860368 , )
                                                                                                                                                                    
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_BFilter",            xsec = 819.040831686, )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_BFilter",          xsec = 69.329881007 , )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_BFilter",         xsec = 35.814728094 , )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_BFilter",         xsec = 9.322304129  , )
                                                                                                                                                                    
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV500_1000",                xsec = 14.562702    , )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV1000_E_CMS",              xsec = 1.19761488   , )


Wmunu = Sample( name =   'Wmunu',
                  tlatex = 'W #rightarrow #mu#nu+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kGreen+1,
                  line_color =  ROOT.kGreen+2,
                  marker_color =  ROOT.kGreen+2,
                  daughters = [
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CVetoBVeto,        
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CVetoBVeto,                                    
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CFilterBVeto,      
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CFilterBVeto,    
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_BFilter,           
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_BFilter,         
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV500_1000,        
                               Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV1000_E_CMS,       
                              ],
                ) 

#-------
# Wtaunu
#-------
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CVetoBVeto",         xsec = 15328.6190165,  )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CVetoBVeto",       xsec = 619.516866415,  ) 
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CVetoBVeto",      xsec = 196.303689268,  )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CVetoBVeto",      xsec = 38.153260385 ,  )
                                                                                                                                                                       
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CFilterBVeto",       xsec = 2403.4269992 ,  )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CFilterBVeto",     xsec = 204.11294685 ,  )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CFilterBVeto",    xsec = 95.639994797 ,  )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CFilterBVeto",    xsec = 22.100151339 ,  )
                                                                                                                                                                       
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_BFilter",            xsec = 829.089088304,  )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_BFilter",          xsec = 95.1431170536,  )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_BFilter",         xsec = 38.868467327 ,  )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_BFilter",         xsec = 9.382038479  ,  )
                                                                                                                                                                       
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV500_1000",                xsec = 14.5976292   ,  )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV1000_E_CMS",              xsec = 1.19712978   ,  )

Wtaunu = Sample( name =   'Wtaunu',
                  tlatex = 'W #rightarrow #tau#nu+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kBlue+1,
                  line_color =  ROOT.kBlue+2,
                  marker_color =  ROOT.kBlue+2,
                  daughters = [
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CVetoBVeto,        
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CVetoBVeto,                                    
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CFilterBVeto,      
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CFilterBVeto,    
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_BFilter,           
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_BFilter,         
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV500_1000,        
                               Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV1000_E_CMS,       
                              ],
                ) 


#---------------------------------------------------------------------------------------------------------------------
# Z + jets (Sherpa 2.2.1)
# Notes:
#       * cross sections:  https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryZjetsSherpa221 (all filters)
#---------------------------------------------------------------------------------------------------------------------

#-----
# Zee
#-----
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CVetoBVeto",                xsec = 1586.66000797, ) 
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CVetoBVeto",              xsec = 74.392831377 , )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CVetoBVeto",             xsec = 24.406766768 , )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CVetoBVeto",             xsec = 4.747987696  , )
                                                                                                                                                                       
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CFilterBVeto",              xsec = 218.160449136, )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CFilterBVeto",            xsec = 19.829640036 , )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CFilterBVeto",           xsec = 9.138632129  , )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CFilterBVeto",           xsec = 2.223207556  , )
                                                                                                                                                                       
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_BFilter",                   xsec = 123.301682947, )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_BFilter",                 xsec = 12.308466245 , )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_BFilter",                xsec = 5.923140985  , )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_BFilter",                xsec = 1.457160985  , )
                                                                                                                                                                       
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV500_1000",                       xsec = 1.76307831   , )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV1000_E_CMS",                     xsec = 0.144870607  , )

Zee = Sample( name =   'Zee',                                                                                                                              
                  tlatex = 'Z #rightarrow ee+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kOrange+1,
                  line_color =  ROOT.kOrange+2,
                  marker_color =  ROOT.kOrange+2,
                  daughters = [
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CVetoBVeto,        
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CVetoBVeto,                                    
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CFilterBVeto,      
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CFilterBVeto,    
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_BFilter,           
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_BFilter,         
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV500_1000,        
                               Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV1000_E_CMS,       
                              ],
                ) 


#-------
# Zmumu
#-------
                                                                     
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CVetoBVeto",              xsec = 1588.71733441,  )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CVetoBVeto",            xsec = 73.2618419445,  ) 
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CVetoBVeto",           xsec = 23.6966813186,  )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CVetoBVeto",           xsec = 4.6487083167 ,  )
                                                                                                                                                                          
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CFilterBVeto",            xsec = 218.358902463,  )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CFilterBVeto",          xsec = 19.8590024419,  )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CFilterBVeto",         xsec = 9.06175614257,  )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CFilterBVeto",         xsec = 2.20891350665,  )
                                                                                                                                                                          
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_BFilter",                 xsec = 124.421478524,  )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_BFilter",               xsec = 12.0883026088,  )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_BFilter",              xsec = 5.74741074457,  )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_BFilter",              xsec = 1.45819160585,  )
                                                                                                                                                                          
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV500_1000",                     xsec = 1.74201615   ,  )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV1000_E_CMS",                   xsec = 0.143944262  ,  )


Zmumu = Sample( name =   'Zmumu',                                                                                                                         
                  tlatex = 'Z #rightarrow #mu#mu+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kSpring+1,
                  line_color =  ROOT.kSpring+2,
                  marker_color =  ROOT.kSpring+2,
                  daughters = [
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CVetoBVeto,        
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CVetoBVeto,                                    
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CFilterBVeto,      
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CFilterBVeto,    
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_BFilter,           
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_BFilter,         
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV500_1000,        
                               Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV1000_E_CMS,       
                              ],
                ) 



#---------
# Ztautau
#---------

Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CVetoBVeto",         xsec = 1587.19549779 ,  )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CVetoBVeto",       xsec = 74.1331155392 ,  ) 
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CVetoBVeto",      xsec = 24.185807051  ,  )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CVetoBVeto",      xsec = 4.67188943921 ,  )
                                                                                                                                                                          
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CFilterBVeto",       xsec = 218.306784343 ,  )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CFilterBVeto",     xsec = 19.7089932529 ,  )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CFilterBVeto",    xsec = 9.09596467878 ,  )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CFilterBVeto",    xsec = 2.21896214715 ,  )
                                                                                                                                                                          
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_BFilter",            xsec = 124.552404811 ,  )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_BFilter",          xsec = 11.9878119426 ,  ) 
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_BFilter",         xsec = 5.34266418886 ,  )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_BFilter",         xsec = 1.46541699447 ,  )
                                                                                                                                                                          
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV500_1000",                xsec = 1.76454096   ,   )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV1000_E_CMS",              xsec = 0.144646334  ,   )


Ztautau = Sample( name =   'Ztautau',
                  tlatex = 'Z #rightarrow #tau#tau+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kAzure-4,
                  line_color =  ROOT.kAzure-5,
                  marker_color =  ROOT.kAzure-5,
                  daughters = [
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CVetoBVeto,        
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CVetoBVeto,                                    
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CVetoBVeto,     
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CFilterBVeto,      
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CFilterBVeto,    
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CFilterBVeto,   
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_BFilter,           
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_BFilter,         
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_BFilter,        
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_BFilter,   
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV500_1000,        
                               Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV1000_E_CMS,       
                              ],
                ) 


#-----------------------------------------------------------------------------
# Top 
#-----------------------------------------------------------------------------


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ttbar ( Powheg + Pythia )
# Notes:
#       * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryTTbar 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

PhPy8EG_A14_ttbar_hdamp258p75_nonallhad = Sample( name =  "PhPy8EG_A14_ttbar_hdamp258p75_nonallhad", xsec = 452.336040799,)
PhPy8EG_A14_ttbar_hdamp258p75_allhad    = Sample( name =  "PhPy8EG_A14_ttbar_hdamp258p75_allhad",    xsec = 379.501934906,)
PhPy8EG_A14_ttbar_hdamp258p75_dil       = Sample( name =  "PhPy8EG_A14_ttbar_hdamp258p75_dil",       xsec = 87.709092,    )

ttbar = Sample( name =  'ttbar',
                    tlatex = 'ttbar',
                    fill_color = ROOT.kCyan+1,
                    line_color =  ROOT.kCyan+2,
                    marker_color =  ROOT.kCyan+2,
                    daughters = [
                                 PhPy8EG_A14_ttbar_hdamp258p75_nonallhad,
                                 PhPy8EG_A14_ttbar_hdamp258p75_allhad,
                                 PhPy8EG_A14_ttbar_hdamp258p75_dil      
                                ],
                    ) 


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# single-top
# Notes:
#       * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummarySingleTop
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PowhegPythiaEvtGen_P2012_Wt_inclusive_top             = Sample( name = "PowhegPythiaEvtGen_P2012_Wt_inclusive_top",             xsec = 35.845486, )
PowhegPythiaEvtGen_P2012_Wt_inclusive_antitop         = Sample( name = "PowhegPythiaEvtGen_P2012_Wt_inclusive_antitop",         xsec = 35.824406, )
PowhegPythiaEvtGen_P2012_Wt_dilepton_top              = Sample( name = "PowhegPythiaEvtGen_P2012_Wt_dilepton_top",              xsec = 3.777009, )
PowhegPythiaEvtGen_P2012_Wt_dilepton_antitop          = Sample( name = "PowhegPythiaEvtGen_P2012_Wt_dilepton_antitop",          xsec = 3.7747956, )
PowhegPythiaEvtGen_P2012_singletop_tchan_lept_top     = Sample( name = "PowhegPythiaEvtGen_P2012_singletop_tchan_lept_top",     xsec = 44.152, )
PowhegPythiaEvtGen_P2012_singletop_tchan_lept_antitop = Sample( name = "PowhegPythiaEvtGen_P2012_singletop_tchan_lept_antitop", xsec = 26.276, )

singletop = Sample( name =   'singletop',
                    tlatex = 'single-top',
                    fill_color = ROOT.kRed+3,
                    line_color =  ROOT.kRed+4,
                    marker_color =  ROOT.kRed+4,
                    daughters = [
                                 PowhegPythiaEvtGen_P2012_Wt_inclusive_antitop,        
                                 PowhegPythiaEvtGen_P2012_Wt_inclusive_top,            
                                 #PowhegPythiaEvtGen_P2012_singletop_tchan_lept_antitop,
                                 #PowhegPythiaEvtGen_P2012_singletop_tchan_lept_top,    
                                 #PowhegPythiaEvtGen_P2012_Wt_dilepton_top,
                                 #PowhegPythiaEvtGen_P2012_Wt_dilepton_antitop,
                                ],
                ) 

#-----------------------------------------------------------------------------
# Diboson (list of samples might be incomplete!)
#-----------------------------------------------------------------------------

Sherpa_221_NNPDF30NNLO_ZqqZvv   = Sample( name = "Sherpa_221_NNPDF30NNLO_ZqqZvv" ,   xsec = 4.35418464, )
Sherpa_221_NNPDF30NNLO_ZqqZll   = Sample( name = "Sherpa_221_NNPDF30NNLO_ZqqZll" ,   xsec = 2.17275043, )
Sherpa_221_NNPDF30NNLO_WqqZvv   = Sample( name = "Sherpa_221_NNPDF30NNLO_WqqZvv" ,   xsec = 6.7973,     )
Sherpa_221_NNPDF30NNLO_WqqZll   = Sample( name = "Sherpa_221_NNPDF30NNLO_WqqZll" ,   xsec = 3.4345,     )
Sherpa_221_NNPDF30NNLO_WpqqWmlv = Sample( name = "Sherpa_221_NNPDF30NNLO_WpqqWmlv" , xsec = 24.719,     )
Sherpa_221_NNPDF30NNLO_WplvWmqq = Sample( name = "Sherpa_221_NNPDF30NNLO_WplvWmqq" , xsec = 112.74,     )
Sherpa_221_NNPDF30NNLO_WlvZqq   = Sample( name = "Sherpa_221_NNPDF30NNLO_WlvZqq" ,   xsec = 11.42,      )

Sherpa_222_NNPDF30NNLO_lllljj_EW6    = Sample( name ="Sherpa_222_NNPDF30NNLO_lllljj_EW6" ,    xsec = 0.010523,)
Sherpa_222_NNPDF30NNLO_lllvjj_EW6    = Sample( name ="Sherpa_222_NNPDF30NNLO_lllvjj_EW6" ,    xsec = 0.046691,)
Sherpa_222_NNPDF30NNLO_llvvjj_EW6    = Sample( name ="Sherpa_222_NNPDF30NNLO_llvvjj_EW6" ,    xsec = 0.11621, )
Sherpa_222_NNPDF30NNLO_llvvjj_ss_EW4 = Sample( name ="Sherpa_222_NNPDF30NNLO_llvvjj_ss_EW4" , xsec = 0.025211,)
Sherpa_222_NNPDF30NNLO_llvvjj_ss_EW6 = Sample( name ="Sherpa_222_NNPDF30NNLO_llvvjj_ss_EW6" , xsec = 0.040804,)

# this is a mix of 222 and 221
Sherpa_222_NNPDF30NNLO_llll = Sample( name ="Sherpa_222_NNPDF30NNLO_llll" , xsec = 1.2523, )
Sherpa_222_NNPDF30NNLO_lllv = Sample( name ="Sherpa_222_NNPDF30NNLO_lllv" , xsec = 4.5832, )
Sherpa_222_NNPDF30NNLO_llvv = Sample( name ="Sherpa_222_NNPDF30NNLO_llvv" , xsec = 12.501, )
Sherpa_222_NNPDF30NNLO_lvvv = Sample( name ="Sherpa_222_NNPDF30NNLO_lvvv" , xsec = 3.231, )
Sherpa_221_NNPDF30NNLO_vvvv = Sample( name ="Sherpa_221_NNPDF30NNLO_vvvv" , xsec = 0.60154,)

diboson = Sample( name =   'diboson',
                    tlatex = 'diboson',
                    fill_color = ROOT.kOrange+4,
                    line_color =  ROOT.kOrange+3,
                    marker_color =  ROOT.kOrange+4,
                    daughters = [
                                  Sherpa_221_NNPDF30NNLO_ZqqZvv,
                                  Sherpa_221_NNPDF30NNLO_ZqqZll,  
                                  Sherpa_221_NNPDF30NNLO_WqqZvv,  
                                  Sherpa_221_NNPDF30NNLO_WqqZll,  
                                  Sherpa_221_NNPDF30NNLO_WpqqWmlv,
                                  #Sherpa_221_NNPDF30NNLO_WplvWmqq,
                                  Sherpa_221_NNPDF30NNLO_WlvZqq,  
                                  #Sherpa_222_NNPDF30NNLO_lllljj_EW6,  
                                  #Sherpa_222_NNPDF30NNLO_lllvjj_EW6,   
                                  #Sherpa_222_NNPDF30NNLO_llvvjj_EW6,   
                                  #Sherpa_222_NNPDF30NNLO_llvvjj_ss_EW4,
                                  #Sherpa_222_NNPDF30NNLO_llvvjj_ss_EW6,
                                  Sherpa_222_NNPDF30NNLO_llll,
                                  Sherpa_222_NNPDF30NNLO_lllv,
                                  Sherpa_222_NNPDF30NNLO_llvv,
                                  Sherpa_222_NNPDF30NNLO_lvvv,
                                  Sherpa_221_NNPDF30NNLO_vvvv,
                                ],
                ) 

#-------------------------------------------------------------------------------
# Collections 
#-------------------------------------------------------------------------------

# Samples loaded for SubmitHist.py
#---------------------------------

all_data = data.daughters

all_mc = []

all_mc += ttbar.daughters
all_mc += singletop.daughters

#all_mc += Wenu.daughters
#all_mc += Wmunu.daughters
all_mc += Wtaunu.daughters

#all_mc += Zee.daughters
#all_mc += Zmumu.daughters
all_mc += Ztautau.daughters

#all_mc += diboson.daughters


# Samples loaded for SubmitPlot.py
#---------------------------------

mc_bkg = []

#mc_bkg.append( Wenu )
#mc_bkg.append( Wmunu )
mc_bkg.append( Wtaunu )

#mc_bkg.append( Zee ) 
#mc_bkg.append( Zmumu )
mc_bkg.append( Ztautau )

#mc_bkg.append( singletop )
mc_bkg.append( ttbar )

#mc_bkg.append( diboson )
## EOF
