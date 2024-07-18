## This is course material for Introduction to Python Scientific Programming
## Example code: plot_3D.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from mpl_toolkits import mplot3d #we have to import 3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d") #this will project the data into 3D

z_line = np.linspace(0, 15, 1000) #the z line is the radius and the radians as the z is going from zero to higher and the readius is getting bigger
x_line = np.cos(z_line)*z_line
y_line = np.sin(z_line)*z_line
ax.plot3D(x_line, y_line, z_line, 'gray')

z_points = 15 * np.random.random(100)
x_points = np.cos(z_points)*z_points + 1 * np.random.randn(100) #if you dont have noise the dots will be exactly on the line
y_points = np.sin(z_points)*z_points + 1 * np.random.randn(100) #the amount of the noise is random
ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv') #this is used to plot the dots
#color is also randomly assigned by z
plt.show()