#!/usr/bin/env python3
from scripts.bands import *
import os

PARENT_DIR = os.path.dirname(os.path.abspath(__file__))
plt.style.use(PARENT_DIR + '/scripts/default.mplstyle')

def get_fermiEnergy(dos_file):
    # reading first line
    with open(dos_file, 'r') as f:
        first_line = f.readline()
    print(first_line)
    fermiEnergy = float(first_line.split()[-2])
    return fermiEnergy

main_dir = PARENT_DIR + "/C_plane4.641_vert2.726/"
dos_file = main_dir + "C.dos.dat"
bandsfile = main_dir + "Bands/C.dat.gnu"


symmetryfile = main_dir + "Bands/C.pp.out"

datafile='si.bands.dat.gnu'

fermi = get_fermiEnergy(dos_file)
print(fermi)
bool_shift_efermi= True
fig, ax = plt.subplots()

fermi = 5.889

#bndplot(datafile,fermi,symmetryfile,ax)
bndplot(bandsfile, fermi, symmetryfile, ax, shift_fermi=1,\
color='black',linestyle='solid',name_k_points=['M','G','K','G'])
#plt.ylim((-9, 0))
plt.xlabel("Wavevector")
plt.tight_layout()
fig.savefig(PARENT_DIR + "/../report/figs/ass4_bands.png", dpi=300)
plt.show()