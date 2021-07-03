from MinIMU_v5_pi import MinIMU_v5_pi

class gryo():
    def __init__(self):
        self.IMU = MinIMU_v5_pi()
        self.IMU.trackAngle()

    def get_tracker_gyro(self):
        """
        Poll ENU_spherical angles from Antenna Tracker gyro
        """
        return self.IMU.prevAngle[0]

def get_tracker_drone_delta(delta_t2d_ENU_spherical, tracker_gyro_ENU_spherical):
    """
    Determine the delta between tracker and drone positions in ENU_spherical
    """
    return (delta_t2d_ENU_spherical - tracker_gyro_ENU_spherical)