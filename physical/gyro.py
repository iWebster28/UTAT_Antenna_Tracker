import glbs as g
import numpy as np

if not g.SW_SIMULATION:
    from MinIMU_v5_pi import MinIMU_v5_pi
class TrackerGyro():
    def __init__(self):
        """
        Initialize IMU for gyro functionality
        test_angle in radians
        """
        if g.SW_SIMULATION:
            print("SW_SIMULATION mode. No TrackerGyro init. Set self.test_angle = [0.0, 0.0]")
            self.test_angle = [(np.pi/180.0) * g.fake_motor_phi_deg, (np.pi/180.0) * g.fake_motor_lambda_deg]
        else:
            self.IMU = MinIMU_v5_pi()
            self.IMU.trackAngle()

    def get_tracker_gyro(self):
        """
        Return poll result for ENU_spherical angles from Antenna Tracker gyro
        in format [x_axis, y_axis] (ignore z_axis).
        Return in radians.
        """
        # TODO: higher poll rate, and read average of prev. queue of data points.
        if g.SW_SIMULATION:
            print("SW_SIMULATION mode. Return [g.fake_motor_phi, g.fake_motor_lambda] for TrackerGyro poll.")
            return [(np.pi/180.0) * g.fake_motor_phi_deg, (np.pi/180.0) * g.fake_motor_lambda_deg]
        else:
            return [(np.pi/180.0) * self.IMU.prevAngle[0][0], (np.pi/180.0) * self.IMU.prevAngle[0][0]] #only return [x_axis, y_axis] (ignore z_axis)

