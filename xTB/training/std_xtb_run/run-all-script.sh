#!/bin/bash
#$ -q all.q
#$ -N xtbstdarun
#$ -l fat
#$ -pe smp 4
#$ -o $HOME/logs
#$ -S /bin/bash -cwd -j y

set host=`hostname -s`
set OMP_NUM_THREADS=4
module load stda

cd $SGE_O_WORKDIR

for i in {0..2499..1}
  do
    echo "Processing bench-${i}.xyz"
    xtb4stda train-${i}.xyz > train-${i}.xtb4stda
    stda -rpa -xtb -e 10 > train-${i}-std.out
    rm -f ./wfn.xtb
    rm -f ./charges
    rm -f ./charges3
  done
