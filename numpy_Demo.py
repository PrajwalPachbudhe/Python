import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print("\n Printing 1-D Array: \n")
print(arr)


arr1 = arr.reshape(4,3)
print("\nprinting multi Dimensional Array(4,3): ")
print(arr1)

arr2 = arr.reshape(2, 3, 2)
print("\n Printing Multi-Dimensional Array(2,3,2): ")

print(arr2)

