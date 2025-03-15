# Task 1
# 1. Rewrite the call to the merge_lists_to_dict function from the previous task so that it uses keyword arguments
# 2. Add another function call. First argument in this Call should be positional argument and the second should be keyword argument
def merge_lists_to_dict(num_first, num_second):
    combined_two_lists = zip(num_first, num_second)
    return dict(combined_two_lists)


new_list = merge_lists_to_dict(
    num_first=["first_key", "second_key", "third_key", "fourth_key"],
    num_second=[8.5, "asd", (78, 99, ["Aleksandr"], "cool"), {True, 88, "banana"}],
)
new_list2 = merge_lists_to_dict(
    num_first=["first_key", "second_key", "third_key", "fourth_key"],
    num_second=["zxc", (99, ["Ivan"], "super"), (465, "toy"), None],
)
print(new_list)
print(new_list2)


# Task 2
# 1. Create an update car_info_function in which all named arguments will be combined into a car dictionary
# 2. Add a new is_available key to the dictionary with the value True
# 3. Return modified dictionary from the function
# 4. Call a function with brand and price keyword arguments, their values can be any
# 5. Output the result of the function call to the terminal
def car_info_function(**car):
    car["is_available"] = True
    return car


car_info = car_info_function(brand="mercedes", model="benz", year=2015)
car_info2 = car_info_function(brand="bmw", price={"count": 20000, "currency": "$"})
print(car_info2)
