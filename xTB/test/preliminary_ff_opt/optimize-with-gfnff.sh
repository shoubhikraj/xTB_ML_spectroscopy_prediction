#!/bin/bash

module load xtb

mkdir scratch
for i in {0..632..1}
  do
    echo "Processing pre-test-${i}.mol"
    cp ../generated_molfiles/pre-test-${i}.mol ./scratch
    cd scratch
    xtb pre-test-${i}.mol --gfnff --opt tight > /dev/null
    mv ./xtbopt.mol ../ffopt-test-${i}.mol
    cd ..
    rm -f ./scratch/*
  done
rm -f ./scratch/.xtboptok
rmdir ./scratch/
