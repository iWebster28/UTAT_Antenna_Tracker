
def init():
    # General
    global SW_SIMULATION 
    SW_SIMULATION = False #True # No HW

    # Enable debug print messages
    global DEBUG_MODE
    DEBUG_MODE = True 

    # --- Tracker ---

    # H-bridge motor pins
    global MOTOR_PIN_1, MOTOR_PIN_2, MOTOR_PIN_3, MOTOR_PIN_4

    # TODO: populate this according to HW.
    MOTOR_PIN_1 = 23
    MOTOR_PIN_2 = 24
    MOTOR_PIN_3 = 2
    MOTOR_PIN_4 = 3

    global MAX_PHI_SEC, MAX_LAMBDA_SEC
    global PHI_RANGE_DEG, LAMBDA_RANGE_DEG
    global MAX_RPM_PHI, MAX_RPM_LAMBDA

    MAX_PHI_SEC = 20.0
    MAX_LAMBDA_SEC = 40.0 

    PHI_RANGE_DEG = 90.0
    LAMBDA_RANGE_DEG = 360.0
    
    MAX_RPM_PHI = (PHI_RANGE_DEG/360.0) / (MAX_PHI_SEC/60.0) # rotation forward to upright
    MAX_RPM_LAMBDA = (LAMBDA_RANGE_DEG/360.0) / (MAX_LAMBDA_SEC/60.0)  # rotation about base

    # Test
    global fake_motor_phi_deg, fake_motor_lambda_deg
    fake_motor_phi_deg = 0
    fake_motor_lambda_deg = 0

    global LOOP_UPDATE_SEC
    LOOP_UPDATE_SEC = 1 # How often to execute loop

    global MAX_ERROR_PHI_DEG, MAX_ERROR_LAMBDA_DEG
    # MAX_ERROR_PHI_DEG = 0.001 # Max error in tracker to drone alignment (degrees)
    # MAX_ERROR_LAMBDA_DEG = 0.001

    MAX_ERROR_PHI_DEG = 0.9 # Max error in tracker to drone alignment (degrees)
    MAX_ERROR_LAMBDA_DEG = 0.9


    # --- Drone ---

    return
