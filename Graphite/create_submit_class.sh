#!/bin/bash

dim_plane=$1
dim_vert=$2

dir_name="C_plane${dim_plane}_vert${dim_vert}"
slurm_script="$dir_name/quantum.qsub"
echo "Creating SLURM script in $dir_name"

cat > "$slurm_script" <<EOL
#!/bin/bash
#SBATCH -J QE_C_plane${dim_plane}_vert${dim_vert}
#SBATCH -o %j.out
#SBATCH -p parallel
#SBATCH -N 1
#SBATCH -n 12
#SBATCH -t 00:20:00
#SBATCH --reservation=nanoscale

module load QuantumESPRESSO/7.1-foss-2022a
srun pw.x < C.scf.in > C.scf.out
EOL

chmod +x "$slurm_script"
