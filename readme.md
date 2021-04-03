## Antenna Tracker Project - UTAT UAS 2021

Ian Webster  
UTAT UAS | RnD Division  

### Project Description
The antenna tracker is a multifaceted electrical, software, and mechanical project. The goal of the antenna tracker is to have an autonomous drone-tracking device that uses telemetry data from a drone to compute the desired tracking angles to "follow" the drone's flight path in real-time.  

The tracker will need to use it's own location data with the recieved telemetry data from the drone to compute the target angles to move the tracker.  

A GPS or gyro module could be used to track z-position (altitude), pitch, and yaw of the tracker, and move the motors accordingly until the (z, p, y) vector is within a suitable range of error of the true computed vector. (i.e. 0.1 degrees)

### Utilized Hardware:
* 2x 12V DC Motors rated at 0.82A stall current, so P = 12 * 0.82 * 2 = 19.68W
* L298N DC Motor Driver (25W max power)
* A microcomputer or microcontroller
  * Raspberry Pi
  * Arduino
* GPS Module (mounted to the antenna on the tracker to identify tracker's position)

### Implementation Details
* Use velocity and acceleration data to **more precisely** move the tracker according to the drone movement (but for now, just use a feedback system with a specified tolerance to move the tracker's motors until the location of the tracker is aligned with the drone's position)
* Intelligent movement to minimize power drawn from motors (i.e. move 30 deg instead of 120 deg) 

### Telemetry Flowchart
Drone / Pixhawk -> GCS (Ground Control Station) -> Antenna Tracker

### Logic Flowchart
Get GPS Data of Drone -> Get GPS Data of Tracker -> Move the Tracker to follow Drone's Current or Future Predicted Position

### Combined Flowchart  
1. Use MavSDK to pull GPS data from drone (pixhawk) to ground control.
2. Ground control sends this GPS data to Rpi/Arduino (tracker computer).
3. Use tracker computer to compute angle to control the antenna motors.

## Milestones
- [ ] Learn about MavSDK  
- [ ] Simulate a drone OR use pull live GPS coordinates from a drone's pixhawk  
- [ ] Receive drone position data using mav-sdk with python.  
- [ ] Communicate the drone position data to the antenna tracker computer  
- [ ] Use the antenna tracker computer to compute the new position of the tracker to follow the drone's position  


### Tracker Algorithm

* Goal: Should take in tracker GPS and Compass Data, and Antenna GPS Data, and return absolute angles (in xy-plane, and with z-axis) to move the tracker to.

## General Definitions:

* **lon** and **lat** angles defined with respect to *center of earth* as ORIGIN
* alt is defined with respect to surface of earth (sea-level) as reference (0 m)

* **lon** = lambda = angle made with xy-plane (0 deg lon)
* **lat** = phi = angle made with the z-axis (0 deg is equator/xy-plane)

* Supplied by the Drone's GPS: (assume 2 is the drone for now. May write code to abstract this to deal with corner cases (i.e. -180, etc.))
* ```<lat2, lon2, alt2>```

* Supplied by the Antenna Tracker's GPS:
* ```<lat1, lon1, alt1>```

* Supplied by the Antenna Tracker's Gryo:
* ```<tracker_theta_xy_gyro, tracker_phi_z_gyro>```

* **tracker_theta_xy_gyro** = the angle the tracker actually makes in the xy plane (NOT lon), treating the tracker as the ORIGIN
* **tracker_phi_z_gryo** = the angle the tracker actually makes with the z-axis (), treating the tracker as the ORIGIN

### Calculations

#### Option 1: Tracker can move to **absolute** angle (lat/lon), i.e. using servos and compass/gryo, treating itself as the origin, North as reference for xy-plane angle.

* phi and delta_lon are the absolute angles to move the servos TO!

* TODO: Make considerations if lon2 > fff or lon2 < ... -> i.e. use abs val? or +180, etc...

* ```"target_phi" = absolute angle to z-axis``` -> target angle to move the tracker to, if xy-plane is 0 deg, and +z is 90 deg [-phi = -z, +phi = +z . The drone's current value of phi is **tracker_phi_z_gryo**]

* ```"target_lon" = lon2 - tracker_theta_xy_gyro``` -> this is not really a delta. It's an absolute target angle to go to. **lon2** is the drone, and **tracker_theta_xy_gryo** is the angle the tracker is currently pointing in the xy-plane (North as 0 deg). 

* [Note: **lon2** = target angle to move tracker (angle in xy plane), assuming the tracker was pointing directly outwards on lon1. This would be a bad approximation of delta_lon on its own, because we need to take into account the actual direction that tracker is currently pointing, using **tracker_theta_xy_gryo**]

#### Option 2: Tracker moves towards the target angle by moving by an incremental angle **relative** to its current direction 
* until we're within a certain range of error of the true directions.)

* ```delta_phi = target_phi - tracker_phi_z_gyro``` -> This is a delta. It's a relative angle to move the tracker's angle with the z-axis in order to point to the drone.

* ```delta_lon = lon2 - lon1 - tracker_theta_xy_gyro``` -> this is a delta. It's a relative angle to move the tracker to get to the final target angle.

#### Option 3: Tracker moves in the direction of the target absolute angle, and tries to achieve this position within some tolerance
* (closer to a control systems approach - calculate the estimate, then move the tracker's DC motors)
* Ideally have the same tolerance as the antenna itself

* We would use the same formulas as Option 2, but then make inferences on which direction to move the tracker based on the drone's current values of ```<tracker_theta_xy_gyro, tracker_phi_z_gyro>```. 
* For example, if the drone's delta_phi is increasing (target_phi is increasing), we should **reduce** tracker_phi_z_gyro until we notice that tracker ```phi_z_gyro/target_phi <= antenna_phi_error_tolerance```, where the best case would result in delta_phi == 0. TODO: think of how to avoid divide by 0 problem.
* We should do something similar for the longitude.

* ```delta_phi = target_phi - tracker_phi_z_gyro``` -> This is a delta. It's a relative angle to move the tracker's angle with the z-axis in order to point to the drone.

* ```delta_lon = lon2 - lon1 - tracker_theta_xy_gyro``` -> this is a delta. It's a relative angle to move the tracker to get to the final target angle.