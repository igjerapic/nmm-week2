#!/bin/bash
#SBATCH -J C_DOS
#SBATCH -o %j.out
#SBATCH -p parallel
#SBATCH -N 1
#SBATCH -n 12
#SBATCH -t 00:30:00

module load QuantumESPRESSO/7.1-foss-2022a
srun dos.x < C.dos.in > C.dos.out
