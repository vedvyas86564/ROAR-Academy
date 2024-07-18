import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Define the vector
v = np.array([2., 2., 4.])

# Define the unit vectors for the 3D coordinate axes
e0 = np.array([1., 0., 0.])  # x-axis
e1 = np.array([0., 1., 0.])  # y-axis
e2 = np.array([0., 0., 1.])  # z-axis

# Project v onto each of the coordinate axes
projection_e0 = np.dot(v, e0)
projection_e1 = np.dot(v, e1)
projection_e2 = np.dot(v, e2)

# ax = plt.axes(projection="3d") i dont know how to make the 3d plotting work

# ax.plot(projection_e0, projection_e1, projection_e2, "gray")
# plt.show()
print("Projection onto e0:", projection_e0)
print("Projection onto e1:", projection_e1)
print("Projection onto e2:", projection_e2)
