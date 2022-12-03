# Overview

The most fundamental capability of a mobile robot is locomotion, meaning the ability to move from one place to another. Numerous locomotion approaches are used in robotics, for instance, wheels, tracks, legs, rotors, etc., each having its own benefits and drawbacks. Here we will focus on wheeled robots, and specifically on such using a differential drive, since they are widely used in practice and easy to deploy. 

Sensors are another essential component of a mobile robot that allows it to perceive its surrounding and perform according actions. Range sensors tell the robot how far the closest surface is in a given direction,  information that can be used for obstacle avoidance, mapping, and localization. 

## Learning Objectives

In this module, you will study the basics of wheeled locomotion on the example of a differential drive robot.  You will learn the forward kinematics for the differential drive and how to set the motor commands to move the robot along certain trajectories. Further, you will learn how to deploy a LiDAR range sensor to detect nearby surfaces and steer the robot along a wall.  

## Readings

Please read the material on the differential drive and range sensing using a LiDAR. 

After this learning unit, you should be able to:

understand the theoretical background of locomotion with a differential drive
program the controller of a differential drive robot to move to a specific goal position
use the measurements of a range sensor to find the surface closest to the robot
implement wall-following behavior in a robot

## ToDo List

In order to successfully complete Module 2, you should do the following: 

Read: Read and watch the provided sources to learn about differential drive and range sensing. (approximated time: 2 hours)
Demonstrate: In the Webots simulator, first devise a differential drive controller and then use it to implement wall following. See the assignment page for more instructions. (approximated time: 8 hours)
Deepen: Answer the questions in the quiz on error sources in forward kinematics and sensing (will be available from Thursday, Nov 24). (approximated time: 30 minutes, not graded)