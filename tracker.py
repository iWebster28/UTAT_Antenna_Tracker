# This tracker should:
# Receive lat, lon, altitude information from mission planner (over serial)
# Find the delta in angles phi and lambda (delta_lon)

import math

EARTH_RADIUS_METERS = 6378137

def main():
    # 1. Read in 3 doubles, lat, lon, alt - separated by commas. How to do this? Read comma-separated data into separate doubles?

    # Make sure this test case actually works

    # CENTER EARTH ORIGIN
    lat1 = 10 
    lon1 = 3
    # SURFACE EARTH ORIGIN
    alt1 = 3

    # CENTER EARTH ORIGIN
    lat2 = 10
    lon2 = 6
    # SURFACE EARTH ORIGIN
    alt2 = 6

    # Current tracker readings from gyro, TRACKER ORIGIN
    tracker_theta_xy_gyro = 0.1 # theta is equiv to lambda?
    tracker_phi_z_gyro = 0.2

    # lat_avg
    # x1, x2, y1, y2, d = 0
    # delta_x, delta_y, delta_alt
    # phi, delta_lon

    #1.1 Read real data from the serial port (sent from python for now)
    # lat1 = Serial.read()  

    # 2. Compute Points
    lat_avg = (lat1 + lat2) / 2 #for distance between 2 points

    x1 = lon1*math.cos(lat_avg)
    y1 = lat1

    x2 = lon2*math.cos(lat_avg)
    y2 = lat2

    delta_x = x2 - x1
    delta_y = y2 - y1

    delta_alt = alt2 - alt1

    # 3. Get ground distance between 2 points
    d = EARTH_RADIUS_METERS*math.sqrt(delta_y*delta_y + delta_x*delta_x) # R = radius of earth

    # 4. Compute angles for servos

    # Option 1
    target_phi  = math.atan(delta_alt / d) # angle to z-axis
    target_lon = lon2 - tracker_theta_xy_gyro #Do we want in degrees or radians?

    # Option 2
    delta_phi = target_phi - tracker_phi_z_gyro
    delta_lon = lon2 - lon1 - tracker_theta_xy_gyro # delta_lon = target_lon - lon1

    # 5. Move the servos to the correct position

    print("Option 1: Absolute angles to move servos to.")
    print(f"target_phi: {target_phi}")
    print(f"target_lon: {target_lon}\n")
    
    print("Option 2: Relative angles to move servos to, based on curr positions.")
    print(f"current phi: {tracker_phi_z_gyro}")
    print(f"current lambda: {tracker_theta_xy_gyro}")
    print("---Current servo positions---")
    print(f"phi (z-axis angle): {delta_phi}")
    print(f"lambda (angle in xy-plane): {delta_lon}")

    # Option 3: Do some math. to check for accuracy/within error tolerance of antenna's polar range


if __name__ == "__main__":
    main()
