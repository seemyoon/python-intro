# Task: Working with Tuples
#
# Create a tuple named myTuple with at least five elements of mixed types (e.g., int, float, string).
myTuple = (45.2, "asd", True, "banana", 89)
# Access and print the second and last elements of the tuple.
print(myTuple[1])
print(myTuple[-1])
# Use slicing to create a new tuple containing the middle three elements of myTuple, and print it.
myNewTuple = myTuple[1:4]
print(myNewTuple)
# Find the index of a specific value (of your choice) in the tuple, and print it.
print(myNewTuple.index("asd"))
