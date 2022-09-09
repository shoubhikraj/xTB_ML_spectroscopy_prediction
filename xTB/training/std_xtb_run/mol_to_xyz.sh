#!/bin/bash

for i in {0..2499..1}
  do
    echo "Converting train-${i}.mol to train-${i}.xyz"
    obabel -imol -oxyz ../final_xtb_opt/train-${i}.mol -O ./train-${i}.xyz
  done
