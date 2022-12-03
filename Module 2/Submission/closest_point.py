"""proxy_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from math import pi

if __name__ == "__main__":

    MAX_SPEED = 12.3
    SPEED = 0.1 * MAX_SPEED
    
    # create the Robot instance.
    robot = Robot()
    
    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    l = 0.325
    wheel_radius = 0.195/2
    
    # get wheel motor controllers
    left_motor = robot.getDevice('left wheel')
    right_motor = robot.getDevice('right wheel')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    
    # set wheel velocities (in rad)
    # a velocity of 2*pi means that the wheel will make one turn per second
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    # get and enable lidar
    lidar = robot.getDevice('Sick LMS 291')
    lidar.enable(60)
    lidar.enablePointCloud()
    
    min_scan_list = []
    # Velocity of wheel i.e. v = w*r
    wheel_velocity = SPEED * wheel_radius
    
    # Distance to travel i.e. 2*theta*R/2 
    theta = pi + 0.10472
    distance = theta * l/2
    # Required time
    duration_time = distance/wheel_velocity
    
    left_speed = - SPEED
    right_speed = SPEED
    start_time = robot.getTime()
    count = 0
    # From LIDAR frame-of-reference
    haulting_distnce = 0.5 - 0.08
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # get current lidar measurements
        scan = lidar.getRangeImage()
        # Get current time
        current_time = robot.getTime()
        # The very first reading of the lidar is 0, removing it..
        if count != 0:
            min_scan = min(scan)
            min_index = scan.index(min_scan)
            min_scan_list.append(min_scan)
        count += 1
        
        
        if current_time > (start_time + duration_time):
        
            # The closest point in the surrounding
            min_distance = min(min_scan_list)
            
            # if closest point in FOV 
            if round( min_distance,1 ) ==  round( min_scan, 1 ):
                
                # if closest point is in left-side of robot
                if (90 - min_index) > 0:
                    left_speed = - 0.5 * SPEED
                    right_speed = 0.5 * SPEED
                
                # closest point is at the center of FOV
                elif (90 - min_index) == 0:
                
                    # If robot reached the haulting distance
                    if min_scan <= haulting_distnce:
                        left_speed = 0
                        right_speed = 0
                    
                    # Otherwise move forward 
                    else:
                        left_speed = 0.3 * MAX_SPEED
                        right_speed = 0.3* MAX_SPEED
                        
                # if closest point is in right-side of robot
                else:
                    left_speed = 0.5 * SPEED
                    right_speed = - 0.5 * SPEED
            
            # Otherwise rotate to find it        
            else:
                left_speed = - SPEED
                right_speed = SPEED
                
            
                
        
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)


# Enter here exit cleanup code.