#!/bin/bash

# create directories based on the parameter space defined in text files
for dim_plane in $(cat dims_plane.txt); do 
    for dim_vert in $(cat dims_vert.txt); do
        bash create_dir.sh $dim_plane $dim_vert 
    done
done