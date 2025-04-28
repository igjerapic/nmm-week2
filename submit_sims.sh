#!/bin/bash

# For initial and with stricter convergence 

for lat_const in 9.8 10.0 10.4 10.6; do
    dir_name="Si_${lat_const}"
    echo "submitting simulation in $dir_name"

    (cd $dir_name && sbatch quantum.qsub)
done
