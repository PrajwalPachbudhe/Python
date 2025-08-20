items = {
	"Pencil" : 44,
	"Pen" : 55,
	"Eraser" : 66,
	"Sharpner" : 34,
	"Football" : 12

}

for i in items.items():
	print(i)
	
	
items.pop("Sharpner")
print("Printing items after removing one item\n")
for i in items.items():
	print(i)


items["fevicol"] = 44
print("Printing items after Add one item\n")
for i in items.items():
	print(i)


items.update({"MAP" : 55})

print("Printing items after update item\n")
for i in items.items():
	print(i)

for name, qty in items.items():
	if qty<40:
		print(name, qty)
