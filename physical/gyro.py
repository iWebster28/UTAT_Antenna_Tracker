
SW_SIMULATION = True # No HW
if not SW_SIMULATION:
    from MinIMU_v5_pi import MinIMU_v5_pi
class TrackerGyro():
    def __init__(self):
        """
        Initialize IMU for gyro functionality
        """
        if SW_SIMULATION:
            print("SW_SIMULATION mode. No TrackerGyro init.")
        else:
            self.IMU = MinIMU_v5_pi()
            self.IMU.trackAngle()

    def get_tracker_gyro(self):
        """
        Return poll result for ENU_spherical angles from Antenna Tracker gyro
        in format [x_axis, y_axis, z_axis]
        """
        # Todo: higher poll rate, and read average of prev. queue of data points.
        if SW_SIMULATION:
            print("SW_SIMULATION mode. Return 1 for TrackerGyro poll.")
            return 1
        else:
            return self.IMU.prevAngle[0]

