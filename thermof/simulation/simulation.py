# Date: August 2017
# Author: Kutay B. Sezginel
"""
Simulation class for reading and initializing Lammps simulations
"""
import os
import pprint
from thermof.parameters import Parameters
from thermof.read import read_run, read_trial, read_trial_set, read_framework_distance
from thermof.initialize.lammps import write_lammps_files, write_lammps_input
from thermof.initialize.job import job_submission_file
from thermof.mof import MOF
from .plot import plot_simulation


class Simulation:
    """
    Reading and initializing Lammps simulations
    """
    def __init__(self, read=None, setup=None, parameters=None, mof=None):
        """
        Create a Lammps simulation object.
        """
        if parameters is None:
            self.parameters = Parameters()
        else:
            self.parameters = parameters
        if read is not None and setup is not None:
            self.read(read, setup)
            self.setup = setup
            self.simdir = read
        elif mof is not None:
            self.set_mof(mof)
        self.verbose = True

    def __repr__(self):
        """
        Returns basic simulation info
        """
        return "<Simulation | setup: %s | total runs: %i>" % (self.setup, len(self))

    def __str__(self):
        """
        Returns name of directory the results were read from
        """
        return self.name

    def __len__(self):
        """
        Returns number of total runs in simulation
        """
        if self.setup == 'run':
            n_runs = 1
        elif self.setup == 'trial':
            n_runs = len(self.trial['runs'])
        elif self.setup == 'trial_set':
            n_runs = 0
            for trial in self.trial_set['trials']:
                n_runs += len(self.trial_set['data'][trial]['runs'])
        return n_runs

    def read(self, simdir, setup='run'):
        """
        Read Lammps simulation results from given directory.
        """
        self.setup = setup
        self.simdir = simdir
        self.name = os.path.basename(simdir)
        if setup == 'run':
            self.run = read_run(simdir, k_par=self.parameters.k)
        elif setup == 'trial':
            self.trial = read_trial(simdir, k_par=self.parameters.k)
        elif setup == 'trial_set':
            self.trial_set = read_trial_set(simdir, k_par=self.parameters.k)
        else:
            print('Select setup: "run" | "trial" | "trial_set"')

    def initialize(self):
        """
        Initialize input files for a Lammps simulation.
        """
        write_lammps_files(self.simdir, self.parameters, verbose=self.verbose)
        write_lammps_input(self.simdir, self.parameters, verbose=self.verbose)
        job_submission_file(self.simdir, self.parameters, verbose=self.verbose)
        print('Done!') if self.verbose else None

    def set_mof(self, mof_file):
        """
        Set MOF file for Lammps simulation
        """
        self.mof = MOF(mof_file)
        self.parameters.lammps['cif_file'] = self.mof.path
        self.parameters.job['name'] = self.mof.name
        self.parameters.job['input'] = 'in.%s' % self.mof.name
        rep = [int(i) for i in self.parameters.lammps['replication'].split()]
        self.parameters.thermof['mof'] = dict(name=self.mof.name,
                                              replication=rep,
                                              volume=self.mof.ase_atoms.get_volume() * rep[0] * rep[1] * rep[2])

    def plot(self, selection, data=None):
        """
        Plot Lammps simulation results.
        """
        plot_simulation(self, selection, data)

    def show_parameters(self, par=None):
        """
        Show selected simulation parameters.
        """
        self.parameters.show(par=par)
