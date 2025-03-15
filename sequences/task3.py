# Create an empty dictionary
dictInstance = {}

# Three times ask the user to enter the name of the key first, and then enter a value for this key.
# There should be a total of 6 text input requests.
inputKey1 = input("enter the first key: ")
inputValue1 = input("enter the first value: ")
inputKey2 = input("enter the second key: ")
inputValue2 = input("enter the second value: ")
inputKey3 = input("enter the third key: ")
inputValue3 = input("enter the third value: ")

# When receiving data from the user, add keys with values to the dictionary according to what the user entered
dictInstance[inputKey1] = inputValue1
dictInstance[inputKey2] = inputValue2
dictInstance[inputKey3] = inputValue3

# Print the resulting dictionary in the terminal
print(dictInstance)

# Receiving keys from dicts convert to list and print it
listInstance = list(dictInstance)
print(listInstance)
