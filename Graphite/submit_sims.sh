#!/bin/bash

# For initial and with stricter convergence 

for dim_plane in $(cat dims_plane.txt); do 
    for dim_vert in $(cat dims_vert.txt); do
        dir_name="C_plane${dim_plane}_vert${dim_vert}"

        echo "submitting simulation in $dir_name"

        (cd $dir_name && sbatch quantum.qsub)
    done
done
