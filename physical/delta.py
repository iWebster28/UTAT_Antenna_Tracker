import numpy as np

def get_delta_t2d_ECEF(tracker_ECEF, drone_ECEF):
    """
    Determine the delta between tracker and drone positions in ENU_spherical
    """
    # Absolute diff? or imply direction
    delta_t2d_ECEF = np.subtract(drone_ECEF, tracker_ECEF)
    print("Delta ECEF of drone & tracker: \n{:>20} {:>20} {:>20}".format(*delta_t2d_ECEF))
    return delta_t2d_ECEF

def get_tracker_drone_delta(delta_t2d_ENU_spherical, tracker_gyro_ENU_spherical):
    # Absolute diff? or imply direction
    error_t2d_ENU_spherical = np.subtract(delta_t2d_ENU_spherical, tracker_gyro_ENU_spherical)
    print("Delta angles between current tracker direction & desired direction:\n{:>20} {:>20}".format(*error_t2d_ENU_spherical))
    return error_t2d_ENU_spherical