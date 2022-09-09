#!/bin/bash

module load xtb

mkdir scratch
for i in {0..19..1}
  do
    echo "Processing ffopt-bench-${i}.mol"
    cp ../preliminary_ff_opt/ffopt-bench-${i}.mol ./scratch
    cd scratch
    xtb ffopt-bench-${i}.mol --opt tight
    mv ./xtbopt.mol ../bench-${i}.mol
    cd ..
    rm -f ./scratch/*
  done
rm -f ./scratch/.xtboptok
rmdir ./scratch/
