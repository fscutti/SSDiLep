import os
import sys
import subprocess

from pyutils.utils import recreplace, mcstrings, prepare_sample_list
            
from ssdilep.samples import samples

import os
from collections import defaultdict

def prepare_path(path):
    if not os.path.exists(path):
        print 'preparing outpath: %s'%(path)
        os.makedirs(path)

folder = "SUSY3MC.v3"
#folder = "SUSY3Data.v3"


indir     = "/coepp/cephfs/share/atlas/MLA/"+folder+"/merged/nominal"
outdir    = "/coepp/cephfs/share/atlas/MLA/"+folder+"/group/nominal"

OUTLOGS   = os.path.join("/coepp/cephfs/share/atlas/MLA/"+folder+"","group_log","nominal")

prepare_path(outdir)
prepare_path(OUTLOGS)

QUEUE          = "long"
NCORES         = 1
SCRIPT         = os.path.join("/coepp/cephfs/mel/fscutti/Analysis/batch","Group.sh")

samples_list = []

if "Data" in folder: samples_list = samples.data_merge
elif "MC" in folder: samples_list = samples.mc_merge

for s in samples_list:
  s_merge = []
  for d in s.daughters:
    for root, dirs, files in os.walk(indir): 
      for f in files:
          if d.name in f:
            s_merge.append(os.path.join(root,f))
  
  outfile  = os.path.join(outdir,s.name+".root")
  job_name = s.name

  vars=[]
  vars+=["NCORES=%d"   % NCORES            ]
  vars+=["OUTFILE=%s"  % outfile           ]
  vars+=["INPUTS=%s"   % " ".join(s_merge) ]
  
  VARS = ','.join(vars)
  
  cmd = 'qsub'
  cmd += ' -l nodes=1:ppn=%d' % NCORES
  cmd += ' -q %s'             % QUEUE
  cmd += ' -v "%s"'           % VARS
  cmd += ' -N j.group.%s'     % job_name
  cmd += ' -j n -o %s'        % OUTLOGS
  cmd += ' -e %s'             % OUTLOGS
  cmd += ' %s'                % SCRIPT
   
  print cmd
  print
  
  m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
  print m.communicate()[0]
