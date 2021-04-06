# This tracker should:
# Receive lat, lon, altitude information from mission planner (over serial)
# Find the delta in angles phi and lambda (delta_lon)

import math
import visualize as vz
import numpy as np

EARTH_RADIUS_METERS = 1 #6378137 #[m]
# EARTH_RADIUS_METERS = 1
rad_to_deg = 180/(np.pi)
deg_to_rad = np.pi/180


def main():
    
    # 1. Read in 3 doubles, lat, lon, alt - separated by commas. How to do this? Read comma-separated data into separate doubles?

    # Make sure this test case actually works

    # # CENTER EARTH ORIGIN
    # lat1 = 10 
    # lon1 = 3
    # # SURFACE EARTH ORIGIN
    # alt1 = 3

    # # CENTER EARTH ORIGIN
    # lat2 = 10
    # lon2 = 6
    # # SURFACE EARTH ORIGIN
    # alt2 = 6

    # CENTER EARTH ORIGIN
    lat1 = 150 * deg_to_rad
    lon1 = 0 * deg_to_rad
    # SURFACE EARTH ORIGIN
    alt1 = 10

    # CENTER EARTH ORIGIN
    lat2 = 450 * deg_to_rad 

    # I think conversions are off by a factor of 100 somewhere! i.e. 300 = 30 deg
    # at least, this fixes the calculation for phi
    # target_lon still messed up
    lon2 = 600 * deg_to_rad #something's wrong with lon scaling when calculating target_lon or lambda
    # SURFACE EARTH ORIGIN
    alt2 = 20

    # Current tracker readings from gyro, TRACKER ORIGIN
    tracker_theta_xy_gyro = 0 * deg_to_rad # theta is equiv to lambda?
    tracker_phi_z_gyro = 0 * deg_to_rad

    # lat_avg
    # x1, x2, y1, y2, d = 0
    # delta_x, delta_y, delta_alt
    # phi, delta_lon

    #1.1 Read real data from the serial port (sent from python for now)
    # lat1 = Serial.read()  

    # 2. Compute Points
    lat_avg = (lat1 + lat2) / 2 #for distance between 2 points
    print(f"lat_avg: {lat_avg}")

    x1 = lon1*math.cos(lat_avg)
    y1 = lat1 #not lon?

    x2 = lon2*math.cos(lat_avg)
    y2 = lat2 #not lon?

    delta_x = x2 - x1
    delta_y = y2 - y1


    # if (delta_x < 0) delta_x *= -1
    # if (delta_y < 0) delta_y *= -1

    delta_alt = alt2 - alt1

    # 3. Get ground distance between 2 points
    d = EARTH_RADIUS_METERS*math.sqrt(delta_y*delta_y + delta_x*delta_x) # R = radius of earth
    print(f"x1: {x1}, x2: {x2}, y1: {y1}, y2: {y2}, delta_x: {delta_x}, delta_y: {delta_y}, d: {d}")

    # 4. Compute angles for servos

    # Option 1
    target_phi  = (math.atan(delta_alt / d))*rad_to_deg # angle to z-axis
    target_lon = (lon2 - tracker_theta_xy_gyro)*rad_to_deg #Do we want in degrees or radians?

    # Option 2
    delta_phi = (math.atan(delta_alt / d) - tracker_phi_z_gyro)*rad_to_deg
    delta_lon = (lon2 - lon1 - tracker_theta_xy_gyro)*rad_to_deg # delta_lon = target_lon - lon1

    # 5. Move the servos to the correct position

    print("Option 1: Absolute angles to move servos to.")
    print(f"target_phi: {target_phi}")
    print(f"target_lon: {target_lon}\n")
    
    print("Option 2: Relative angles to move servos to, based on curr positions.")
    print(f"phi (z-axis angle): {delta_phi}")
    print(f"lambda (angle in xy-plane): {delta_lon}")
    print("---Current servo positions---")
    print(f"current phi: {tracker_phi_z_gyro}")
    print(f"current lambda: {tracker_theta_xy_gyro}")
    # Option 3: Do some math. to check for accuracy/within error tolerance of antenna's polar range


    # Visualize
    # vz.spherical(target_phi, target_lon)

    vz.vectors([[0, 0, 0, x1, y1, alt1], [0, 0, 0, x1, y1, 0], [x1, y1, 0, 0, 0, alt1], [0, 0, 0, x2, y2, alt2], [0, 0, 0, x2, y2, 0], [x2, y2, 0, 0, 0, alt2]]) 

    # it seems like phi and lon are switched?

if __name__ == "__main__":
    main()
