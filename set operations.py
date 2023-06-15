E = {0, 1, 2, 3, 4, 5, 6}
N = {2, 4, 6, 8}

union = E.union(N)
intersection = E.intersection(N)
difference = E.difference(N)
symmetric_difference = E.symmetric_difference(N)

print("Union of E and N is", union)
print("Intersection of E and N is", intersection)
print("Difference of E and N is", difference)
print("Symmetric difference of E and N is", symmetric_difference)
