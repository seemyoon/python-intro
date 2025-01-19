# print
print("wow")
#
# # main types
print("hello world")
#
print(123 + 321)
#
print(True)
#
print([1, 2, "three"])
print(2, 45, 5, True)
#
print({"greet": "hello", "number": 23})


# functions
def toSum(a, b):
    summary = a + b
    print(summary)
    return summary


toSum(1, 1)


def greet(name):
    print(f"Hello {name}")


greet("alex")

print(__name__)


toType = type(12)
print(toType)

listExample = [2, 3, "maria"]
print(listExample)

distExample = {"name": "elena", "age": 45}
print(distExample)

print(type(distExample))

exampleId = 1
print(id(exampleId))

print(len(listExample))

listOfNumbers = [1, 3, 5]

print(sum(listOfNumbers))

print(dir())

# userInput = input("pls enter your name")


# print(userInput)

# statement
exampleOfNumber = 2

exampleOfLetter = "f"

if exampleOfNumber > 1:
    print("your value more than 1")

# expression
operation = 4 - 2

wordOperation = "Hello " + "world"

print(wordOperation)

# variables
your_number = 3

# constant variables
MY_PASSWORD = "qweqwe"

# reassign variables
your_value = "asd"
print(your_value)
your_value = 2
print(your_value)

# id of value in the memory
print(id(your_value))

findId = 123
findId2 = 123

print(id(findId))

print(id(findId) == id(findId2))

variableString = "jkhdfs"
print(type(variableString))

print(type(object))

inst = isinstance(234, int)
inst2 = isinstance("sasha", int)

print(inst)
print(inst2)
