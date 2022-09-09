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

for i in {0..632..1}
  do
    echo "Processing test-${i}.xyz"
    xtb4stda test-${i}.xyz > test-${i}.xtb4stda
    stda -rpa -xtb -e 10 > test-${i}-std.out
    rm -f ./wfn.xtb
    rm -f ./charges
    rm -f ./charges3
  done
