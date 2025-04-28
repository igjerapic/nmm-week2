#!/bin/bash

# Go to each simulation directory and create a C.scf.in file based on the ecutwfc, nk-points, and conv_thr 

ecut=40.0
nk=4
conv_thr="1.0d-8"

dim_plane=$1
dim_vert=$2

potential_file="$(pwd)/scripts/C.pbe-rrkjus.UPF"

dir_name="C_plane${dim_plane}_vert${dim_vert}"
input_script="$dir_name/C.scf.in"

echo "Creating PW input script and copying PW potenial file in $dir_name"


cp $potential_file $dir_name/C.pbe-rrkjus.UPF

cat > "$input_script" <<EOL
 &control
    calculation = 'scf'
    restart_mode='from_scratch',
    prefix='C',
    pseudo_dir = './'
    outdir = './'
 /
 &system    
    ibrav=  4, 
    celldm(1)= ${dim_plane}, 
    celldm(3)= ${dim_vert}, 
    nat=  4, 
    ntyp= 1,
    ecutwfc= 40.0
    vdw_corr= 'DF-D3'
 /
 &electrons
    mixing_mode = 'plain'
    mixing_beta = 0.7 
    conv_thr =  1.0d-8
 /

ATOMIC_SPECIES
 C  12.011  C.pbe-rrkjus.UPF
ATOMIC_POSITIONS (alat)
C      0.000 0.000 0.000
C      0.000 0.577 0.000
C      0.000 0.000 1.363
C      0.500 0.288 1.363 
K_POINTS {automatic}
  4 4 4 1 1 1
EOL
