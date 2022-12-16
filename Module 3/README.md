# Overview
Acting in the physical world is inherently uncertain. As discussed during the last week, motor commands issued to a robot do not always lead to the robot state predicted by the kinematic model. Taking the example of locomotion, the robot might end up in a different position because a motor does not function correctly, the wheels slip on the ground, or the robot bumps into an obstacle. The estimation of the robot state, e.g., its pose, can be improved by incorporating sensor measurements, however, also sensors are a subject to noise and errors.

The recursive Bayes filter is a mathematical framework that incorporates noisy actions and sensor measurements to estimate the robot state. This week, you will learn how to derive the general form of the algorithm, in the rest of the course we will use different forms of the Bayes filter to solve the problem of robot localization.

# Learning Objectives

In this module, you will learn the basics of Bayes filtering. In particular, you will learn the necessary mathematical notation, the assumptions of the model, and how the Bayes filter can be derived from first principles of probability theory.

# Readings

Besides the material provided in Canvas, we recommend reading Chapter 2 of the course book.

After this learning unit, you should be able to:

understand the derivation of the Bayes filter
apply the Bayes filter algorithm to solve small problems on paper
discuss the assumptions and limitations of the Bayes filter

# To-Do List

In order to successfully complete Module 3, you should do the following: 

Read: Read and watch the provided sources to learn about the Bayes Formula, how the robot state is estimated from measurements and actions, and about the Bayes Filter. (approximated time: 3 hours)
Demonstrate: Use the Bayes filter algorithm to manually calculate the state of a robot. See the assignment page for more instructions. (approximated time: 4 hours)
Deepen: In a group of up to four people, discuss the assumptions made in the Bayes filter algorithm. (approximated time: 3 hours)