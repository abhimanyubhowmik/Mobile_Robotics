# Overview
The last module introduced the recursive Bayes filter. To implement it in practice, one requires the transition model  and the measurement or sensor model . In the previous assignment, the necessary values of these functions were provided. In real-world applications, however, the transition and sensor model have a more complex form and need to fit the robot hardware at hand. 

# Learning Objectives

In this module, you will learn a transition model that approximates the uncertainty in the motion of a wheeled robot, the odometry-based motion model. You will further learn the beam-based sensor model for range sensors.

# Readings

Besides the material provided in Canvas, we recommend reading the following chapters in the course book: Chapter 5.4 for the odometry-based model and Chapter 6.3  for the sensor model.

After this learning unit, you should be able to:

model the motion uncertainty of a wheeled robot
implement an algorithm that samples from the odometry-based motion model
understand and apply a sensor model to estimate the likelihood of a range measurement

# To-Do List
In order to successfully complete Module 3, you should do the following: 

Read: Read the provided sources to learn about the odometry-based motion model and the beam-based sensor model.  (approximated time: 4 hours)
Demonstrate: Implement the sampling algorithm for the motion model and use the sensor model to compute the likelihood of a range measurement. See the assignment page for more instructions. (approximated time: 6 hours)