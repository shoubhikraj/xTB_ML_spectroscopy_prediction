#!/bin/bash

module load xtb

mkdir scratch
for i in {0..2499..1}
  do
    echo "Processing pre-train-${i}.mol"
    cp ../generated_molfiles/pre-train-${i}.mol ./scratch
    cd scratch
    xtb pre-train-${i}.mol --gfnff --opt tight > /dev/null
    mv ./xtbopt.mol ../ffopt-train-${i}.mol
    cd ..
    rm -f ./scratch/*
  done
rm -f ./scratch/.xtboptok
rmdir ./scratch/
