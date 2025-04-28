import numpy as np
import matplotlib.pyplot as plt
import os 

from cycler import cycler


#plt.style.use('scripts/default.mplstyle')

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

def plot_convergence(file):
    etots = np.loadtxt("si.etot_conv_1d-12").T
    iteratiosn= np.arange()

def main():

    dims_plane = np.loadtxt("dims_plane.txt").T
    dims_vert = np.loadtxt("dims_vert.txt").T

    fig, ax = plt.subplots(dims_plane.size, dims_vert.size, figsize=(50,50))
    for i, dim_plane in enumerate(dims_plane):
        for j,  dim_vert in enumerate(dims_vert):
            sim_label = f"C_plane{dim_plane}_vert{dim_vert}"

            file = sim_label + "/etots.txt" 
            etots = np.loadtxt(file).T
            iterations = np.arange(1,len(etots) + 1)

            ax[i,j].plot(iterations, etots)
            ax[i,j].set_title(sim_label)
    
    fig.supxlabel("Iteration")
    fig.supylabel("Total Energy (Ry)")
    plt.tight_layout()

    plt.show()
    # plt.savefig("etot_conv_1d-12.svg", dpi=200)

if __name__=="__main__":
    main()