#!/bin/bash

lat_const=$1
dir_name="Si_${lat_const}"
slurm_script="$dir_name/quantum.qsub"
echo "Creating SLURM script in $dir_name"

cat > "$slurm_script" <<EOL
#!/bin/bash
#SBATCH -J QE_Si_${lat_const}
#SBATCH -o %j.out
#SBATCH -p parallel
#SBATCH -N 1
#SBATCH -n 12
#SBATCH -t 00:20:00
#SBATCH --reservation=nanoscale

module load QuantumESPRESSO/7.1-foss-2022a
srun pw.x < Si.scf.in > Si.scf.out
EOL

chmod +x "$slurm_script"
