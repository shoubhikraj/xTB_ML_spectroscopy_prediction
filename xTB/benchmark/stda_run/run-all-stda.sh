#!/bin/bash

# cp ../std_xtb_run/*.xyz ./

for i in {0..19..1}
  do
    echo "Processing bench-${i}.xyz"
    xtb4stda bench-${i}.xyz > /dev/null
    stda -xtb -e 10 > bench-${i}-stda.out
    rm -f ./wfn.xtb
    rm -f ./charges
    rm -f ./charges3
  done
