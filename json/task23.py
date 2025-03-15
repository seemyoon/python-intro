# 1. Create any list of dictionaries
# 2. Convert such list to JSON
# 3. Print the resulting JSON to the terminal
# 4. Print the type of the resulting value to the terminal
# 5. Convert JSON back to list of dictionaries
# 6. Print resulting list to the terminal and compare to the original list
import json

deals = [
    {"id": 1, "title": "Laptop Sale", "discount": "20%", "price": 800},
    {"id": 2, "title": "Smartphone Discount", "discount": "15%", "price": 500},
    {"id": 3, "title": "Headphones Offer", "discount": "10%", "price": 100},
    {"id": 4, "title": "Gaming Console Bundle", "discount": "25%", "price": 300},
]

converted_list_to_json = json.dumps(deals)
print(converted_list_to_json)
print(type(converted_list_to_json))

converted_list_from_json = json.loads(converted_list_to_json)
print(converted_list_from_json)

print(converted_list_from_json == deals)  # True
