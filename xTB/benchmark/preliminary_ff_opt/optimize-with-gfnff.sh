#!/bin/bash

module load xtb

mkdir scratch
for i in {0..19..1}
  do
    echo "Processing pre-bench-${i}.mol"
    cp ../generated_molfiles/pre-bench-${i}.mol ./scratch
    cd scratch
    xtb pre-bench-${i}.mol --gfnff --opt tight
    mv ./xtbopt.mol ../ffopt-bench-${i}.mol
    cd ..
    rm -f ./scratch/*
  done
rm -f ./scratch/.xtboptok
rmdir ./scratch/
