# Overview
In the previous module, you learned how to localize a robot using a particle filter. There, the algorithm was provided with a map that was constructed from the ground truth data obtained from the simulator. In practice, a map can be recovered from sensor data if the robot trajectory is known, a.k.a. mapping with known poses. The problem of Simultaneous Localisation and Mapping (SLAM) is more complex. In SLAM, the robot needs to estimate its pose while mapping the environment at the same time. That is often described as a chicken-or-egg problem since localization requires a map and robot poses are needed for map creation. 

# Learning Objectives

In this module, you will first obtain an introduction to the SLAM problem. Next, you will learn about the Kalman Filter, a widely used state estimation method for Gaussian processes. Finally, you will learn the FastSLAM algorithm, which is a SLAM solution based on the particle filter and Kalman Filter approaches.

# Readings

Besides the material provided in Canvas, we recommend reading Chapter 10.1 in the course book for an overview of SLAM, Chapter 3.2 for the Kalman Filter, and the original FastSLAM paper Links to an external site..

After this learning unit, you should be able to:

* Understand the SLAM problem
* Understand the Kalman Filter and the FastSLAM algorithms
* Implement FastSLAM to localize a robot and build a map in a simulated environment

# To-Do List
In order to successfully complete Module 6, you should do the following: 

Read: Read the material on SLAM, the Kalman Filter, and FastSLAM.
Assignment: The assignment on implementing the FastSLAM algorithm will be published on Tuesday, Jan 17. and is due by Jan 29., 23:59 CET. The assignment can be completed either individually or in a group. If you decide to submit as a group, please join a group under People->Module 6: SLAM.