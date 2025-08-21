import numpy as np

a1 = np.array([1010,1021,1234,1436,1119,1999])

filt1=[]
filt2=[]

for x in a1:
	if x%2 == 0:
		filt1.append(True)
		filt2.append(False)
		
	else:
		filt2.append(True)
		filt1.append(False)		
print("\nPrinting Even tokens")		
a2 = a1[filt1]
print(a2)
print("\nPrinting ODD tokens")
a3 = a1[filt2]
print(a3)
