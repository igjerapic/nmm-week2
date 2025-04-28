#!/bin/bash

rm etot-v-lat_const
for lat_const in 9.8 10.0 10.26  10.4 10.6; do
    dir_name="Si_${lat_const}"
    outfile="$dir_name/Si.scf.out"
    
    etot=$(grep -e ! $outfile | awk '{print $(NF-1)}')
    
    echo "$lat_const    $etot" >> etot-v-lat_const
done
