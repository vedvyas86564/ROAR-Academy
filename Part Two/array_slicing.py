import numpy as np

# Create an array with numbers from 0 to 24 (since a 5x5 matrix has 25 elements)
arr = np.arange(0, 36).reshape(6, 6)

# print(arr)

for row in range(len(arr)):
    for col in range(len(arr[row])):
        arr[row][col] = arr[row][col] + 4*row

print(arr)

column_to_print = arr[:, 1]
print(column_to_print) #should print 1-51 in increments of 10

element_12 = arr[1][2]
element_13 = arr[1][3]

arr2 = (element_12, element_13) #should print 12 and 13
print(arr2)

indices = [(0, 2), (2, 2), (4,2), [4, 0], [4, 4]] #defines the indices for the elements to include in the subarray
subarray = arr[[i[0] for i in indices], [i[1] for i in indices]]
print(subarray)

indices2 = [(2, 4), (2, 5), (3,4), [3, 5]] #defines the indices for the elements to include in the subarray
subarray2 = arr[[i[0] for i in indices2], [i[1] for i in indices2]]
print(subarray2)

