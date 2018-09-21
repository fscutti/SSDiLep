import os
import re

## need to replace these strings in the output
## WARNING: order is important -> substrings should go last !!!
mcstrings = []
mcstrings.append(["",""])

def recreplace(s=None,l=[]):
  ns = s
  for x in l: ns = ns.replace(x[0],x[1])
  return ns


def prepare_sample_list(dic={}):
  
  sample_dic={}
  for k,v in dic.iteritems():

    sample_id = None
    run_id = None
    if "physics_Main" in k: 
      sample_id = k.split(".")[6]+"_"+k.split(".")[7]
      run_id = k.split(".")[9]
    else: 
      sample_id = k.split(".")[6]
      run_id = k.split(".")[8]
    
    if not sample_id in sample_dic.keys(): 
      sample_dic[sample_id] = [str(v)]
    else: 
      prefix = str(v).split("."+run_id,1)[0]
      
      remove_sample = ""

      for s in sample_dic[sample_id]:
        # the prefix includes the sample id + container tags
        s_prefix = s.split(".r",1)[0]
        s_version = re.search('%s.r(.*)_'%(s_prefix), s).group(1)
        
        if not prefix in s: continue
        else:
          if int(run_id.split("r")[1]) > int(s_version): remove_sample = s
          else: remove_sample = str(v)
            
      sample_dic[sample_id].append(str(v))
      
      if remove_sample in sample_dic[sample_id]: sample_dic[sample_id].remove(remove_sample)      
  
  return sample_dic




def build_strings(isType="mc15",channel=None,sample=None,type=None,rTag=None,pTag=None,use_ami=False,OUTTAG=None):
  
  dataset = []
  assert isType in ["mc15","data15","data16"], "ERROR: dataset type not supported!!! Must be in [mc15, data15, data16]"
  if isType == "mc15": dataset    += ["mc15_13TeV"]
  elif isType == "data15": dataset      += ["data15_13TeV"]
  elif isType == "data16": dataset      += ["data16_13TeV"]
  if channel: dataset += [str(channel)]
  else: dataset       += ["*"]
  if sample: dataset  += ["*"+str(sample)+"*"]
  else: dataset       += ["*"]
  if type: dataset    += [str(type)]
  else: dataset       += ["*"]
  
  fname = filter(lambda i: i != "*", dataset)
  fname = "_".join(fname)
  fname = fname.replace("*","")

  string = ".".join(dataset)+"."
  
  if rTag: 
    assert isType, "ERROR: rTag requested but sample is data"
    string += "*%s*" % rTag
    fname  +=  "_%s" % rTag
  if pTag: 
    string += "*%s*" % pTag
    fname  += "_%s" % pTag
  
  string += "*" 
  fname  += ".txt"
  
  # wildcarding in use_ami
  if use_ami:
    string = string.replace("*","%")
    while "%%" in string: string = string.replace("%%","%")
  
  if OUTTAG: fname = "_".join([OUTTAG,fname])
  
  return {"search_string":string,"file_name":fname}
