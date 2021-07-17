def get_tracker_drone_delta(delta_t2d_ENU_spherical, tracker_gyro_ENU_spherical):
    """
    Determine the delta between tracker and drone positions in ENU_spherical
    """
    return (delta_t2d_ENU_spherical - tracker_gyro_ENU_spherical)