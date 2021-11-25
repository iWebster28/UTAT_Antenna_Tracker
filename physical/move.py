import glbs as g
import numpy as np
class Motors():
    def __init__(self, num_motors=2):
        # TODO: populate this
        self.motor_pins = [g.MOTOR_PIN_1, g.MOTOR_PIN_2, g.MOTOR_PIN_3, g.MOTOR_PIN_4]
        self.motor_states = [0 for i in range(num_motors)]

    def move_tracker(self, error_t2d_ENU_spherical):
        print("Moving motors to desired direction:\nphi:{:>20} lambda:{:>20}".format(*error_t2d_ENU_spherical))
        if g.SW_SIMULATION:
            # just move tracker gyro to desired direction at 5RPM
            # TODO: fix this bug. Need to consider direction + or -
            if (error_t2d_ENU_spherical[0] > g.MAX_ERROR_PHI_DEG):
                g.fake_motor_phi_deg += g.MAX_RPM_PHI * g.LOOP_UPDATE_SEC
            if (error_t2d_ENU_spherical[1] > g.MAX_ERROR_LAMBDA_DEG):
                g.fake_motor_lambda_deg += g.MAX_RPM_LAMBDA * g.LOOP_UPDATE_SEC
            print(f"Simulation mode: motors moved to: {(np.pi/180) *  g.fake_motor_phi_deg} and {(np.pi/180) * g.fake_motor_lambda_deg}")
        return