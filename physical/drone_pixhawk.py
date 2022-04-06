# gps.py
# Pixhawk GPS module in the Antenna tracker.
# TODO: create a class.
# Author(s): Ian Webster
# Date: Nov 2021 

import os
import sys
import numpy as np

# Include libraries
subdirs = [
    "physical",
    "utils"
]

for dir in subdirs:
    sys.path.append(os.path.join(os.getcwd(), dir))

import glbs as g

import coordinates as co

def get_ecef_drone():
    # TIODO: To be pulled from drone pixhawk (Jun Ho)
    llh = np.array([0,1,0])
    drone_ECEF = co.llh_to_ecef(llh)
    print("ECEF of drone: \n{:>20} {:>20} {:>20}".format(*drone_ECEF))
    return drone_ECEF