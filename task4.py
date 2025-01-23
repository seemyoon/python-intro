# 1. Create a set of several elements of the int type
setInstance = {12, 465, 1, 798}
# 2. Add another element to it
setInstance.add(999)
# 3. Create another set with several elements, some of which should be the same as in the first set
setInstance2 = {987, 12, 1}
# 4. Find common elements in two sets and place them in a new set
# setInstance & setInstance2
# or
my_intersection = setInstance.intersection(setInstance2)
# 5. Convert the resulting set to a list and print the list to the terminal
print(list(my_intersection))
