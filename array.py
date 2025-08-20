import numpy
arr = numpy.array([1,3,2,4,5,6])
print("\nPrinting array")
print(arr)

print("\n4th element of array")
print(arr[4])

print("\nprinting from 2 to 4")
print(arr[2:5])


print("\npriting from 2")
print(arr[2:])

print("\nPrinting last three elements")
print(arr[-3:])

print("\nPrinting in reverse")
print(arr[::-1])


d = arr.ndim

print("\nPrinting dimension of array")
print(d)


arr1 = numpy.array([[1,2,4],[3,6,5]])

print("\nPrinting 2 dimensional array")
print(arr1)

d = arr1.ndim
print("\nPrinting dimension of array")
print(d)

print("\nPrinting shape of array1")
print(arr.shape)


print("\nPrinting shape of array2")
print(arr1.shape)


print("\nPrinting size of array1")
print(arr.size)



print("\nPrinting Size of array2")
print(arr1.size)


print("\nPrinting dType of array")
print(arr.dtype)


print("\nPrinting  1D array")
for i in arr:
	print(i)
	
	
print("\nPrinting  2D array")
for i in arr1:
	for y in i:
		print(y)
print("\nPrinting  2D array Using nditer")
for x in numpy.nditer(arr1):
	print(x)

sorted_array = numpy.sort(arr)

print(sorted_array)







