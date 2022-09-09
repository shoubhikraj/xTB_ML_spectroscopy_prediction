#!/bin/bash

for i in {0..632..1}
  do
    echo "Converting test-${i}.mol to test-${i}.xyz"
    obabel -imol -oxyz ../final_xtb_opt/test-${i}.mol -O ./test-${i}.xyz
  done
