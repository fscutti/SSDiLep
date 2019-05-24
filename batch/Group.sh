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


echo " SCRIPT:        $SCRIPT"
echo " OUTFILE:       $OUTFILE"
echo " INPUTS:        $INPUTS"
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

# --------------
# hadd with root
# --------------
#lsetup root
lsetup "root 6.14.04-x86_64-slc6-gcc62-opt"

echo "-----> hadd ${OUTFILE} ${INPUTS}"
hadd ${OUTFILE} ${INPUTS}

# EOF

