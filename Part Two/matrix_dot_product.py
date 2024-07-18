import numpy as np

# Define the scalar
scalar = 2

# Define the matrix
matrix = np.array([[6, -9, 1], [4, 24, 8]])

# Compute the scalar dot product
result = scalar * matrix

print(result)

matrix_2 = np.array([[1,0], [0, 1]])

result_2 = np.dot(matrix_2, matrix)

print(result_2)

matrix_3 = np.array([[4, 3], [3, 2]])

matrix_4 = np.array([[-2, 3], [3, -4]])

result_3 = np.dot(matrix_3, matrix_4)

print(result_3)