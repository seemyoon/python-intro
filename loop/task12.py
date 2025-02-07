# Task 1
# 1. Create a dict_to_list function that will convert the dictionary to a list of tuples
# 2. Function should accept the dictionary, and return a list of tuples, each tuple must have pairs (key, value) from the dictionary
# 3. If the value of the key is an integer, it must be multiplied by 2 before adding it to the tuple


def dict_to_list(my_dictionary: dict):
    new_list = []
    for k, v in my_dictionary.items():
        if isinstance(v, int):
            v = v * 2
        new_list.append((k, v))
    return new_list


new_dict = {
    "name": "Oleksandr",
    "age": 24,
    "speciality": {
        "speciality1": "Machine learning",
        "speciality2": "Data science",
        "speciality3": "Wev development",
        "speciality4": "Backend development",
        "speciality5": "Frontend development",
        "speciality6": "DevOps",
    },
    "hometown": "Kharkiv",
}
result = dict_to_list(new_dict)
print(result)

# Task 2
# 1. Create a filter_list function that will filter the list
# 2. The function will accept two arguments - list and value type, for example int, str or bool
# 3. Function should return a new list in which only values of the specific type that was passed in the function call as the second argument will remain
# 4. The function can be called, for example, as follows: filter_list([35, True, 'abe', 10], int) and function will return [35, 10]


def filter_list(values: list, value_type):
    try:
        new_filter_list = []
        for value in values:
            if type(value) is value_type:
                new_filter_list.append(value)
        if new_filter_list:
            return new_filter_list
        else:
            return "The type you entered is not in the current list"
    except Exception as e:
        print(e)


some_list = [
    25,
    False,
    None,
    {"name": "Peter", "age": 22},
    46465,
    True,
    999,
    "asd",
    ("ad", None),
    "name",
]
result2 = filter_list(some_list, int)
print(result2)
