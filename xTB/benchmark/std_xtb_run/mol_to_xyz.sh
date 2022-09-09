#!/bin/bash

for i in {0..19..1}
  do
    echo "Converting bench-${i}.mol to bench-${i}.xyz"
    obabel -imol -oxyz ../final_xtb_opt/bench-${i}.mol -O ./bench-${i}.xyz
  done
