import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler


plt.style.use('scripts/default.mplstyle')

plt.rcParams['axes.prop_cycle'] = plt.cycler(cycler(color = [
                                    '#332288', 
                                    '#CC6677', 
                                    '#88CCEE',
                                    '#DDCC77', 
                                    '#117733', 
                                    '#882255', 
                                    '#44AA99', 
                                    '#999933', 
                                    '#AA4499',
                                    '#DDDDDD'
                                ]))
def get_fermiEnergy(file):
    # reading first line
    with open(file, 'r') as f:
        first_line = f.readline()
    
    fermiEnergy = float(first_line.split()[-2])
    return fermiEnergy

def get_bandGap(energies, dos, fermiEnergy = 0):

    energies_lower = energies[energies < fermiEnergy]
    energies_above = energies[energies > fermiEnergy]

    energy_above = energies_above[dos[energies > fermiEnergy] > 0][0]
    energy_lower = energies_lower[dos[energies < fermiEnergy] > 0][-1]

    print(energy_lower, energy_above)

    band_gap = energy_above - energy_lower

    return band_gap

def main():
    # load data
    file = "Si_10.4/Si.dos.dat"
    fermiEnergy = get_fermiEnergy(file)

    energy, dos, idos = np.loadtxt(file, unpack=True)

    # centering around Fermi energy
    energy -= fermiEnergy

    band_gap = get_bandGap(energy, dos, fermiEnergy = 0.1)
    print(band_gap)
    # make plot
    plt.figure(figsize = (12, 6))
    plt.plot(energy, dos, linewidth=0.75, color='C1')
    
    # Showing filled states
    plt.fill_between(energy, 0, dos, where=(energy < 0), facecolor='C1', alpha=0.25)

    # indicating Fermi energy
    plt.axvline(x=0, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
    plt.text(0.25, 1.5, 'Fermi energy', fontsize= 15, rotation=90)

    # Adjusting Plot axes
    plt.yticks([])
    plt.xlabel('Energy (eV)')
    plt.ylabel('DOS')
    plt.xlim(-10, 10)
    plt.ylim(0, )
    plt.tight_layout()
    plt.savefig("report/figs/ass2_dos.png", dpi = 300)
    plt.show()

if __name__ == "__main__":
    main()