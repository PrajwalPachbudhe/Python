st = []
for i in range(10):
	nm = input("enter the name: ")
	cou = input("Enter the 1 course: ")
	marks = int(input("Enter the marks: "))
	usn = int(input("Enter the usn: "))
	mrk =(nm, usn, cou, marks)
	st.append(tuple(mrk))
	
for i in range(10):	
	print("\n", st[i])
	
