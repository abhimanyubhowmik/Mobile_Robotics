# -*- coding: utf-8 -*-

import numpy as np
import math
import matplotlib.pyplot as plt
import random

# Sample from a normal distribution using 12 uniform samples.
def sample_normal_distribution(mu, sigma):
    #return sample from normal distribution with mean = a and standard deviation b
    random_sum = 0
    for i in range(12):
        random_num = random.uniform(-sigma + mu,sigma + mu)
        random_sum += random_num
    random_num_final = 1/12 * random_sum
    return random_num_final


""" Sample odometry motion model.

Arguments:
x -- pose of the robot before moving [x, y, theta]
u -- odometry reading obtained from the robot [rot1, rot2, trans]
a -- noise parameters of the motion model [a1, a2, a3, a4]

"""
def sample_motion_model(x, u, a):

    x, y, theta = x[0], x[1], x[2]
    rot1, rot2, trans = u[0], u[1], u[2]
    a1, a2, a3, a4 = a[0], a[1], a[2], a[3]

    rot1_prime = rot1 + sample_normal_distribution(0, a1*abs(rot1) + a2*trans)
    rot2_prime = rot2 + sample_normal_distribution(0, a1*abs(rot2) + a2*trans)
    trans_prime = trans + sample_normal_distribution(0, a3*trans + a4*(abs(rot1)+ abs(rot2)))

    x_prime = x + trans_prime * np.cos(theta + rot1_prime)
    y_prime = y + trans_prime * np.sin(theta + rot1_prime)
    theta_prime = theta + rot1_prime + rot2_prime
    return np.array([x_prime, y_prime, theta_prime])


""" Evaluate motion model """

def main():
  # start pose
  x = [0.0, 0.0, 0.0]
  # odometry
  u = [[0.0, 0.0, 1.0],
       [0.0, 0.0, 1.0],
       [np.pi/2, 0.0, 1.0],
       [0.0, 0.0, 1.0],
       [0.0, 0.0, 1.0],
       [np.pi/2, 0.0, 1.0],
       [0.0, 0.0, 1.0],
       [0.0, 0.0, 1.0],
       [0.0, 0.0, 1.0],
       [0.0, 0.0, 1.0]]
  # noise parameters
  a = [0.02, 0.02, 0.01, 0.01]

  num_samples = 1000
  x_prime = np.zeros([num_samples, 3])
  # 1000 samples with initial pose
  for i in range(0, num_samples):
      x_prime[i,:] = x

  plt.axes().set_aspect('equal')
  plt.xlim([-5, 5])
  plt.ylim([-3, 7])
  plt.plot(x[0], x[1], "bo")
  
  # incrementally apply motion model
  for i in range(0,10):
      for j in range(0, num_samples):
        x_prime[j,:] = sample_motion_model(x_prime[j,:],u[i],a)        
      plt.plot(x_prime[:,0], x_prime[:,1], "r,")

  
  plt.xlabel("x-position [m]")
  plt.ylabel("y-position [m]")

  plt.show()

if __name__ == "__main__":
  main()


