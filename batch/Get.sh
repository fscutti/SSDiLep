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
#echo " Temp dir:      $TMPDIR"
echo " parameters passed: $*"
echo 


echo " Temp dir:      $JOBTMP"

echo " SCRIPT:        $SCRIPT"
echo " TREEFILE:      $TREEFILE"
echo " METAFILE:      $METAFILE"
echo " CUTFLOWFILE:   $CUTFLOWFILE"
echo " MERGEDTREE:    $MERGEDTREE"
echo " MERGEDMETA:    $MERGEDMETA"
echo " MERGEDCUTFLOW: $MERGEDCUTFLOW"
echo " OUTTREE:       $OUTTREE"
echo " OUTMETA:       $OUTMETA"
echo " OUTCUTFLOW:    $OUTCUTFLOW"
echo " MERGED:        $MERGED"
echo " OUTMERGED:     $OUTMERGED"
echo " NCORES:        $NCORES"

echo
export 

MYDIR=Get_${RANDOM}${RANDOM}

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

echo "-----> mkdir ${JOBTMP}/${MYDIR} "
mkdir ${JOBTMP}/${MYDIR} 

echo "-----> ls ${JOBTMP} -la"
ls ${JOBTMP} -la

echo "-----> cd ${JOBTMP}/${MYDIR} "
cd ${JOBTMP}/${MYDIR} 

# -------------------
# download with rucio
# -------------------
lsetup rucio

# tree file
# ---------
echo "-----> rucio download --dir=${JOBTMP}/${MYDIR} ${TREEFILE}"
rucio download --dir=${JOBTMP}/${MYDIR} ${TREEFILE}

echo "-----> ls ${JOBTMP}/${MYDIR}/*_tree.root -la"
ls ${JOBTMP}/${MYDIR}/*_tree.root -la

echo "-----> cp -rf ${JOBTMP}/${MYDIR}/*_tree.root ${OUTTREE}"
cp -rf ${JOBTMP}/${MYDIR}/*_tree.root ${OUTTREE}

# meta file
# ---------
echo "-----> rucio download --dir=${JOBTMP}/${MYDIR} ${METAFILE}"
rucio download --dir=${JOBTMP}/${MYDIR} ${METAFILE}

echo "-----> ls ${JOBTMP}/${MYDIR}/*_metadata.root -la"
ls ${JOBTMP}/${MYDIR}/*_metadata.root -la

echo "-----> cp -rf ${JOBTMP}/${MYDIR}/*_metadata.root ${OUTMETA}"
cp -rf ${JOBTMP}/${MYDIR}/*_metadata.root ${OUTMETA}

# cutflow file
# ------------
echo "-----> rucio download --dir=${JOBTMP}/${MYDIR} ${CUTFLOWFILE}"
rucio download --dir=${JOBTMP}/${MYDIR} ${CUTFLOWFILE}

echo "-----> ls ${JOBTMP}/${MYDIR}/*_cutflow.root -la"
ls ${JOBTMP}/${MYDIR}/*_cutflow.root -la

echo "-----> cp -rf ${JOBTMP}/${MYDIR}/*_cutflow.root ${OUTCUTFLOW}"
cp -rf ${JOBTMP}/${MYDIR}/*_cutflow.root ${OUTCUTFLOW}


# --------------
# hadd with root
# --------------
#lsetup root
lsetup "root 6.14.04-x86_64-slc6-gcc62-opt"

replace=".root/*.root*"

TREEFILE=${TREEFILE//.root/$replace}
METAFILE=${METAFILE//.root/$replace}
CUTFLOWFILE=${CUTFLOWFILE//.root/$replace}


# tree file
# ---------
echo "-----> hadd ${MERGEDTREE} ${TREEFILE}"
hadd ${MERGEDTREE} ${TREEFILE}

echo "-----> rm -rf ${JOBTMP}/${MYDIR}/*_tree.root/"
rm -rf ${JOBTMP}/${MYDIR}/*_tree.root/

echo "-----> ls ${JOBTMP}/${MYDIR} -la"
ls ${JOBTMP}/${MYDIR} -la


# meta file
# ---------
echo "-----> hadd ${MERGEDMETA} ${METAFILE}"
hadd ${MERGEDMETA} ${METAFILE}

echo "-----> rm -rf ${JOBTMP}/${MYDIR}/*_metadata.root/"
rm -rf ${JOBTMP}/${MYDIR}/*_metadata.root/

echo "-----> ls ${JOBTMP}/${MYDIR} -la"
ls ${JOBTMP}/${MYDIR} -la


# cutflow file
# ------------
echo "-----> hadd ${MERGEDCUTFLOW} ${CUTFLOWFILE}"
hadd ${MERGEDCUTFLOW} ${CUTFLOWFILE}

echo "-----> rm -rf ${JOBTMP}/${MYDIR}/*_cutflow.root/"
rm -rf ${JOBTMP}/${MYDIR}/*_cutflow.root/

echo "-----> ls ${JOBTMP}/${MYDIR} -la"
ls ${JOBTMP}/${MYDIR} -la


# ----------------------
# merge cutflow and tree
# ----------------------
echo "-----> hadd ${MERGED} ${MERGEDTREE} ${MERGEDMETA} ${MERGEDCUTFLOW}"
hadd ${MERGED} ${MERGEDTREE} ${MERGEDMETA} ${MERGEDCUTFLOW}


echo "-----> ls ${JOBTMP}/${MYDIR} -la"
ls ${JOBTMP}/${MYDIR} -la

echo "-----> cp ${MERGED} ${OUTMERGED}"
cp ${MERGED} ${OUTMERGED}

echo "-----> cd ${JOBTMP}"
cd ${JOBTMP}

echo "-----> rm -rf ${MYDIR}"
rm -rf ${MYDIR}

echo "-----> ls ${JOBTMP} -la"
ls ${JOBTMP} -la

# EOF

