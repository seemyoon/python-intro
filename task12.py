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
