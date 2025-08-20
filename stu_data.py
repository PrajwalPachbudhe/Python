marks = []
n = int(input("How many student marks: "))

def read():
	for i in range(n):
		mr = int(input("Enter the marks: "))
		marks.append(mr)
		
		
def high():
	a= marks[1]
	for i in range(1, n) :
		if a < marks[i]:
			a= marks[i]
					
	print("highest marks: ", a)
	
		
def low():
	a= marks[1]
	for i in range(1, n) :
		if a > marks[i]:
			a= marks[i]
					
	print("lowest marks: ", a)
	
		
def Average():

	average = sum(marks) / len(marks)

	print("Average marks:", average
		
					
def pass():
	
