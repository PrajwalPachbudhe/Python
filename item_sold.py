item = (101, 255, 55, 50, 40, 101, 48, 101, 68, 99, 199, 299)
it = list(item)

l=len(it)

def costly():
	a=it[0]
	for i in range(1,l):
		if a < it[i]:
			a=it[i]
			
	print("Costly item price: ", a)
	
def cheap():
	a=it[0]
	for i in range(1,l):
		if a > it[i]:
			a=it[i]
			
	print("Cheap item price:", a)
	
	
def same():
	count =0
	for i in range(l):
		if 101 == it[i] :
			count+=1
					
	print("Number of 101 price item sold: ", count)
	
def total():
	count =0
	for i in it :
			count+=1
					
	print("Total item sold: ", count)
	
	
costly()			
cheap()
same()
total()
	
	

