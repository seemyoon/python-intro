# Part 1
# 1. Create a dictionary with several keys, the values of which should be of type str +
# 2. Create a new dictionary based on an existing one, in which the values of all keys must be in upper case
# 3. Print the resulting dictionary to the terminal

specialities_dictionary = {
    "speciality1": "Machine learning",
    "speciality2": "Data science",
    "speciality3": "Wev development",
    "speciality4": "Backend development",
    "speciality5": "Frontend development",
    "speciality6": "DevOps",
}

updated_specialities_dictionary = {
    k: v.upper() for k, v in specialities_dictionary.items()
}
print(updated_specialities_dictionary)

# Part 2
# 1. Create a list with elements of type str
# 2. From this list, create a new list that will contain only strings which have more than 4 characters
# 3. Reverse the order of the elements in the list
# 4. Print the resulting list to the terminal

string_list = ["hello", "world", "Python", "AI", "ML"]

new_string_list = [value for value in string_list if len(value) > 4]
reversed_string_list = list(reversed(new_string_list))

print(reversed_string_list)
