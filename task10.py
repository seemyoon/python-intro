# 1. Create an image_info function with one dict type parameter
# 2. Function waits for a dictionary that must contain at least two keys:
# - image_id
# - image_title
# 3. Function must return a string like following:
# "Image 'my cat' has id 5136"
# 4. If at least one of these keys is not in the dictionary, function must generate a TypeError error
# 5. Call the function and correctly handle the error if it appears
def check_keys_in_dict(key: str, dictionary: dict):
    if not key in dictionary.keys() and dictionary:
        raise TypeError(f"this key '{key}' doesn't exist in dictionary")
    return key


def image_info(some_dict: dict):
    return "Image '%s' has id %s" % (
        some_dict[check_keys_in_dict("image_title", some_dict)],
        some_dict[check_keys_in_dict("image_id", some_dict)],
    )


try:
    res = image_info({"image_id": 456, "image_title": "Sasha's photo"})
    print(res)
except TypeError as e:
    print(e)
