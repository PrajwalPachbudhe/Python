import numpy as np
index = []

arr = np.array([10, 60, 50, 40, 20,30])
print(arr)
print(np.sort(arr))
print(np.where(arr == 40))

index = list(np.where(arr == 11 ))
if index[0] >= 0:
	print("IS available\n")
else:
	print("Is not Available\n")
	
	
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[11,12,13]])

print(np.hstack((arr1,arr2)))
print(np.vstack((arr1,arr2)))

print(np.split(arr, 3))

