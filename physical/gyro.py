from MinIMU_v5_pi import MinIMU_v5_pi

class TrackerGyro():
    def __init__(self):
        """
        Initialize IMU for gyro functionality
        """
        self.IMU = MinIMU_v5_pi()
        self.IMU.trackAngle()

    def get_tracker_gyro(self):
        """
        Return poll result for ENU_spherical angles from Antenna Tracker gyro
        in format [x_axis, y_axis, z_axis]
        """
        # Todo: higher poll rate, and read average of prev. queue of data points.
        return self.IMU.prevAngle[0]

