# 1. Create any dictionary using keys with different value types
# 2. Convert dictionary to JSON
# 3. Print the resulting JSON to the terminal
# 4. Print the type of the resulting value to the terminal
import json

my_pet = {
    "name": "Murka",
    "age": 4,
    "kind_of_animal": {"species": "cat", "breed": "Siamese"},
}

print(type(my_pet))
res = json.dumps(my_pet, indent=2)

print(res)
print(type(res))
