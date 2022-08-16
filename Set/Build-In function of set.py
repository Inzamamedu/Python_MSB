"""
# Union
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)  # Bitwise Operator
print(A.union(B))
print(B.union(A))
"""

"""
# intersection
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A & B)
print(A.intersection(B))
print(B.intersection(A))
"""

"""
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A ^ B)
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

"""

"""
# difference

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A - B)
print(B - A)

print(A.difference(B))
print(B.difference(A))
"""

"""
# Disjoint
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {2, 9, 10, 11, 12, 13}

print(A.isdisjoint(B))
print(A.isdisjoint(C))

"""
"""
# subset
# A is in B
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print(A.issubset(B))
print(B.issubset(A))
"""

# superset
# A is in B
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print(B.issuperset(A))
print(A.issuperset(B))