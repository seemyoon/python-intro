# 1. Create a merge_lists_to_dict function
# 2. The function must have two parameters
# 3. The function should combine two lists using the built-in zip function
# 4. Convert a zip object to a dictionary and return it from the function
# 5. Call a function by passing it two lists as arguments
# 6. Output the result of the function call to the terminal
def merge_lists_to_dict(num_first, num_second):
    combined_two_lists = zip(num_first, num_second)
    return dict(combined_two_lists)


new_list = merge_lists_to_dict(
    ["first_key", "second_key", "third_key", "fourth_key"],
    [8.5, "asd", (78, 99, ["Aleksandr"], "cool"), {True, 88, "banana"}],
)
print(new_list)
