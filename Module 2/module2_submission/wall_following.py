"""wall_following controller."""

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
    
    
    
    sonar_sensors = []
    for i in range(16):
        sensor_name = 'so' + str(i)
        sonar_sensors.append(robot.getDevice(sensor_name))
        sonar_sensors[i].enable(timestep)
        
        
    def turn_right_in_place():
        print('Turn Right in place')
            
        return SPEED, - SPEED
        
    def turn_right():
        
        print('Trun Right')
        
        return SPEED, SPEED/8
        
    def turn_left():
        
        print('Turn Left')
                
        return SPEED/8, SPEED
        
    def move_forward():
    
        print('Move Forward')
                
        return SPEED, SPEED
                
    def move_backward():
    
        print('Move Backward')
                
        return -SPEED, -SPEED
        
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
                        
                        lidar.disable()
                        lidar.disablePointCloud()
                        
                        left_speed = SPEED
                        right_speed = SPEED
                        
                        for i in range(16):
                            print('sensor {i}, distance {val}'.format(i = i, val = sonar_sensors[i].getValue()))
                            
                        # Process the sensor data
                        front_wall = sonar_sensors[3].getValue() > 80 or sonar_sensors[4].getValue() > 80
                        left_wall = sonar_sensors[0].getValue() > 80 and sonar_sensors[15].getValue()> 80
                        left_corner = sonar_sensors[2].getValue() > 80 or sonar_sensors[1].getValue() > 80
                        
                        sensor_0 = sonar_sensors[0].getValue()
                        sensor_1 = sonar_sensors[1].getValue()
                        sensor_2 = sonar_sensors[2].getValue()
                        sensor_3 = sonar_sensors[3].getValue()
                        sensor_4 = sonar_sensors[4].getValue()
                        sensor_5 = sonar_sensors[5].getValue()
                        sensor_9 = sonar_sensors[9].getValue()
                        sensor_10 = sonar_sensors[10].getValue()
                        sensor_11 = sonar_sensors[11].getValue()
                        sensor_12 = sonar_sensors[12].getValue()
                        sensor_14 = sonar_sensors[14].getValue()
                        sensor_15 = sonar_sensors[15].getValue()
                        
                        # Wall following logic
                        if front_wall:
                        
                            if sensor_3 < 970 and sensor_4 < 970:
                            
                                if sensor_1 < 970 or sensor_2 < 970:
                            
                                    left_speed, right_speed = move_forward()
                                    
                                else:
                                    
                                    left_speed, right_speed = move_backward()
                                
                            elif sensor_1 > 1010 and sensor_2 > 1010:
                            
                                left_speed, right_speed = move_backward()
                                
                            
                                
                            else:
                                
                                left_speed, right_speed = turn_right_in_place()
                            
                        else:
                        
                            if left_corner:
                                print('Too close to wall, Trun Right')
                                
                                left_speed, right_speed = turn_right()
                            
                            elif left_wall:
                            
                                if sensor_0 > 1010 or  sensor_15 > 1010 :
                                
                                    left_speed, right_speed = turn_right()
                    
                                elif sensor_14 < 970 or sensor_15 < 970 :
                                
                                    left_speed, right_speed = turn_left()
                                    
                                else:
                                    
                                    left_speed, right_speed = move_forward()   
                                 
                            elif front_wall == False and left_wall == False:
                                
                                if sensor_4 <970 or sensor_5 <970:
                                    left_speed, right_speed = turn_left()
                                
                            elif sensor_11 > 800 or sensor_12 > 800:
                                left_speed, right_speed = turn_left()
                    
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

from controller import Robot
from math import pi

MAX_SPEED = 12.3
SPEED = 0.1 * MAX_SPEED

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 64
l = 0.325
wheel_radius = 0.195/2

# get wheel motor controllers
left_motor = robot.getDevice('left wheel')
right_motor = robot.getDevice('right wheel')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# set wheel velocities (in rad)
# a velocity of 2*pi means that the wheel will make one turn per second

    

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)


# Enter here exit cleanup code.
