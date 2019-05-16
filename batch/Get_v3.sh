#!/bin/bash
#PBS -S /bin/bash
#PBS -l walltime=24:00:00
#PBS -l pmem=1gb


STARTTIME=`date +%s`
date

echo 
echo "Environment variables..."
echo " User name:     $USER"
echo " User home:     $HOME"
echo " Queue name:    $PBS_O_QUEUE"
echo " Job name:      $PBS_JOBNAME"
echo " Job-id:        $PBS_JOBID"
echo " Work dir:      $PBS_O_WORKDIR"
echo " Submit host:   $PBS_O_HOST"
echo " Worker node:   $HOSTNAME"
echo " parameters passed: $*"
echo 


echo " Temp dir:      $JOBTMP"

echo " SCRIPT:        $SCRIPT"
echo " TREEFILE:      $TREEFILE"
echo " METAFILE:      $METAFILE"
echo " CUTFLOWFILE:   $CUTFLOWFILE"
echo " OUTTREE:       $OUTTREE"
echo " OUTMETA:       $OUTMETA"
echo " OUTCUTFLOW:    $OUTCUTFLOW"
echo " NCORES:        $NCORES"

echo
export 

# ----------------
# This is the job!
# ----------------

export X509_USER_PROXY=/coepp/cephfs/mel/fscutti/jobdir/x509up_u1132
setupATLAS

# -----------------------------
# avoid to fuck the cluster up:
# -----------------------------


cgcreate -a ${USER}:people -t ${USER}:people -g cpu,memory:user/${USER}/${PBS_JOBID}
MEMLIMIT="$((3 * ${NCORES}))"
echo "${MEMLIMIT}g" > /cgroup/memory/user/${USER}/${PBS_JOBID}/memory.limit_in_bytes
echo $$ > /cgroup/memory/user/${USER}/${PBS_JOBID}/tasks


echo "executing job..."

# -------------------
# download with rucio
# -------------------
lsetup rucio

# tree file
# ---------
echo "-----> rucio download ${TREEFILE} --dir=${OUTTREE}"
rucio download ${TREEFILE} --dir=${OUTTREE}

# meta file
# ---------
echo "-----> rucio download ${METAFILE} --dir=${OUTMETA}"
rucio download ${METAFILE} --dir=${OUTMETA}

# cutflow file
# ------------
echo "-----> rucio download ${CUTFLOWFILE} --dir=${OUTCUTFLOW}"
rucio download ${CUTFLOWFILE} --dir=${OUTCUTFLOW}

# EOF

