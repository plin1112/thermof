"""
Tests center of mass and mean square displacement for Trajectory class
"""
import os
import numpy as np
from thermof import Trajectory


mof_trial_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ideal-mof-trial')
ipmof_trial_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ip-mof-trial')


def test_center_of_mass_for_single_ideal_mof():
    """ Test trajectory class read method for non-interpenetrated ideal MOF """
    traj = Trajectory(read=os.path.join(mof_trial_dir, 'Run1', 'traj.xyz'))
    traj.change_atoms({'1': 'C'})
    traj.get_com()
    assert np.isclose(traj.com[0][0], traj.com[0][1], traj.com[0][2])


def test_center_of_mass_for_interpenetrated_ideal_mof():
    """ Test trajectory class read method for interpenetrated ideal MOF """
    traj = Trajectory(read=os.path.join(ipmof_trial_dir, 'Run1', 'traj.xyz'))
    traj.change_atoms({'1': 'C', '2': 'O'})
    traj.get_com()
    assert np.isclose(traj.com[0][0], traj.com[0][1], traj.com[0][2])
