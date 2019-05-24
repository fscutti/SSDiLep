import os
import sys
import subprocess

from pyutils.utils import recreplace, mcstrings, prepare_sample_list
            
from SamplesID import SampleID

import os
from collections import defaultdict


folder = "SUSY3Data.v3"


indir_tree     = "/coepp/cephfs/share/atlas/MLA/"+folder+"/tree/nominal"
indir_metadata = "/coepp/cephfs/share/atlas/MLA/"+folder+"/metadata/nominal"
indir_cutflow  = "/coepp/cephfs/share/atlas/MLA/"+folder+"/cutflow/nominal"

outdir         = "/coepp/cephfs/share/atlas/MLA/"+folder+"/merged/nominal"

OUTLOGS        = os.path.join("/coepp/cephfs/share/atlas/MLA/"+folder+"","log","nominal")


QUEUE          = "long"
NCORES         = 1
SCRIPT         = os.path.join("/coepp/cephfs/mel/fscutti/Analysis/batch","Merge.sh")

files_dict     = defaultdict(list)
jname_dict     = defaultdict(str)

sample_name = 3
sample_id = 2
if "Data" in folder:
 sample_name = 2
 sample_id = 2

for tree in os.listdir(indir_tree):         
  #sname = tree.split(".")[sample_name]
  #sid   = tree.split(".")[sample_id]
  
  sname = "00282992"
  sid   = "00282992"
  
  #sname = "00281075"
  #sid   = "00281075"
  
  if not sname in tree: continue

  jname_dict[os.path.join(outdir, "physics_Main_" + sname + ".root")        ] = sid
  files_dict[os.path.join(outdir, "physics_Main_" + sname + ".root")        ].append(os.path.join(indir_tree,tree))

for metadata in os.listdir(indir_metadata): 
  #sname = metadata.split(".")[sample_name]
  sname = "00282992"
  #sname = "00281075"

  if not sname in metadata: continue
  files_dict[os.path.join(outdir, "physics_Main_" + sname + ".root")].append(os.path.join(indir_metadata,metadata))

for cutflow in os.listdir(indir_cutflow):   
  #sname = cutflow.split(".")[sample_name]
  sname = "00282992"
  #sname = "00281075"

  if not sname in cutflow: continue
  files_dict[os.path.join(outdir, "physics_Main_" + sname + ".root")  ].append(os.path.join(indir_cutflow,cutflow))


for outfile, inputs in files_dict.iteritems():
  
  job_name = jname_dict[outfile]

  vars=[]
  vars+=["NCORES=%d"     % NCORES          ]
  vars+=["OUTFILE=%s"    % outfile         ]
  vars+=["INPUTS=%s"   % " ".join(inputs)  ]
  
  VARS = ','.join(vars)
  
  cmd = 'qsub'
  cmd += ' -l nodes=1:ppn=%d' % NCORES
  cmd += ' -q %s'             % QUEUE
  cmd += ' -v "%s"'           % VARS
  cmd += ' -N j.merge.%s'     % job_name
  cmd += ' -j n -o %s'        % OUTLOGS
  cmd += ' -e %s'             % OUTLOGS
  cmd += ' %s'                % SCRIPT
   
  print cmd
  print
  #m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
  #print m.communicate()[0]

