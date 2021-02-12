## Antenna Tracker Project - UTAT UAS 2021

Ian Webster  
UTAT UAS | RnD Division  

### Project Description
The antenna tracker is a multifaceted electrical, software, and mechanical project. The goal of the antenna tracker is to have an autonomous drone-tracking device that uses telemetry data from a drone to compute the desired tracking angles to "follow" the drone's flight path in real-time.  

The tracker will need to use it's own location data with the recieved telemetry data from the drone to compute the target angles to move the tracker.  

A GPS or gyro module could be used to track z-position (altitude), pitch, and yaw of the tracker, and move the motors accordingly until the (z, p, y) vector is within a suitable range of error of the true computed vector. (i.e. 0.1 degrees)

### Utilized Hardware:
* 2x 12V DC Motors rated at 0.82A stall current, so P = 12*0.82*2 = 19.68W
* Driven with L298N DC Motor Driver (25W max power)
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
[ ] Learn about MavSDK
[ ] Simulate a drone OR use pull live GPS coordinates from a drone's pixhawk
[ ] Receive drone position data using mav-sdk with python.
[ ] Communicate the drone position data to the antenna tracker computer
[ ] Use the antenna tracker computer to compute the new position of the tracker to follow the drone's position






