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
import samples_DCH 
import ROOT
from data_periods import data_periods

## colors
black = ROOT.kBlack
white = ROOT.kWhite
red   = ROOT.kRed
green = ROOT.kGreen+1


def getFiltered(sample, suffix):
   
   filtered_style = {}
   filtered_style['qfakes'] = 3144
   filtered_style['gfakes'] = 3315
   filtered_style['ufakes'] = 3305
   
   globals()[sample.name+"_"+suffix] = sample.duplicate(suffix=suffix, tlatex='{} {}'.format(sample.name, suffix), fill_style=filtered_style[suffix])


#-------------------------------------------------------------------------------
# data
#-------------------------------------------------------------------------------

for name in data_periods:
    sname = "physics_Main_"+name
    globals()[sname] = Sample(
            name = sname,
            type = "data"
            )

list_runs =[globals()["physics_Main_"+name] for name in data_periods]

data = Sample(name         = "data",
              tlatex       = "Data",
              fill_color   = white,
              fill_style   = 0,
              line_color   = black,
              line_style   = 1,
              marker_color = black,
              marker_style = 20,
              type         = "data",
              #daughters    = list_runs,
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

Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CVetoBVeto",       ) 
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CVetoBVeto",     )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CVetoBVeto",    )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CVetoBVeto",    )
                                                                                                                                           
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CFilterBVeto",     )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CFilterBVeto",   )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CFilterBVeto",  )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CFilterBVeto",  )
                                                                                                                                           
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_BFilter",          )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_BFilter",        )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_BFilter",       )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_BFilter",       )
                                                                                                                                           
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV500_1000",              )
Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV1000_E_CMS",            )


Wenu = Sample( name =   'Wenu',
                  tlatex = 'W #rightarrow e#nu+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kRed+1,
                  line_color =  ROOT.kRed+2,
                  marker_color =  ROOT.kRed+2,
                  #daughters = [
                  #             Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CVetoBVeto,        
                  #             Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CVetoBVeto, 
                  #             Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CVetoBVeto,     
                  #             Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CVetoBVeto,     
                  #             Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_CFilterBVeto,      
                  #             Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_CFilterBVeto,    
                  #             Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_CFilterBVeto,   
                  #             Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_CFilterBVeto,   
                  #             Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV0_70_BFilter,           
                  #             Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV70_140_BFilter,         
                  #             Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV140_280_BFilter,        
                  #             Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV280_500_BFilter,        
                  #             Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV500_1000,        
                  #             Sherpa_221_NNPDF30NNLO_Wenu_MAXHTPTV1000_E_CMS,       
                  #            ],
                ) 


Wenu_fakes = Sample( name =   'Wenu_fakes',
                  tlatex = 'W #rightarrow e#nu+jets (fakes)',
                  fill_color = ROOT.kRed+1,
                  fill_style = 3002,
                  line_color =  ROOT.kRed+2,
                  marker_color =  ROOT.kRed+2,
                  daughters = Wenu.daughters,
                ) 



#------
# Wmunu
#------

Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CVetoBVeto",       )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CVetoBVeto",     ) 
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CVetoBVeto",    )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CVetoBVeto",    )
                                                                                                                                            
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CFilterBVeto",     )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CFilterBVeto",   )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CFilterBVeto",  )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CFilterBVeto",  )
                                                                                                                                            
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_BFilter",          )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_BFilter",        )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_BFilter",       )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_BFilter",       )
                                                                                                                                            
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV500_1000",              )
Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV1000_E_CMS",            )


Wmunu = Sample( name =   'Wmunu',
                  tlatex = 'W #rightarrow #mu#nu+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kGreen+1,
                  line_color =  ROOT.kGreen+2,
                  marker_color =  ROOT.kGreen+2,
                  #daughters = [
                  #             Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CVetoBVeto,        
                  #             Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CVetoBVeto,                                    
                  #             Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CVetoBVeto,     
                  #             Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CVetoBVeto,     
                  #             Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_CFilterBVeto,      
                  #             Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_CFilterBVeto,    
                  #             Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_CFilterBVeto,   
                  #             Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_CFilterBVeto,   
                  #             Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV0_70_BFilter,           
                  #             Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV70_140_BFilter,         
                  #             Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV140_280_BFilter,        
                  #             Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV280_500_BFilter,        
                  #             Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV500_1000,        
                  #             Sherpa_221_NNPDF30NNLO_Wmunu_MAXHTPTV1000_E_CMS,       
                  #            ],
                ) 

Wmunu_fakes = Sample( name =   'Wmunu_fakes',
                  tlatex = 'W #rightarrow #mu#nu+jets (fakes)',
                  fill_color = ROOT.kGreen+1,
                  fill_style = 3002,
                  line_color =  ROOT.kGreen+2,
                  marker_color =  ROOT.kGreen+2,
                  daughters = Wmunu.daughters,
                ) 

#-------
# Wtaunu
#-------
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CVetoBVeto",        )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CVetoBVeto",      ) 
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CVetoBVeto",     )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CVetoBVeto",     )
                                                                                                                                               
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CFilterBVeto",      )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CFilterBVeto",    )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CFilterBVeto",   )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CFilterBVeto",   )
                                                                                                                                               
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_BFilter",           )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_BFilter",         )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_BFilter",        )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_BFilter",        )
                                                                                                                                               
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV500_1000",               )
Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV1000_E_CMS",             )

Wtaunu = Sample( name =   'Wtaunu',
                  tlatex = 'W #rightarrow #tau#nu+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kBlue+1,
                  line_color =  ROOT.kBlue+2,
                  marker_color =  ROOT.kBlue+2,
                  #daughters = [
                  #             Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CVetoBVeto,        
                  #             Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CVetoBVeto,                                    
                  #             Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CVetoBVeto,     
                  #             Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CVetoBVeto,     
                  #             Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_CFilterBVeto,      
                  #             Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_CFilterBVeto,    
                  #             Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_CFilterBVeto,   
                  #             Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_CFilterBVeto,   
                  #             Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV0_70_BFilter,           
                  #             Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV70_140_BFilter,         
                  #             Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV140_280_BFilter,        
                  #             Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV280_500_BFilter,        
                  #             Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV500_1000,        
                  #             Sherpa_221_NNPDF30NNLO_Wtaunu_MAXHTPTV1000_E_CMS,       
                  #            ],
                ) 

Wtaunu_fakes = Sample( name =   'Wtaunu_fakes',
                  tlatex = 'W #rightarrow #tau#nu+jets (fakes)',
                  fill_color = ROOT.kBlue+1,
                  fill_style = 3002,
                  line_color =  ROOT.kBlue+2,
                  marker_color =  ROOT.kBlue+2,
                  daughters = Wtaunu.daughters,
                ) 


#---------------------------------------------------------------------------------------------------------------------
# Z + jets (Sherpa 2.2.1)
# Notes:
#       * cross sections:  https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryZjetsSherpa221 (all filters)
#---------------------------------------------------------------------------------------------------------------------

#-----
# Zee
#-----
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CVetoBVeto",       ) 
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CVetoBVeto",     )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CVetoBVeto",    )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CVetoBVeto",    )
                                                                                                                                         
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CFilterBVeto",     )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CFilterBVeto",   )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CFilterBVeto",  )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CFilterBVeto",  )
                                                                                                                                         
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_BFilter",          )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_BFilter",        )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_BFilter",       )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_BFilter",       )
                                                                                                                                         
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV500_1000",              )
Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV1000_E_CMS",            )

Zee = Sample( name =   'Zee',                                                                                                                              
                  tlatex = 'Z #rightarrow ee+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kOrange+1,
                  line_color =  ROOT.kOrange+2,
                  marker_color =  ROOT.kOrange+2,
                  #daughters = [
                  #             Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CVetoBVeto,        
                  #             Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CVetoBVeto,                                    
                  #             Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CVetoBVeto,     
                  #             Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CVetoBVeto,     
                  #             Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_CFilterBVeto,      
                  #             Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_CFilterBVeto,    
                  #             Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_CFilterBVeto,   
                  #             Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_CFilterBVeto,   
                  #             Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV0_70_BFilter,           
                  #             Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV70_140_BFilter,         
                  #             Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV140_280_BFilter,        
                  #             Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV280_500_BFilter,        
                  #             Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV500_1000,        
                  #             Sherpa_221_NNPDF30NNLO_Zee_MAXHTPTV1000_E_CMS,       
                  #            ],
                ) 


#-------
# Zmumu
#-------
                                                                     
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CVetoBVeto",        )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CVetoBVeto",      ) 
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CVetoBVeto",     )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CVetoBVeto",     )
                                                                                                                                             
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CFilterBVeto",      )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CFilterBVeto",    )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CFilterBVeto",   )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CFilterBVeto",   )
                                                                                                                                             
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_BFilter",           )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_BFilter",         )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_BFilter",        )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_BFilter",        )
                                                                                                                                             
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV500_1000",               )
Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV1000_E_CMS",             )


Zmumu = Sample( name =   'Zmumu',                                                                                                                         
                  tlatex = 'Z #rightarrow #mu#mu+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kSpring+1,
                  line_color =  ROOT.kSpring+2,
                  marker_color =  ROOT.kSpring+2,
                  #daughters = [
                  #             Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CVetoBVeto,        
                  #             Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CVetoBVeto,                                    
                  #             Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CVetoBVeto,     
                  #             Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CVetoBVeto,     
                  #             Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_CFilterBVeto,      
                  #             Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_CFilterBVeto,    
                  #             Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_CFilterBVeto,   
                  #             Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_CFilterBVeto,   
                  #             Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV0_70_BFilter,           
                  #             Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV70_140_BFilter,         
                  #             Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV140_280_BFilter,        
                  #             Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV280_500_BFilter,        
                  #             Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV500_1000,        
                  #             Sherpa_221_NNPDF30NNLO_Zmumu_MAXHTPTV1000_E_CMS,       
                  #            ],
                ) 


#---------
# Ztautau
#---------

Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CVetoBVeto         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CVetoBVeto",       )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CVetoBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CVetoBVeto",     ) 
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CVetoBVeto",    )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CVetoBVeto      = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CVetoBVeto",    )
                                                                                                                                                
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CFilterBVeto       = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CFilterBVeto",     )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CFilterBVeto     = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CFilterBVeto",   )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CFilterBVeto",  )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CFilterBVeto    = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CFilterBVeto",  )
                                                                                                                                                
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_BFilter            = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_BFilter",          )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_BFilter          = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_BFilter",        ) 
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_BFilter",       )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_BFilter         = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_BFilter",       )
                                                                                                                                                
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV500_1000                = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV500_1000",              )
Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV1000_E_CMS              = Sample( name =  "Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV1000_E_CMS",            )


Ztautau = Sample( name =   'Ztautau',
                  tlatex = 'Z #rightarrow #tau#tau+jets (Sherpa 2.2.1)',
                  fill_color = ROOT.kAzure-4,
                  line_color =  ROOT.kAzure-5,
                  marker_color =  ROOT.kAzure-5,
                  #daughters = [
                  #             Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CVetoBVeto,        
                  #             Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CVetoBVeto,                                    
                  #             Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CVetoBVeto,     
                  #             Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CVetoBVeto,     
                  #             Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_CFilterBVeto,      
                  #             Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_CFilterBVeto,    
                  #             Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_CFilterBVeto,   
                  #             Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_CFilterBVeto,   
                  #             Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV0_70_BFilter,           
                  #             Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV70_140_BFilter,         
                  #             Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV140_280_BFilter,        
                  #             Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV280_500_BFilter,   
                  #             Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV500_1000,        
                  #             Sherpa_221_NNPDF30NNLO_Ztautau_MAXHTPTV1000_E_CMS,       
                  #            ],
                ) 

#-----------------------------------------------------------------------------
# Top 
#-----------------------------------------------------------------------------


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ttbar ( Powheg + Pythia )
# Notes:
#       * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummaryTTbar 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

PhPy8EG_A14_ttbar_hdamp258p75_nonallhad = Sample( name =  "PhPy8EG_A14_ttbar_hdamp258p75_nonallhad",)
PhPy8EG_A14_ttbar_hdamp258p75_allhad    = Sample( name =  "PhPy8EG_A14_ttbar_hdamp258p75_allhad",   )
PhPy8EG_A14_ttbar_hdamp258p75_dil       = Sample( name =  "PhPy8EG_A14_ttbar_hdamp258p75_dil",      )

ttbar = Sample( name =  'ttbar',
                    tlatex = 'ttbar',
                    fill_color = ROOT.kCyan+1,
                    line_color =  ROOT.kCyan+2,
                    marker_color =  ROOT.kCyan+2,
                    #daughters = [
                    #             PhPy8EG_A14_ttbar_hdamp258p75_nonallhad,
                    #             PhPy8EG_A14_ttbar_hdamp258p75_allhad,
                    #             PhPy8EG_A14_ttbar_hdamp258p75_dil      
                    #            ],
                    ) 


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# single-top
# Notes:
#       * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/XsecSummarySingleTop
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PhPy8EG_A14_tchan_BW50_lept_antitop                      = Sample( name = "PhPy8EG_A14_tchan_BW50_lept_antitop"                  )
PhPy8EG_A14_tchan_BW50_lept_top                          = Sample( name = "PhPy8EG_A14_tchan_BW50_lept_top"                      )
PowhegPythia8EvtGen_A14_singletop_schan_lept_antitop     = Sample( name = "PowhegPythia8EvtGen_A14_singletop_schan_lept_antitop" )
PowhegPythia8EvtGen_A14_singletop_schan_lept_top         = Sample( name = "PowhegPythia8EvtGen_A14_singletop_schan_lept_top"     )
PowhegPythia8EvtGen_A14_Wt_DR_inclusive_antitop          = Sample( name = "PowhegPythia8EvtGen_A14_Wt_DR_inclusive_antitop"      )
PowhegPythia8EvtGen_A14_Wt_DR_inclusive_top              = Sample( name = "PowhegPythia8EvtGen_A14_Wt_DR_inclusive_top"          )

singletop = Sample( name =   'singletop',
                    tlatex = 'single-top',
                    fill_color = ROOT.kRed+3,
                    line_color =  ROOT.kRed+4,
                    marker_color =  ROOT.kRed+4,
                    #daughters = [
                    #              PhPy8EG_A14_tchan_BW50_lept_antitop,                 
                    #              PhPy8EG_A14_tchan_BW50_lept_top,                     
                    #              PowhegPythia8EvtGen_A14_singletop_schan_lept_antitop,
                    #              PowhegPythia8EvtGen_A14_singletop_schan_lept_top,    
                    #              PowhegPythia8EvtGen_A14_Wt_DR_inclusive_antitop,     
                    #              PowhegPythia8EvtGen_A14_Wt_DR_inclusive_top,         
                    #            ],
                ) 


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ttV
# Notes:
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

aMcAtNloPythia8EvtGen_A14_NNPDF23_NNPDF30ME_ttH125_allhad   = Sample( name = "aMcAtNloPythia8EvtGen_A14_NNPDF23_NNPDF30ME_ttH125_allhad"  )
aMcAtNloPythia8EvtGen_A14_NNPDF23_NNPDF30ME_ttH125_semilep  = Sample( name = "aMcAtNloPythia8EvtGen_A14_NNPDF23_NNPDF30ME_ttH125_semilep" )
aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttee                = Sample( name = "aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttee"               )
aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttmumu              = Sample( name = "aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttmumu"             )
aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_tttautau            = Sample( name = "aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_tttautau"           )
aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttW                 = Sample( name = "aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttW"                )
aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttZnunu             = Sample( name = "aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttZnunu"            )
aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttZqq               = Sample( name = "aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttZqq"              )
MadGraphPythia8EvtGen_A14NNPDF23_3top_SM                    = Sample( name = "MadGraphPythia8EvtGen_A14NNPDF23_3top_SM"                   )
MadGraphPythia8EvtGen_A14NNPDF23_4topSM                     = Sample( name = "MadGraphPythia8EvtGen_A14NNPDF23_4topSM"                    )

ttV = Sample( name =   'ttV',
                    tlatex = 'ttV',
                    fill_color = ROOT.kPink+3,
                    line_color =  ROOT.kPink-7,
                    marker_color =  ROOT.kPink-7,
                    #daughters = [
                    #             #aMcAtNloPythia8EvtGen_A14_NNPDF23_NNPDF30ME_ttH125_allhad,
                    #             #aMcAtNloPythia8EvtGen_A14_NNPDF23_NNPDF30ME_ttH125_semilep,
                    #             aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttee,              
                    #             aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttmumu,
                    #             aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_tttautau,
                    #             aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttW,               
                    #             aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttZnunu,
                    #             aMcAtNloPythia8EvtGen_MEN30NLO_A14N23LO_ttZqq,          
                    #             MadGraphPythia8EvtGen_A14NNPDF23_3top_SM,                  
                    #             MadGraphPythia8EvtGen_A14NNPDF23_4topSM,                   
                    #            ],
                ) 


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# dijet ( A14 NNPDF23 LO tune )
# Notes:
#       * cross sections: https://twiki.cern.ch/twiki/bin/view/AtlasProtected/MC15MultijetPMG
#       * more info:      https://twiki.cern.ch/twiki/bin/view/AtlasProtected/MultijetFocusGroup
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ0WithSW   = Sample( name =   "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ0WithSW",  )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ1WithSW   = Sample( name =   "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ1WithSW",  )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ2WithSW   = Sample( name =   "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ2WithSW",  )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ3WithSW   = Sample( name =   "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ3WithSW",  )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ4WithSW   = Sample( name =   "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ4WithSW",  )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ5WithSW   = Sample( name =   "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ5WithSW",  )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ6WithSW   = Sample( name =   "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ6WithSW",  )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ7WithSW   = Sample( name =   "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ7WithSW",  )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ8WithSW   = Sample( name =   "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ8WithSW",  )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ9WithSW   = Sample( name =   "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ9WithSW",  )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ10WithSW  = Sample( name =   "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ10WithSW", )
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ11WithSW  = Sample( name =   "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ11WithSW", )  
Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ12WithSW  = Sample( name =   "Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ12WithSW", )


JZ_dict = {"0"  : ROOT.kRed,
           "1"  : ROOT.kYellow,
           "2"  : ROOT.kBlue,
           "3"  : ROOT.kGreen,
           "4"  : ROOT.kCyan,
           "5"  : ROOT.kMagenta,
           "6"  : ROOT.kOrange,
           "7"  : ROOT.kRed+1,
           "8"  : ROOT.kBlue+1,
           "9"  : ROOT.kMagenta+1,
           "10" : ROOT.kYellow+1,
           "11" : ROOT.kGreen+1,
           "12" : ROOT.kSpring+1}

for jz,jz_color in JZ_dict.iteritems():
  globals()["Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ%sWithSW"%(jz)].tlatex = "JZ%sW"%(jz)
  globals()["Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ%sWithSW"%(jz)].fill_color   = jz_color
  globals()["Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ%sWithSW"%(jz)].line_color   = jz_color+1
  globals()["Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ%sWithSW"%(jz)].marker_color = jz_color+1


dijet = Sample( name =   'dijet',
                    tlatex = 'Di-Jet',
                    fill_color = ROOT.kOrange+6,
                    line_color =  ROOT.kOrange+5,
                    marker_color =  ROOT.kOrange+5,
                    daughters = [
                             ##Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ0WithSW,         
                             # Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ1WithSW, 
                             # Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ2WithSW, 
                             # Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ3WithSW, 
                             # Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ4WithSW, 
                             # Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ5WithSW, 
                             # Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ6WithSW, 
                             # Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ7WithSW, 
                             # Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ8WithSW, 
                             # Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ9WithSW, 
                             # Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ10WithSW,
                             # Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ11WithSW,
                             # Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ12WithSW,
                              ],
                ) 


#-----------------------------------------------------------------------------
# Diboson (list of samples might be incomplete!)
#-----------------------------------------------------------------------------

# this is a mix of 222 and 221
Sherpa_222_NNPDF30NNLO_llll            = Sample( name = "Sherpa_222_NNPDF30NNLO_llll" )
Sherpa_222_NNPDF30NNLO_lllv            = Sample( name = "Sherpa_222_NNPDF30NNLO_lllv" )
Sherpa_222_NNPDF30NNLO_llvv            = Sample( name = "Sherpa_222_NNPDF30NNLO_llvv" )
Sherpa_222_NNPDF30NNLO_lvvv            = Sample( name = "Sherpa_222_NNPDF30NNLO_lvvv" )
Sherpa_221_NNPDF30NNLO_vvvv            = Sample( name = "Sherpa_221_NNPDF30NNLO_vvvv" )
                                       
Sherpa_221_NNPDF30NNLO_ZqqZvv          = Sample( name = "Sherpa_221_NNPDF30NNLO_ZqqZvv"   )
Sherpa_221_NNPDF30NNLO_ZqqZll          = Sample( name = "Sherpa_221_NNPDF30NNLO_ZqqZll"   )
Sherpa_221_NNPDF30NNLO_WqqZvv          = Sample( name = "Sherpa_221_NNPDF30NNLO_WqqZvv"   )
Sherpa_221_NNPDF30NNLO_WqqZll          = Sample( name = "Sherpa_221_NNPDF30NNLO_WqqZll"   )
Sherpa_221_NNPDF30NNLO_WpqqWmlv        = Sample( name = "Sherpa_221_NNPDF30NNLO_WpqqWmlv" )
Sherpa_221_NNPDF30NNLO_WplvWmqq        = Sample( name = "Sherpa_221_NNPDF30NNLO_WplvWmqq" )
Sherpa_221_NNPDF30NNLO_WlvZqq          = Sample( name = "Sherpa_221_NNPDF30NNLO_WlvZqq"   )
                                       
Sherpa_222_NNPDF30NNLO_lllljj_EW6      = Sample( name ="Sherpa_222_NNPDF30NNLO_lllljj_EW6"    )
Sherpa_222_NNPDF30NNLO_lllvjj_EW6      = Sample( name ="Sherpa_222_NNPDF30NNLO_lllvjj_EW6"    )
Sherpa_222_NNPDF30NNLO_llvvjj_EW6      = Sample( name ="Sherpa_222_NNPDF30NNLO_llvvjj_EW6"    )
Sherpa_222_NNPDF30NNLO_llvvjj_ss_EW4   = Sample( name ="Sherpa_222_NNPDF30NNLO_llvvjj_ss_EW4" )
Sherpa_222_NNPDF30NNLO_llvvjj_ss_EW6   = Sample( name ="Sherpa_222_NNPDF30NNLO_llvvjj_ss_EW6" )
                                       
Sherpa_222_NNPDF30NNLO_WWW_3l3v_EW6    = Sample( name = "Sherpa_222_NNPDF30NNLO_WWW_3l3v_EW6"  )
Sherpa_222_NNPDF30NNLO_WWZ_4l2v_EW6    = Sample( name = "Sherpa_222_NNPDF30NNLO_WWZ_4l2v_EW6"  )
Sherpa_222_NNPDF30NNLO_WWZ_2l4v_EW6    = Sample( name = "Sherpa_222_NNPDF30NNLO_WWZ_2l4v_EW6"  )
Sherpa_222_NNPDF30NNLO_WZZ_5l1v_EW6    = Sample( name = "Sherpa_222_NNPDF30NNLO_WZZ_5l1v_EW6"  )
Sherpa_222_NNPDF30NNLO_WZZ_3l3v_EW6    = Sample( name = "Sherpa_222_NNPDF30NNLO_WZZ_3l3v_EW6"  )
Sherpa_222_NNPDF30NNLO_ZZZ_6l0v_EW6    = Sample( name = "Sherpa_222_NNPDF30NNLO_ZZZ_6l0v_EW6"  ) 
Sherpa_222_NNPDF30NNLO_ZZZ_4l2v_EW6    = Sample( name = "Sherpa_222_NNPDF30NNLO_ZZZ_4l2v_EW6"  )
Sherpa_222_NNPDF30NNLO_ZZZ_2l4v_EW6    = Sample( name = "Sherpa_222_NNPDF30NNLO_ZZZ_2l4v_EW6"  )
Sherpa_222_NNPDF30NNLO_WWZ_3l1v2j_EW6  = Sample( name = "Sherpa_222_NNPDF30NNLO_WWZ_3l1v2j_EW6")
Sherpa_222_NNPDF30NNLO_WZZ_4l2j_EW6    = Sample( name = "Sherpa_222_NNPDF30NNLO_WZZ_4l2j_EW6"  )
Sherpa_222_NNPDF30NNLO_WZZ_3l1v2j_EW6  = Sample( name = "Sherpa_222_NNPDF30NNLO_WZZ_3l1v2j_EW6")

Sherpa_221_NNPDF30NNLO_6l0v_EW6        = Sample( name = "Sherpa_221_NNPDF30NNLO_6l0v_EW6" )
Sherpa_221_NNPDF30NNLO_5l1v_EW6        = Sample( name = "Sherpa_221_NNPDF30NNLO_5l1v_EW6" )
Sherpa_221_NNPDF30NNLO_4l2v_EW6        = Sample( name = "Sherpa_221_NNPDF30NNLO_4l2v_EW6" )
Sherpa_221_NNPDF30NNLO_3l3v_EW6        = Sample( name = "Sherpa_221_NNPDF30NNLO_3l3v_EW6" )
Sherpa_221_NNPDF30NNLO_2l4v_EW6        = Sample( name = "Sherpa_221_NNPDF30NNLO_2l4v_EW6" )

Sherpa_222_NNPDF30NNLO_ggllll_0M4l130  = Sample( name = "Sherpa_222_NNPDF30NNLO_ggllll_0M4l130" )
Sherpa_222_NNPDF30NNLO_ggllll_130M4l   = Sample( name = "Sherpa_222_NNPDF30NNLO_ggllll_130M4l"  )
Sherpa_222_NNPDF30NNLO_ggllvvInt       = Sample( name = "Sherpa_222_NNPDF30NNLO_ggllvvInt"      )
Sherpa_222_NNPDF30NNLO_ggllvvWW        = Sample( name = "Sherpa_222_NNPDF30NNLO_ggllvvWW"       )
Sherpa_222_NNPDF30NNLO_ggllvvZZ        = Sample( name = "Sherpa_222_NNPDF30NNLO_ggllvvZZ"       )
Sherpa_222_NNPDF30NNLO_ggZllZqq        = Sample( name = "Sherpa_222_NNPDF30NNLO_ggZllZqq"       )
Sherpa_222_NNPDF30NNLO_ggZvvZqq        = Sample( name = "Sherpa_222_NNPDF30NNLO_ggZvvZqq"       )
Sherpa_222_NNPDF30NNLO_ggWmlvWpqq      = Sample( name = "Sherpa_222_NNPDF30NNLO_ggWmlvWpqq"     )
Sherpa_222_NNPDF30NNLO_ggWplvWmqq      = Sample( name = "Sherpa_222_NNPDF30NNLO_ggWplvWmqq"     )
  

diboson = Sample( name =   'diboson',
                    tlatex = 'diboson',
                    fill_color = ROOT.kGray+1,
                    line_color =  ROOT.kGray+2,
                    marker_color =  ROOT.kGray+1,
                    #daughters = [
                    #              Sherpa_222_NNPDF30NNLO_llll,          
                    #              Sherpa_222_NNPDF30NNLO_lllv,          
                    #              Sherpa_222_NNPDF30NNLO_llvv,          
                    #              Sherpa_222_NNPDF30NNLO_lvvv,          
                    #              Sherpa_221_NNPDF30NNLO_vvvv,          
                    #              Sherpa_221_NNPDF30NNLO_ZqqZvv,        
                    #              Sherpa_221_NNPDF30NNLO_ZqqZll,        
                    #              Sherpa_221_NNPDF30NNLO_WqqZvv,        
                    #              Sherpa_221_NNPDF30NNLO_WqqZll,        
                    #              Sherpa_221_NNPDF30NNLO_WpqqWmlv,      
                    #              Sherpa_221_NNPDF30NNLO_WplvWmqq,      
                    #              Sherpa_221_NNPDF30NNLO_WlvZqq,        
                    #              Sherpa_222_NNPDF30NNLO_WWW_3l3v_EW6,  
                    #              Sherpa_222_NNPDF30NNLO_WWZ_4l2v_EW6,  
                    #              Sherpa_222_NNPDF30NNLO_WWZ_2l4v_EW6,  
                    #             Sherpa_222_NNPDF30NNLO_WZZ_5l1v_EW6,  
                    #             Sherpa_222_NNPDF30NNLO_WZZ_3l3v_EW6,  
                    #             Sherpa_222_NNPDF30NNLO_ZZZ_6l0v_EW6,  
                    #             Sherpa_222_NNPDF30NNLO_ZZZ_4l2v_EW6,  
                    #             Sherpa_222_NNPDF30NNLO_ZZZ_2l4v_EW6,  
                    #             Sherpa_221_NNPDF30NNLO_6l0v_EW6,      
                    #             Sherpa_221_NNPDF30NNLO_5l1v_EW6,      
                    #             Sherpa_221_NNPDF30NNLO_4l2v_EW6,      
                    #             Sherpa_221_NNPDF30NNLO_3l3v_EW6,      
                    #             Sherpa_221_NNPDF30NNLO_2l4v_EW6,      
                    #             Sherpa_222_NNPDF30NNLO_ggllvvZZ,      
                    #           ],
                ) 

# not available for SUSY3
###Sherpa_222_NNPDF30NNLO_lllljj_EW6,    
###Sherpa_222_NNPDF30NNLO_lllvjj_EW6,    
###Sherpa_222_NNPDF30NNLO_llvvjj_EW6,    
###Sherpa_222_NNPDF30NNLO_llvvjj_ss_EW4, 
###Sherpa_222_NNPDF30NNLO_llvvjj_ss_EW6, 
###Sherpa_222_NNPDF30NNLO_WWZ_3l1v2j_EW6,
###Sherpa_222_NNPDF30NNLO_WZZ_4l2j_EW6,  
###Sherpa_222_NNPDF30NNLO_WZZ_3l1v2j_EW6,
##Sherpa_222_NNPDF30NNLO_ggllll_0M4l130,
##Sherpa_222_NNPDF30NNLO_ggllll_130M4l, 
##Sherpa_222_NNPDF30NNLO_ggllvvInt,     
##Sherpa_222_NNPDF30NNLO_ggllvvWW,     
##Sherpa_222_NNPDF30NNLO_ggZllZqq,      
##Sherpa_222_NNPDF30NNLO_ggZvvZqq,      
##Sherpa_222_NNPDF30NNLO_ggWmlvWpqq,    
##Sherpa_222_NNPDF30NNLO_ggWplvWmqq,    


Pythia8EvtGen_A14NNPDF23LO_DCH200  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH200"  )
Pythia8EvtGen_A14NNPDF23LO_DCH250  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH250"  )  
Pythia8EvtGen_A14NNPDF23LO_DCH300  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH300"  ) 
Pythia8EvtGen_A14NNPDF23LO_DCH350  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH350"  ) 
Pythia8EvtGen_A14NNPDF23LO_DCH400  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH400"  ) 
Pythia8EvtGen_A14NNPDF23LO_DCH450  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH450"  ) 
Pythia8EvtGen_A14NNPDF23LO_DCH500  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH500"  ) 
Pythia8EvtGen_A14NNPDF23LO_DCH550  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH550"  ) 
Pythia8EvtGen_A14NNPDF23LO_DCH600  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH600"  ) 
Pythia8EvtGen_A14NNPDF23LO_DCH650  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH650"  ) 
Pythia8EvtGen_A14NNPDF23LO_DCH700  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH700"  ) 
Pythia8EvtGen_A14NNPDF23LO_DCH750  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH750"  ) 
Pythia8EvtGen_A14NNPDF23LO_DCH800  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH800"  ) 
Pythia8EvtGen_A14NNPDF23LO_DCH850  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH850"  ) 
Pythia8EvtGen_A14NNPDF23LO_DCH900  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH900"  ) 
Pythia8EvtGen_A14NNPDF23LO_DCH950  = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH950"  ) 
Pythia8EvtGen_A14NNPDF23LO_DCH1000 = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH1000" ) 
Pythia8EvtGen_A14NNPDF23LO_DCH1050 = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH1050" ) 
Pythia8EvtGen_A14NNPDF23LO_DCH1100 = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH1100" ) 
Pythia8EvtGen_A14NNPDF23LO_DCH1150 = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH1150" ) 
Pythia8EvtGen_A14NNPDF23LO_DCH1200 = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH1200" ) 
Pythia8EvtGen_A14NNPDF23LO_DCH1250 = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH1250" ) 
Pythia8EvtGen_A14NNPDF23LO_DCH1300 = Sample( name ="Pythia8EvtGen_A14NNPDF23LO_DCH1300" ) 


#-------------------------------------------------------------------------------
# Here we put filtered samples in the global dictionary filtered 
#-------------------------------------------------------------------------------

getFiltered(dijet, "qfakes")
getFiltered(dijet, "gfakes")
getFiltered(dijet, "ufakes")


#-------------------------------------------------------------------------------
# Here we put filtered samples in the global dictionary filtered 
#-------------------------------------------------------------------------------

SUSY3_list = [
              dijet,
              Wtaunu,
              ttbar,
              ttV,
              Zmumu,
              Ztautau,
              diboson,
              Zee,
              singletop,
              Wmunu,
              Wenu,
             ]

SUSY11_list = [
               dijet,
               Wtaunu,
               ttbar,
              ]

#daughters_list = SUSY11_list
daughters_list = SUSY3_list

qfakes = Sample( name =   'qfakes',
                  tlatex = 'quark fakes',
                  fill_color = ROOT.kRed+1,
                  line_color =  ROOT.kRed+2,
                  marker_color =  ROOT.kRed+2,
                  daughters = daughters_list,
                ) 

bfakes = Sample( name =   'bfakes',
                  tlatex = 'b-jet fakes',
                  fill_color = ROOT.kOrange+1,
                  line_color =  ROOT.kOrange+2,
                  marker_color =  ROOT.kOrange+2,
                  daughters = daughters_list,
                ) 

gfakes = Sample( name =   'gfakes',
                  tlatex = 'gluon fakes',
                  fill_color = ROOT.kBlue+1,
                  line_color =  ROOT.kBlue+2,
                  marker_color =  ROOT.kBlue+2,
                  daughters = daughters_list,
                ) 

ufakes = Sample( name =   'ufakes',
                  tlatex = 'unident. fakes',
                  fill_color = ROOT.kGray+1,
                  line_color =  ROOT.kGray+2,
                  marker_color =  ROOT.kGray+2,
                  daughters = daughters_list,
                ) 

#-------------------------------------------------------------------------------
# Collections 
#-------------------------------------------------------------------------------

#---------------------------------
# Samples loaded for SubmitHist.py
#---------------------------------

all_data = [data]

all_mc = []

all_mc += [dijet]
all_mc += [Wtaunu]
#"""
all_mc += [Wenu]
all_mc += [Wmunu]

all_mc += [Zee]
all_mc += [Zmumu]
all_mc += [Ztautau]

all_mc += [diboson]

all_mc += [singletop]
all_mc += [ttV]
#"""
all_mc += [ttbar]

#all_mc += [qfakes]
#all_mc += [bfakes]
#all_mc += [gfakes]
#all_mc += [ufakes]

#all_mc += samples_DCH.root_AtLeastOneTauFilter_DCH
#"""

"""
all_mc += dijet.daughters
all_mc += dijet_qfakes.daughters
all_mc += dijet_gfakes.daughters
all_mc += dijet_ufakes.daughters
"""

"""
all_mc += [Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ0W]
all_mc += [Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ1W]
all_mc += [Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ2W]
all_mc += [Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ3W]
all_mc += [Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ4W]
all_mc += [Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ5W]
all_mc += [Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ6W]
all_mc += [Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ7W]
all_mc += [Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ8W]
all_mc += [Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ9W]
"""

#---------------------------------
# Samples loaded for SubmitPlot.py
#---------------------------------

mc_bkg = []
#"""
mc_bkg.append( singletop )

mc_bkg.append( Wenu )
mc_bkg.append( Wmunu )

mc_bkg.append( Zee ) 
mc_bkg.append( Zmumu )
mc_bkg.append( Ztautau )

#"""
mc_bkg.append( diboson )
mc_bkg.append( Wtaunu )
mc_bkg.append( ttbar )
mc_bkg.append( ttV )


#mc_bkg.append( dijet )
#mc_bkg.append( dijet_qfakes )
#mc_bkg.append( dijet_gfakes )
#mc_bkg.append( dijet_ufakes )

"""
#mc_bkg.append( Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ0W )
mc_bkg.append( Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ1W )
mc_bkg.append( Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ2W )
mc_bkg.append( Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ3W )
mc_bkg.append( Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ4W )
mc_bkg.append( Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ5W )
mc_bkg.append( Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ6W )
mc_bkg.append( Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ7W )
mc_bkg.append( Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ8W )
mc_bkg.append( Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ9W )
"""

# filtered samples
#---------------------------------
mc_fakes_bkg = []
"""
mc_fakes_bkg.append( ttbar_fakes )

mc_fakes_bkg.append( Wenu_fakes )
mc_fakes_bkg.append( Wmunu_fakes )
mc_fakes_bkg.append( Wtaunu_fakes )

mc_fakes_bkg.append( Zee_fakes ) 
mc_fakes_bkg.append( Zmumu_fakes )
mc_fakes_bkg.append( Ztautau_fakes )

#mc_fakes_bkg.append( Wtaunu_qfakes )
#mc_fakes_bkg.append( Wtaunu_gfakes )
#mc_fakes_bkg.append( dijet_qfakes )
#mc_fakes_bkg.append( dijet_gfakes )
"""

#----------------------------------
# Samples loaded for SubmitMerge.py
#----------------------------------

data_merge = [data]

mc_merge = []
mc_merge.append( singletop )

mc_merge.append( Wenu )
mc_merge.append( Wmunu )

#mc_merge.append( Zee ) 
#mc_merge.append( Zmumu )
#mc_merge.append( Ztautau )

#mc_merge.append( diboson )
#mc_merge.append( Wtaunu )
#mc_merge.append( ttbar )
#mc_merge.append( ttV )

#mc_merge.append( dijet )

## EOF
