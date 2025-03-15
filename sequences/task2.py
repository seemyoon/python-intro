# 1 part
# Create a list with 5 elements of different types
listInstance = [123, "Sasha", 45.2, True, {"age": 24, "town": "Kharkiv"}]
# Delete the third element
del listInstance[2]
# Print the length of the list to the terminal
print(len(listInstance))
# Change the order of items in the list
listInstance.reverse()
# Create another list with two elements
listInstance2 = ["coding", 10010010]
# Expand the first list with elements of the second list
# fullList = listInstance + listInstance2
# print(fullList)
# or
listInstance.extend(listInstance2)
# Display an extended list of 6 elements to the terminal
print(listInstance)

# 2 part
# Create two lists
listInstance3 = ["apple", "banana", {"juice1": "grape", "juice2": "orange"}, 10]
listInstance4 = ["audi", "bmw", None, 999.5]
# Combine two lists using the + operator
fullList2 = listInstance3 + listInstance4
# Determine which magic method of lists is called when using the + operator
# it's a __add__
# Merge lists using this magic method
fullList3 = listInstance3 + listInstance4
# Print the result to the terminal
print(id(fullList2))
print(id(fullList3))