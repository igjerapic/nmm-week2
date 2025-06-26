#!/bin/bash
#SBATCH -J Si_DOS
#SBATCH -o %j.out
#SBATCH -p parallel
#SBATCH -N 1
#SBATCH -n 12
#SBATCH -t 00:30:00

module load QuantumESPRESSO/7.1-foss-2022a
srun dos.x < Si.dos.in > Si.dos.out
