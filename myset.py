my_set = {1,2,2,3,4,4,4}
print("set :", my_set)



my_set.add(5)
print("updated set:", my_set)
print()
print()

set1 = {1,2,3,4,5}
set2 = {2,4,4,6}

print("\nset1",set1)
print("set2",set2)
print()

print("difference")
print(set1.difference(set2))


print()
print("symmetric difference")
print(set1.symmetric_difference(set2))

print("\nintersection of two saud sets")
setz = set1.intersection(set2)
print(setz)

setc = set1.union(set2)
print("\nunoin of above sets :")
print(setc)