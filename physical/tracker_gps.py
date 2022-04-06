# gps.py
# GPS module in the Antenna tracker. 
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

def get_ecef_tracker():
    # TODO: To be pulled from antenna tracker GPS (Hitansh)
    llh = np.array([0,0,0])
    tracker_ECEF = co.llh_to_ecef(llh)
    print("ECEF of antenna tracker: \n{:>20} {:>20} {:>20}".format(*tracker_ECEF))
    return tracker_ECEF