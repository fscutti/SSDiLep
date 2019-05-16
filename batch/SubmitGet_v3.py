import os
import sys
import subprocess

from pyutils.utils import recreplace, mcstrings, prepare_sample_list
            
from SamplesID import SampleID

from optparse import OptionParser

parser = OptionParser()
parser.add_option('-s', '--samp', dest='sample',
                  help='sample name',metavar='SAMP',default="")
parser.add_option('-c', '--camp', dest='campaign',
                  help='campaign name',metavar='CAMP',default="")

(options, args) = parser.parse_args()

# prototype of sample name
# user.tadej.MLA.SUSY3.v3.dilep.Wjets_MC16a.r1
# user.tadej.MLA.SUSY3.v3.dilep.Data_16.r1
# user.tadej.MLA.SUSY3.v3.dilep.DCH_MC16a_fast.r1


# -------------
# main analysis
# -------------
#"""
user      = "tadej"
analysis  = "MLA"
deriv     = "SUSY3"
version   = "v3"
type      = "dilep"
sample    = options.sample
campaign  = options.campaign
rep       = "r1"
#"""

# -------------
# fakes
# -------------
"""
user      = "tadej"
analysis  = "MLA"
deriv     = "SUSY11"
version   = "v3"
type      = "fakes"
sample    = options.sample
campaign  = options.campaign
rep       = "r1"
"""

container = "user.{}.{}.{}.{}.{}.{}_{}.{}".format(user,analysis,deriv,version,type,sample,campaign,rep)

sys   = None
if not sys: sys = "nominal"

SCRIPT     = os.path.join("/coepp/cephfs/mel/fscutti/Analysis/batch","Get_v3.sh")

campaign_folder = ""
if "MC" in campaign: campaign_folder = "MC"
if "period" in campaign: campaign_folder = "Data"

OUTDIR     = "/coepp/cephfs/share/atlas/{}/{}{}.{}".format(analysis,deriv,campaign_folder,version)

OUTMERGED  = os.path.join(OUTDIR,"merged",sys)
OUTTREE    = os.path.join(OUTDIR,"tree",sys)
OUTMETA    = os.path.join(OUTDIR,"metadata",sys)
OUTCUTFLOW = os.path.join(OUTDIR,"cutflow",sys)
OUTLOGS    = os.path.join(OUTDIR,"log",sys)
QUEUE      = "long"
NCORES     = 1

JOBDIR    = "/coepp/cephfs/mel/fscutti/jobdir" 

dir_list = []
dir_list.append(JOBDIR)
dir_list.append(os.path.join(OUTDIR,"tree"))
dir_list.append(os.path.join(OUTDIR,"tree",sys))
dir_list.append(os.path.join(OUTDIR,"metadata"))
dir_list.append(os.path.join(OUTDIR,"metadata",sys))
dir_list.append(os.path.join(OUTDIR,"cutflow"))
dir_list.append(os.path.join(OUTDIR,"cutflow",sys))
dir_list.append(os.path.join(OUTDIR,"merged"))
dir_list.append(os.path.join(OUTDIR,"merged",sys))
dir_list.append(os.path.join(OUTDIR,"log"))
dir_list.append(os.path.join(OUTDIR,"log",sys))

for d in dir_list:
 if not os.path.exists(d):
   os.makedirs(d)

outjobs_tree     = "{}_tree.txt".format(container)
outjobs_metadata = "{}_metadata.txt".format(container)
outjobs_cutflow  = "{}_cutflow.txt".format(container)

outjobs_tree     = recreplace(outjobs_tree,[["*","X"]])
outjobs_metadata = recreplace(outjobs_metadata,[["*","X"]])
outjobs_cutflow  = recreplace(outjobs_cutflow,[["*","X"]])

infile_tree     = os.path.join(JOBDIR,outjobs_tree)
infile_metadata = os.path.join(JOBDIR,outjobs_metadata)
infile_cutflow  = os.path.join(JOBDIR,outjobs_cutflow)

with open(infile_tree,"w") as f:
  cmd = "rucio list-files"
  #cmd += " %s.%s:" % ("user",user)
  cmd += " {}_tree.root".format(container)
  print cmd
  m = subprocess.Popen(cmd,shell=True,stdout=f)
  print m.communicate()[0]
f.close()

with open(infile_metadata,"w") as f:
  cmd = "rucio list-files"
  #cmd += " %s.%s:" % ("user",user)
  cmd += " {}_metadata.root".format(container)
  print cmd
  m = subprocess.Popen(cmd,shell=True,stdout=f)
  print m.communicate()[0]
f.close()

with open(infile_cutflow,"w") as f:
  cmd = "rucio list-files"
  #cmd += " %s.%s:" % ("user",user)
  cmd += " {}_cutflow.root".format(container)
  print cmd
  m = subprocess.Popen(cmd,shell=True,stdout=f)
  print m.communicate()[0]
f.close()


out_tree = {}
out_metadata = {}
out_cutflow = {}


with open(infile_tree) as f:
  for line in f:
    if not "user" in line: continue
    key = line.split(".")[3]
    if not key in out_tree:
      out_tree[key] = [line.split("|")[1].replace(" ","")]
    else:
      out_tree[key] += [line.split("|")[1].replace(" ","")]
f.close()

with open(infile_metadata) as f:
  for line in f:
    if not "user" in line: continue
    key = line.split(".")[3]
    if not key in out_metadata:
      out_metadata[key] = [line.split("|")[1].replace(" ","")]
    else:
      out_metadata[key] += [line.split("|")[1].replace(" ","")]
f.close()

with open(infile_cutflow) as f:
  for line in f:
    if not "user" in line: continue
    key = line.split(".")[3]
    if not key in out_cutflow:
      out_cutflow[key] = [line.split("|")[1].replace(" ","")]
    else:
      out_cutflow[key] += [line.split("|")[1].replace(" ","")]
f.close()



for k in out_tree.keys():

  for i, sample in enumerate(out_tree[k]):
     job_name = "{}_{}_s{}".format(k,campaign,i)
     
     vars=[]
     vars+=["NCORES=%d"        % NCORES             ]
     vars+=["TREEFILE=%s"      % out_tree[k][i]     ]
     vars+=["METAFILE=%s"      % out_metadata[k][i] ]
     vars+=["CUTFLOWFILE=%s"   % out_cutflow[k][i]  ]
     vars+=["OUTTREE=%s"       % OUTTREE            ]
     vars+=["OUTMETA=%s"       % OUTMETA            ]
     vars+=["OUTCUTFLOW=%s"    % OUTCUTFLOW         ]
     
     VARS = ','.join(vars)
     
     cmd = 'qsub'
     cmd += ' -l nodes=1:ppn=%d' % NCORES
     cmd += ' -q %s'             % QUEUE
     cmd += ' -v "%s"'           % VARS
     cmd += ' -N j.get.%s'       % job_name
     cmd += ' -j n -o %s'        % OUTLOGS
     cmd += ' -e %s'             % OUTLOGS
     cmd += ' %s'                % SCRIPT
      
     print cmd
     print
     m = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
     print m.communicate()[0]
