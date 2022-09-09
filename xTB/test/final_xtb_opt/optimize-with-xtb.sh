#!/bin/bash
#$ -q all.q
#$ -N xtbstdarun
#$ -l fat
#$ -pe smp 4
#$ -o $HOME/logs
#$ -S /bin/bash -cwd -j y

set host=`hostname -s`
set OMP_NUM_THREADS=4
module load xtb

mkdir scratch
for i in {0..632..1}
  do
    echo "Processing ffopt-test-${i}.mol"
    cp ../preliminary_ff_opt/ffopt-test-${i}.mol ./scratch
    cd scratch
    xtb ffopt-test-${i}.mol --opt tight
    mv ./xtbopt.mol ../test-${i}.mol
    cd ..
    rm -f ./scratch/*
  done
rm -f ./scratch/.xtboptok
rmdir ./scratch/
