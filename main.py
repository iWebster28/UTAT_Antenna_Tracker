# Revised tracker

# Functional Summary and Assignment
# 1. Get ECEF of antenna tracker (only once at beginning) (Michelangelo)
# 2. Get ECEF of drone (Jun Ho)
# 3. Find delta ECEF of drone & tracker (makes tracker origin, but directions are still in ECEF) (Jun Ho)
# 4. Use rotation matrix to rotate origin of our tracker coordinates to point north (ECEF -> ENU_XYZ Which axis is north will depend on code) (Stephen)
# 5. Convert our delta drone coordinates to spherical (ENU_XYZ -> ENU_Spherical) (Stephen)
# 6. Get gyroscope direction of tracker (ENU_Spherical) (Ian)
# 7. Find delta angles between current tracker direction & desired direction (Ian)
# 8. Output direction to motors to desired direction (Stephen)

import sys
sys.path.append('./physical')
from gyro import get_tracker_gyro

def main():
    # t2d: tracker to drone
    tracker_ECEF = [x_t, y_t, z_t]
    drone_ECEF = [x_d, y_d, z_d]
    delta_t2d_ECEF = [x_del, y_del, z_del]

    delta_t2d_ENU_spherical = [t2d_phi, t2d_lambda]
    tracker_gyro_ENU_spherical = [gyro_phi, gyro_lambda]
    error_t2d_ENU_spherical = [error_phi, error_lambda]

    # Init
    tracker_ECEF = get_ecef_tracker() # 1. Get ECEF of antenna tracker (only once at beginning) (Michelangelo)

    # Loop
    drone_ECEF = get_ecef_drone() # 2. Get ECEF of drone (Jun Ho)
    delta_t2d_ECEF = get_delta_t2d_ECEF(tracker_ECEF, drone_ECEF) # 3. Find delta ECEF of drone & tracker (makes tracker origin, but directions are still in ECEF) (Jun Ho)

    delta_ENU_XYZ = ecef_to_ENU_XYZ(delta_t2d_ECEF) # 4. Use rotation matrix to rotate origin of our tracker coordinates to point north (ECEF -> ENU_XYZ Which axis is north will depend on code) (Stephen)
    delta_t2d_ENU_spherical = ecef_to_spherical(delta_ENU_XYZ) # 5. Convert our delta drone coordinates to spherical (ENU_XYZ -> ENU_Spherical) (Stephen)
    # Note: just need the delta_phi and delta_lambda. Don't need R; only care about angles.

    tracker_gyro_ENU_spherical = get_tracker_gyro() # 6. Get gyroscope direction of tracker (ENU_Spherical) (Ian)

    error_t2d_ENU_spherical = get_tracker_drone_delta(delta_t2d_ENU_spherical, tracker_gyro_ENU_spherical) # 7. Find delta angles between current tracker direction & desired direction (Ian)

    # 8. Output direction to motors to desired direction (Stephen)
    move_tracker(error_t2d_ENU_spherical)

    return


if __name__ == "__main__":
    main()