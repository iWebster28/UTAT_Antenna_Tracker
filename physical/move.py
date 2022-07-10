# move.py
# A library to control DC motors on the Antenna Tracker.
# Author(s): Ian Webster
# Date: Nov 2021

import glbs as g
import numpy as np
import RPi.GPIO as gpio

import time

class Motors():
    def __init__(self, num_motors=2):
        # TODO: populate this according to HW.
        self.n_motors = num_motors
        self.motor_pins = [g.MOTOR_PIN_1, g.MOTOR_PIN_2, g.MOTOR_PIN_3, g.MOTOR_PIN_4]
        self.motor_states = [0 for i in range(num_motors)]
        self.motor_ids = [i for i in range(num_motors)]

        # Initialize GPIO pins if not running simulation
        if not g.SW_SIMULATION:
            self.init_gpio()

    def init_gpio(self):
        gpio.setmode(gpio.BCM)
        for i in range(self.n_motors):
            if(g.DEBUG_MODE):
                print("setting GPIO mode for pins "+str(i<<1)+", "+str((i<<1)+1))
            gpio.setup(self.motor_pins[(i<<1)],gpio.OUT)
            gpio.setup(self.motor_pins[(i<<1)+1],gpio.OUT)

    def __del__(self):
        if(g.DEBUG_MODE):
            print("deleting motor object, cleaning GPIO")
        gpio.cleanup()

    def move_tracker(self, error_t2d_ENU_spherical):
        print("Moving motors to desired direction:\nphi:{:>20} lambda:{:>20}".format(*error_t2d_ENU_spherical))

        # Software simulation. Improve this for actual implementation.
        if g.SW_SIMULATION:
            # For now, just move tracker gyro to desired direction at 5RPM

            # TODO: fix this bug. Need to consider direction + or -
            if (error_t2d_ENU_spherical[0] > g.MAX_ERROR_PHI_DEG):
                g.fake_motor_phi_deg += g.MAX_RPM_PHI * g.LOOP_UPDATE_SEC
            if (error_t2d_ENU_spherical[1] > g.MAX_ERROR_LAMBDA_DEG):
                g.fake_motor_lambda_deg += g.MAX_RPM_LAMBDA * g.LOOP_UPDATE_SEC
            print(f"Simulation mode: motors moved to: {(np.pi/180.0) *  g.fake_motor_phi_deg} and {(np.pi/180.0) * g.fake_motor_lambda_deg}")
        else:
            
            pass

        return

    def move_motor(self, motor_id, direction):
        # direction: 0 or 1
        # TODO: add calibration code to figure out which direction 0 or 1 is (left vs right, CCW vs CW)
#        c_motor_pins = (motor_pins[(motor_id-1)<<1,(motor_id-1)<<1)
        if(g.DEBUG_MODE):
            print("moving motor "+str(motor_id)+" in direction "+str(direction))
        gpio.output(self.motor_pins[(motor_id<<1)],direction)
        gpio.output(self.motor_pins[(motor_id<<1)+1],not direction)

if __name__=="__main__":
    g.init()
    m_obj = Motors(1)
    m_obj.move_motor(0, 0)
    time.sleep(10)
