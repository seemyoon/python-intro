# 1. Create a route_info function which accepts dictionary as parameter
# 2. If the dictionary has a distance key and its value is an integer, return the string "Distance to your destination is ‹distance›"
# 3. Otherwise, if there are speed and time keys in the dictionary, return the string "Distance to your destination is ‹speed *time>"
# 4. Otherwise, return the string "No distance info is available"
# 5. Call the function several times with different arguments
def route_info(some_dict: dict):
    if some_dict.get("distance") and type(some_dict.get("distance")) is int:
        return f"Distance to your destination is {some_dict['distance']}"

    if some_dict.get("speed") and some_dict.get("time"):
        distance = some_dict["speed"] * some_dict["time"]
        return f"Distance to your destination is {distance}"

    return "No distance info is available"


route_dict1 = {"distance": 30}
route_dict2 = {"distance": 40}
route_dict3 = {"speed": 150, "time": 60}
route_dict4 = {"speed": 100, "time": 60}
route_dict5 = {"time": 60}

result = route_info(route_dict1)
print(result)
