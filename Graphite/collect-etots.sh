#!/bin/bash

# For initial and with stricter convergence 

outfile=C.scf.out
for dim_plane in $(cat dims_plane.txt); do 
    for dim_vert in $(cat dims_vert.txt); do
        dir_name="C_plane${dim_plane}_vert${dim_vert}"

        echo "Extracting energies from $dir_name"

        cd $dir_name
        grep -e '     total energy' -e '!    ' C.scf.out  \
        | awk '{print $(NF-1)}' > etots.txt

        cd -
    done
done