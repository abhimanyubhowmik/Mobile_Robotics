"""Differential_drive controller - Module 2 assignment, Part 1"""
""" © Abhimanyu Bhowmik """

from controller import Robot
from math import pi

if __name__ == "__main__":

    # Max speed and speed for driving the robot
    MAX_SPEED = 12.3
    SPEED = 0.25 * MAX_SPEED

    # The Robot instance.
    robot = Robot()

    # get the time step of the current world.
    timestep = 64

    # get wheel motor controllers
    left_motor = robot.getDevice('left wheel')
    right_motor = robot.getDevice('right wheel')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))

    # set wheel velocities (in rad)
    # a velocity of 2*pi means that the wheel will make one turn per second
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    # Radius of Curvature
    R = 2
    # Distance between the wheels
    l = 0.325
    # Total travel distance
    distance = pi * R
    # Wheel radius
    wheel_radius = 0.195/2
    # Wheel speeds
    left_speed = SPEED*(R - l/2)
    right_speed = SPEED*(R + l/2)
    # Wheel velocity 
    left_velocity = left_speed * wheel_radius
    right_velocity = right_speed * wheel_radius
    # Linear velocity of Robot
    linear_velocity = (left_velocity + right_velocity)/2
    # Total duration
    duration_time = distance/linear_velocity
    # Get starting time
    start_time = robot.getTime()
    # Count No. of steps
    steps = 1
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Get current time
        current_time = robot.getTime()
        # Sropping conditions
        if current_time > (start_time + duration_time):
            
            # Move on to next step
            if steps == 1:  
                # New Speeds
                left_speed = - 0.5 * MAX_SPEED
                right_speed = 0.5 * MAX_SPEED
                # Reset start time
                start_time = robot.getTime()
          
                # Velocity of wheel i.e. v = w*r
                wheel_velocity = 0.5 * MAX_SPEED * wheel_radius
                # Distance to travel i.e. 2*pi*R/2 
                distance = pi * l/2
                # Required time
                duration_time = distance/wheel_velocity
                
                steps += 1
            
            # Last step 
            else:
                # Stop the robot
                left_speed = 0
                right_speed = 0
        
                
        # Set velocities
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)


# Enter here exit cleanup code.
