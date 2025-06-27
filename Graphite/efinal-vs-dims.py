import os 
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('scripts/default.mplstyle')


def main():
    # reading in parameter space
    dims_plane = np.loadtxt("dims_plane.txt").T 
    dims_vert = np.loadtxt("dims_vert.txt").T

    # generating mesh from parameter space
    DIMS_PLANE, DIMS_VERT = np.meshgrid(dims_plane, dims_vert)

    # collecting efinals from the Output of the SCF sims
    efinals = np.zeros_like(DIMS_PLANE)
    for i, dim_plane in enumerate(dims_plane):
        for j, dim_vert in enumerate(dims_vert):
            outfile = f"C_plane{dim_plane}_vert{dim_vert}/C.scf.out"
            cmd = "grep -e ! " + outfile+ " | awk '{print $(NF-1)}'"

            efinal = float(os.popen(cmd).read()[:-1]) # last character is new line '\n'
            efinals[i,j] = efinal

    fig, ax= plt.subplots(figsize=(5,5))

    c = ax.pcolormesh(DIMS_PLANE, DIMS_VERT, efinals, cmap='RdBu', vmin=efinals.min(), vmax=efinals.max())
    fig.colorbar(c, ax=ax, label = ("Engery (Ry)"))
    ax.set_yticks(dims_vert)
    ax.set_xticks(dims_plane)
    ax.set_xlabel("a (Bohr)")
    ax.set_ylabel("c/a")
    plt.tight_layout()
    plt.savefig("../report/figs/ass4_energies.png", dpi=300)
    plt.show()
if __name__ == "__main__":
    main()