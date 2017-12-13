[![Build Status](https://travis-ci.org/kbsezginel/thermof.svg?branch=master)](https://travis-ci.org/kbsezginel/thermof)
[![codecov](https://codecov.io/gh/kbsezginel/thermof/branch/master/graph/badge.svg)](https://codecov.io/gh/kbsezginel/thermof)

Thermal transport in MOFs (thermof)
===================================
Investigating thermal transport in metal-organic frameworks.

<p align="center"> <img src="https://raw.githubusercontent.com/kbsezginel/thermof/master/docs/img/Fig1.png"> </p>

-   a) Idealized porous crystal (8 × 8 × 8 cubic unit cells), single unit cell highlighted in red
-   b) Bonding arrangement for single unit cell using Morse potential (red bonds are modeled stronger than blue bonds)
-   c) Doubly interpenetrated unit cells with framework depicted as red and blue (initial frameworks in each simulation are 5 Å apart in each dimension
-   d) Interpenetrated idealized porous crystal (8 × 8 × 8 cubic unit cells).

Installation
------------
First, install [lammps_interface](https://github.com/kbsezginel/lammps_interface) Python package:

```bash
git clone https://github.com/kbsezginel/lammps_interface
cd lammps_interface
python setup.py install
```

Then, clone the repository, enter the main repository directory and run setup:

```bash
git clone https://github.com/kbsezginel/thermof.git
cd thermof
python setup.py install
```

Usage
-----
thermof library can be used to initialize, run, and analyze simulation results to investigate thermal transport in porous crytals. Here sample files for an idealized cubic MOF along with an interpenetrated version are provided (see Figure 1). Using these files Molecular Dynamics simulations can be run with [Lammps].

### Command-line interface

TherMOF can be used with the command-line interface (CLI) provided in this repository. The CLIs are installed as console scripts by default. Alternatively, you can find the scripts in `thermof/cli`.

#### Initializing LAMMPS simulations

A thermal conductivity calculation input files for LAMMPS can be generated for a `cif` file with the `thermof_write` CLI as follows:
```
thermof_write myMOF.cif
```
This would create a directory (`myMOF`) in the same directory as the cif file containing LAMMPS input files. Currently only `P1` symmetry is accepted. An example cif file can be found in `thermof/sample/MOF5.cif`.


Using the `--help` flag more information about the CLI (such as selecting force field, cell size) can be obtained:
```
thermof_write --help
```

#### Analyzing LAMMPS simulations

After running LAMMPS simulations the resuts can be analyzed and plotted with the `thermof_read` CLI as follows:
```
thermof_read /path/to/simulation
```
Here `/path/to/simulation` is the name of the directory that contains simulation results.

Using the `--help` flag more information about the CLI (such as selecting plots, parameters) can be obtained:
```
thermof_read --help
```

### Sample
Sample [Lammps] input files for thermal conductivity calculations can be found in `thermof/sample`

-   in3_ipmof.cond.sample: Interpenetrated MOF simulation parameters with 3D thermal flux
-   in3_single.cond.sample: Single MOF simulation parameters with 3D thermal flux
-   in_ipmof.cond.sample: Interpenetrated MOF simulation parameters with 1D thermal flux
-   lammps_ipmof.data.sample: Interpenetrated MOF structure file
-   lammps_ipmof_metal.data.sample: Interpenetrated MOF with differemt corner atoms structure file
-   lammps_single.data.sample: Single MOF structure file
-   lammps_single_metal.data.sample: Single MOF with differemt corner atoms structure file
-   lammps_qsub.sh.sample: Job submission script for lammps simulations on [Frank]

### Notebooks
Example jupyter notebooks can be found in `/notebooks`

-   change_trajectory: Change xyz trajectory atoms names
-   initialize: Initialize Lammps simulation files according to selected simulation parameters
-   interpenetrate: Create interpenetrated structure
-   read_simulation: Read and plot thermal conductivity Lammps simulation results

-------------------------------------------------------------------------
[Lammps]: http://lammps.sandia.gov/ "Lammps home page"
[Frank]: http://core.sam.pitt.edu/frank "Frank home page"
