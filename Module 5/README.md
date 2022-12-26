# Overview
The recursive Bayes filter can be evaluated analytically under certain circumstances. For example, if the state space is discrete with a relatively low number of states or the motion model, the sensor model, and the initial belief all follow a Gaussian distribution. However, in the case of a continuous state space and a belief that follows a general probability distribution, we have to rely on some approximation of the belief. Consider the scenario of localizing a robot using identical landmarks: In case the robot observes only a single landmark, the resulting belief of the pose would be a multi-modal distribution, with one peak near each landmark. It is not trivial to represent such a distribution by a parametric function.

Non-parametric Bayes filters can approximate arbitrary belief distributions. In this module, you will learn two non-parametric filters: the discrete Bayes filter and the particle filter, whereby the focus will be on the particle filter.

# Organization and Timeline

This learning module is nominally planned for two weeks, however, it also encloses the winter holiday break of three weeks. Thus, officially the module begins on December 12 and ends on January 15. In the first week, you are provided with the reading material on the discrete Bayes filter and the particle filter. You also have a small individual assignment due December 18. By the end of the first week, we will publish a larger group assignment in which you will have to implement a particle filter. That group assignment will be due January 15, so you can plan within your group when to work on it.  

# Learning Objectives

In this module, you will learn two implementations of the Bayes filter, namely the discrete Bayes filter and the particle filter. Further, you will learn how to implement a particle filter and use it for robot localization.

# Readings

Besides the material provided in Canvas, we recommend reading Chapter 4 in the course book.

After this learning unit, you should be able to:

* understand the discrete Bayes filter and the particle filter
* implement a particle filter in Python
* apply the particle filter robot localization and solve the captured robot problem
* understand how different algorithm parameters influence the performance of the particle filter

# To-Do List
In order to successfully complete Module 5, you should do the following: 

Read: Read the material on the discrete Bayes filter, on the particle filter algorithm, and on localization with the particle filter.  
Individual Assignment: Please complete the individual assignment by Dec 18., 23:59 CET.
Group Assignment: Implement a particle filter and use it for robot localization by Jan 15., 23:59 CET. You can find the detailed instructions on the assignment page. By Dec 18., please join a group under People->Module 5: Particle Filter Implementation. The group membership is copied from Module 3, however, you can switch to another group until Dec 18.
