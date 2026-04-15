print("251C025", "24-03-2026")
import numpy as np
arr1D = np.array([1, 2, 3, 4, 5])
print("1D Array", arr1D)
print(arr1D[2])
reshaped = arr1D.reshape(5, 1)  # reshaping
print("Reshaped=", reshaped)  # SLICING
print(arr1D[1:4])
arr2D = np.array(
    [[2, 3, 4], [8, 9, 10]]
)
print("2D array", arr2D)
print(arr2D[1][1])
print(arr2D[0:1])  # SLICING
arr3D = np.array([
    [[21, 2, 7], [8, 1, 10]],
    [[4, 5, 7], [37, 5, 8]]
])
print("3D array", arr3D)
print(arr3D[1][1])
print(arr2D[0:2])  # SLICING
