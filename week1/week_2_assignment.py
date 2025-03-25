# This is python week 2 Assignment
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert 15 at the second position (index 1)
my_list.insert(1, 15)

#Extend the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

#Remove the last element from the list
my_list.pop()

#Sort the list in ascending order
my_list.sort()

#Find and print the index of the value 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)

# Print the final list for verification
print("Final List:", my_list)

