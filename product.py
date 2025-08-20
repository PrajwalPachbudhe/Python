prod = {}

n = int(input("Enter the number of product you want to add: "))

for i in range(n):
	name = input("Enter the product name: ")
	price  = int(input("Enter the price: "))
	prod[name]=price
	
	
print(prod)
