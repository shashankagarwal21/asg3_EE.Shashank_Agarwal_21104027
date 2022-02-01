# make the 3 sets and a new set
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
new_set={}


# Create a new set of all elements that are in Set1 and Set2 but not both
new_set = (Set1 | Set2) - (Set1 & Set2)
print("elements that are in Set1 and Set2 but not both are " + str(new_set))


# Create a new set of all elements that are in only one of the three sets Set1, Set2 and Set3
new_set = Set1 - (Set2 | Set3)
print("all elements that are only in Set1 " + str(new_set))

new_set = Set2 - (Set1 | Set3)
print("all elements that are only in Set2 " + str(new_set))

new_set = Set3 - (Set1 | Set2)
print("all elements that are only in Set3 " + str(new_set))


# Create a new set of elements that are exactly two of the sets Set1, Set2 and Set3
new_set = Set1 & Set2
print("set of elements that are exactly two of the sets Set1, Set2 " + str(new_set))

new_set = Set2 & Set3
print("set of elements that are exactly two of the sets Set2, Set3 " + str(new_set))

new_set = Set1 & Set3
print("set of elements that are exactly two of the sets Set1, Set3 " + str(new_set))

# Create a new set of all integers in the range 1 to 10 that are not in Set1
new_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} -Set1
print("set of all integers in the range 1 to 10 that are not in Set1 " + str(new_set))


# Create a new set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3
new_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} - (Set1 | Set2 | Set3)
print("set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3 " + str(new_set))