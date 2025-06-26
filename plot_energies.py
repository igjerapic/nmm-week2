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

def main():
    lattice_const, energies = np.loadtxt("etot-v-lat_const").T
    lattice_const *= 0.529177249 # Converting to Angstrom 
    idx = np.where(energies == min(energies))[0][0]
    print(lattice_const[idx])

    plt.plot(lattice_const, energies, "o:")
    plt.xlabel("Lattice const ($\AA$)")
    plt.ylabel("Total Energy (Ry)")
    plt.xticks(lattice_const, [f"{lat:.2f}" for lat in lattice_const])
    plt.tight_layout()
    plt.savefig("report/figs/ass1_etot-vs-lat_const.png", dpi=300)
    #plt.show()

if __name__ == "__main__":
    main()