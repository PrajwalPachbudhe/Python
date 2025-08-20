A={199.99, 150, 160, 170, 299.99, 298, 293}
B={199.99, 155, 165, 175, 299.99, 298, 294}
C={190, 155, 165, 175, 290, 291, 292}

print(A.union(B.union(C)))

print(A.intersection(B.intersection(C)))

print(A.symmetric_difference(B.symmetric_difference(C)))
print(A.intersection(B))
print(B.intersection(C))



