from MinIMU_v5_pi import MinIMU_v5_pi

<<<<<<< HEAD
class gryo():
    def __init__(self):
=======
class TrackerGyro():
    def __init__(self):
        """
        Initialize IMU for gyro functionality
        """
>>>>>>> 8baf596e850ab894bb49c1b22ee8265113feab95
        self.IMU = MinIMU_v5_pi()
        self.IMU.trackAngle()

    def get_tracker_gyro(self):
        """
<<<<<<< HEAD
        Poll ENU_spherical angles from Antenna Tracker gyro
        """
        return self.IMU.prevAngle[0]

def get_tracker_drone_delta(delta_t2d_ENU_spherical, tracker_gyro_ENU_spherical):
    """
    Determine the delta between tracker and drone positions in ENU_spherical
    """
    return (delta_t2d_ENU_spherical - tracker_gyro_ENU_spherical)
=======
        Return poll result for ENU_spherical angles from Antenna Tracker gyro
        in format [x_axis, y_axis, z_axis]
        """
        # Todo: higher poll rate, and read average of prev. queue of data points.
        return self.IMU.prevAngle[0]
>>>>>>> 8baf596e850ab894bb49c1b22ee8265113feab95
