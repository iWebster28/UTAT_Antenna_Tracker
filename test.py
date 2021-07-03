# Test imports

import sys
sys.path.append('./physical')
import gyro as gy

# Init
gyro_inst = gy.TrackerGyro() # Instantiate tracker gyro

while True:
    tracker_gyro_ENU_spherical = gyro_inst.get_tracker_gyro() # 6. Get gyroscope direction of tracker (ENU_Spherical) (Ian)
    # error_t2d_ENU_spherical = gyro_inst.get_tracker_drone_delta(10, 10) # 7. Find delta angles between current tracker direction & desired direction (Ian)
    print(tracker_gyro_ENU_spherical)
    # print(error_t2d_ENU_spherical)