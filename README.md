# Tutorial 2
For this and following tutorials: some relevant scripts will be in these repositories, but a more complete version can also be found in the Habrok /scratch/hb-nanoscale folder.

The topic of this session will be to optimize the lattice parameters and calculate the electronic properties of bulk materials. You will need to use XCrysDen or the online tool that you tried last week to visualize your structures. 

## Assignment 1

We will start with the DFT calculation of bulk Si. This exercise will consist of the lattice constant optimization and the calculations of the density of states (DOS). Last week, you ran the file 'Si.scf.in', and you got familiar with the input parameters and output files. Now, we will continue with the same input file and set up the calculations to optimize the lattice constant of Si. 

### Instructions

1a. First, input files with different lattice constants should be prepared. If you are familiar with bash or python scripting, you can easily automate the file preparation and running. Otherwise, create four empty directories called ‘Si_<lattice_constant>’ using the following set of lattice constants {9.8, 10.0, 10.4, 10.6}. Note that the values in parentheses are expressed in atomic units in accordance with the requirements of QE. Convert them to angstroms (for yourself) to make sure that you know what you are doing. 

Copy the file ‘Si.scf.in’, the pseudopotential file, and the submission script to each directory. Open each of these files using an editor and change the value of the parameter celldm(1) to a corresponding value of lattice constant. Run the job script in each directory.

Once all four calculations are finished, first control that they terminated correctly and then type 
grep ‘!    total energy’ Si.scf.out to check the values of total energy for each lattice constant. Write these values to a file, including the one calculated initially with the lattice constant of 10.26 a.u. 

1b. Use your favorite tool (for example, python, Gnuplot, or if you really want to, MS Excel) to plot the lattice constant vs the total energy curve. Write down the value of the lattice constant for which you see the minimum. Does the optimized lattice constant agree with the experimental value? Compare with the literature. 

## Assignment 2

Now, we will perform density of states (DOS) calculations for the bulk silicon. 

### Instructions

2a. Copy the files ‘Si.nscf.in’ and ‘Si.dos.in’ to the directory containing calculations with the optimized lattice constant. Make sure that celldm(1) in these files is equal to the optimized lattice constant. Run the non-self-consistent calculation using the file ‘Si.nscf.in’. Note that the k-mesh is much larger than in the previous runs and a longer time will be required to finish the calculation. When the calculation is terminated successfully, run the file ‘Si.dos.in’ using the script 'dos.sh'. 

2b. The result will be written in a file ‘Si.dos.dat’ containing three columns and the value of Fermi energy at the beginning of the file. Plot energy vs dos(E) using your favorite plotting tool, for example, Gnuplot, Python, or if you really want, in Excel. Don’t forget to shift the Fermi energy printed at the beginning of the file. For example, type ‘module load gnuplot’, then ‘gnuplot’ and then use the command:
plot 'Si.dos.dat' using ($1-<Fermi_energy>):2 with lines

Compare the result with the plot below. Does it agree? Based on the calculated DOS, would you classify crystalline Si as an insulator, a semiconductor, or a metal?

![Test](/images/dos.png)

## Assignment 3

Finally, we will calculate the electronic structure of Si along the high symmetry lines in the Brillouin zone.

### Instructions

3a. Let us first visualize the Brillouin zone and the high-symmetry points. To this aim, type ‘xcrysden’ and open again the file ‘Si.scf.in’. Then, go to Tools and choose k-path Selection. Explore the shape of the Brillouin zone. Does it look as you expected?
Alternatively, you can use an online tool at https://tools.materialscloud.org/seekpath/, this time the left-hand panel. The high-symmetry points in the BZ of Si will be already displayed. 

Now, create a new directory and call it Bands. Copy to it the entire directory Si.save by typing ‘cp -r Si.save Bands’. 
Copy the file ‘Si.bands.in’ and ‘Si.pp.in’ into the directory Bands. 
Open the file Si.bands.in and check the last lines describing the coordinates of high-symmetry points. Are you able to identify them in the visualized Brillouin zone?

Run the calculations for bands, using the script 'bands.sh'. 

Once the calculation is terminated correctly – check the job status and the end of the ‘Si.bands.out’ file – run the postprocessing calculation with the input file 'Si.pp.in'. Use the script 'bands.pp.sh'. 

When the calculation is done, you will see the band structure files in various formats. The quickest way to visualize the band structure is to use ‘Si.dat.gnu’. You can simply call Gnuplot and type: 

plot 'Si.dat.gnu' using 1:($2-<Fermi_energy>) with lines

Alternatively, you can write your own python script to get a nicer figure. You should see the occupied part of the spectrum similar to the one below. Does it agree with the literature?

![Test](/images/bands.png)

## Assignment 4

Repeat the exercises 1-3 to analyze the properties of graphite - a bulk van der Waals material consisting of graphene layers. The following parameters might be useful for constructing your Quantum Espresso file:

```bash
&system  
    ibrav  = 4
    celldm(1)= 4.641 
    celldm(3)= 2.726

ATOMIC_POSITIONS {alat}
C      0.000 0.000 0.000
C      0.000 0.577 0.000
C      0.000 0.000 1.363
C      0.500 0.288 1.363
```

Note: Graphite is a van der Waals material, so using at least a semi-empirical van der Waals correction (DFT-D2) is suggested for the structure optimization. 

Calculate your band structure along M-G-K-M direction. Does it agree with the literature?
