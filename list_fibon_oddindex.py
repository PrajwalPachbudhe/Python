n =  int(input("Enter the number: "))
fibo1 = [0, 1]
a=0
b=1
fibo2=[]
for i in range(n):
	sum = a+b
	fibo1.append(sum)
	a=b
	b=sum
	
	
for i in range(n):
	if i%2 == 1:
		c=fibo1[i]
		fibo2.append(c)
		
print(fibo2)
		
		
	
