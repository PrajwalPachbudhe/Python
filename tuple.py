
my_tuple = (1, 2, 3, "hello", 5.0)  
empty_tuple = ()
single_item_tuple = ("apple",)  
nested_tuple = ((1, 2), ("a", "b"))

print("1. Creating Tuples:")
print("my_tuple:", my_tuple)
print("empty_tuple:", empty_tuple)
print("single_item_tuple:", single_item_tuple)
print("nested_tuple:", nested_tuple)


print("\n2. Accessing Elements:")
print("Element at index 0 in my_tuple:", my_tuple[0])
print("Element at index -1 (last) in my_tuple:", my_tuple[-1])
print("Slice from index 1 to 3 (exclusive) in my_tuple:", my_tuple[1:4])
print("Slice from beginning to index 2 (exclusive) in my_tuple:", my_tuple[:3])
print("Slice from index 2 to end in my_tuple:", my_tuple[2:])
print("Reverse the tuple using slicing:", my_tuple[::-1])


print("\n3. Tuple Operations:")

tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)


repeated_tuple = ("x",) * 3
print("Repeated tuple:", repeated_tuple)


print("Is 'hello' in my_tuple?", 'hello' in my_tuple)
print("Is 10 in my_tuple?", 10 in my_tuple)


print("Length of my_tuple:", len(my_tuple))


print("Count of 2 in my_tuple:", my_tuple.count(2))

print("Index of 'hello' in my_tuple:", my_tuple.index('hello'))

print("\n4. Immutability Example:")
try:
    my_tuple[0] = 10  
except TypeError as e:
    print("Error:", e, "(Tuples are immutable)")


print("\n5. Iterating through a tuple:")
for item in my_tuple:
    print(item)
