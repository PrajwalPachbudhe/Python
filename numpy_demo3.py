import numpy as np

a1 = np.array([112,115,36,96, 87,49,51])

filt = []

for x in a1:
	if x%3 == 0:
		filt.append(True)
		
	else:
		filt.append(False)
		
a2 = a1[filt]
print("Printing Filtered array")
print(a2)
