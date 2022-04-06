# main.py

# Functional Summary and Assignment
# 1. Get ECEF of antenna tracker (only once at beginning) (Hitansh)
# 2. Get ECEF of drone (Jun Ho)
# 3. Find delta ECEF of drone & tracker (makes tracker origin, but directions are still in ECEF) (Jun Ho)
# 4. Use rotation matrix to rotate origin of our tracker coordinates to point north (ECEF -> ENU_XYZ Which axis is north will depend on code) (Stephen)
# 5. Convert our delta drone coordinates to spherical (ENU_XYZ -> ENU_Spherical) (Stephen)
# 6. Get gyroscope direction of tracker (ENU_Spherical) (Ian)
# 7. Find delta angles between current tracker direction & desired direction (Ian)
# 8. Output direction to motors to desired direction (Stephen)

import os
import sys

# Include libraries
subdirs = [
    "physical",
    "utils"
]

for dir in subdirs:
    sys.path.append(os.path.join(os.getcwd(), dir))

import glbs as g
g.init()

import gyro as gy
import delta as dl
import coordinates as co
from move import Motors
import tracker_gps
import drone_pixhawk

import numpy as np
from time import sleep

def main():
    # t2d: tracker to drone
    # tracker_ECEF = [x_t, y_t, z_t]
    # drone_ECEF = [x_d, y_d, z_d]
    # delta_t2d_ECEF = [x_del, y_del, z_del]

    # delta_t2d_ENU_spherical = [t2d_phi, t2d_lambda]
    tracker_gyro_ENU_spherical = [g.MAX_ERROR_PHI_DEG + 1, g.MAX_ERROR_LAMBDA_DEG + 1] # [gyro_phi, gyro_lambda]
    # error_t2d_ENU_spherical = [error_phi, error_lambda]

    # Init
    gyro_inst = gy.TrackerGyro() # Instantiate tracker gyro
    motors_inst = Motors() # Instantiate motors
    tracker_ECEF = tracker_gps.get_ecef_tracker() # 1. Get ECEF of antenna tracker (only once at beginning) (Hitansh)

    error_t2d_ENU_spherical = [1, 1] # init

    # TODO: add a safety stop.
    # Loop
    while (True):
        drone_ECEF = drone_pixhawk.get_ecef_drone() # 2. Get ECEF of drone (Jun Ho)
        delta_t2d_ECEF = dl.get_delta_t2d_ECEF(tracker_ECEF, drone_ECEF) # 3. Find delta ECEF of drone & tracker (makes tracker origin, but directions are still in ECEF) (Jun Ho)

        delta_ENU_XYZ = co.conv_ecef_enu(delta_t2d_ECEF) # 4. Use rotation matrix to rotate origin of our tracker coordinates to point north (ECEF -> ENU_XYZ Which axis is north will depend on code) (Stephen)
        delta_t2d_ENU_spherical = co.enu_cart_to_enu_sphere(delta_ENU_XYZ)[:-1] # 5. Convert our delta drone coordinates to spherical (ENU_XYZ -> ENU_Spherical) (Stephen)
        # Note: just need the delta_phi and delta_lambda. Don't need R; only care about angles.

        tracker_gyro_ENU_spherical = gyro_inst.get_tracker_gyro() # 6. Get gyroscope direction of tracker (ENU_Spherical) (Ian)

        error_t2d_ENU_spherical = dl.get_tracker_drone_delta(delta_t2d_ENU_spherical, tracker_gyro_ENU_spherical) # 7. Find delta angles between current tracker direction & desired direction (Ian)

        # 8. Output direction to motors to desired direction (Stephen)
        motors_inst.move_tracker(error_t2d_ENU_spherical)

        if ((error_t2d_ENU_spherical[0] < g.MAX_ERROR_PHI_DEG) \
         and (error_t2d_ENU_spherical[1] < g.MAX_ERROR_LAMBDA_DEG)):
            break
        
        sleep(g.LOOP_UPDATE_SEC)
        
    return

if __name__ == "__main__":
    main()
