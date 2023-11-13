#!/bin/bash
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=4

cd $SLURM_SUBMIT_DIR

echo "Master node: $(hostname)"
echo "Configuration for the HPL.dat as follows:"
cat HPL.dat


# mpirun /clusterfs/common/hpl-2.3/testing/xhpl



mpiexec /clusterfs/usr/bin/python3 temp.py
