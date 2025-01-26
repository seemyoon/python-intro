# # print
# print("wow")
# #
# # # main types
# print("hello world")
# #
# print(123 + 321)
# #
# print(True)
# #
# print([1, 2, "three"])
# print(2, 45, 5, True)
# #
# print({"greet": "hello", "number": 23})
#
#
# # functions
# def toSum(a, b):
#     summary = a + b
#     print(summary)
#     return summary
#
#
# toSum(1, 1)
#
#
# def greet(name):
#     print(f"Hello {name}")
#
#
# greet("alex")
#
# print(__name__)
#
#
# toType = type(12)
# print(toType)
#
# listExample = [2, 3, "maria"]
# print(listExample)
#
# distExample = {"name": "elena", "age": 45}
# print(distExample)
#
# print(type(distExample))
#
# exampleId = 1
# print(id(exampleId))
#
# print(len(listExample))
#
# listOfNumbers = [1, 3, 5]
#
# print(sum(listOfNumbers))
#
# print(dir())
#
# # userInput = input("pls enter your name")
#
#
# # print(userInput)
#
# # statement
# exampleOfNumber = 2
#
# exampleOfLetter = "f"
#
# if exampleOfNumber > 1:
#     print("your value more than 1")
#
# # expression
# operation = 4 - 2
#
# wordOperation = "Hello " + "world"
#
# print(wordOperation)
#
# # variables
# your_number = 3
#
# # constant variables
# MY_PASSWORD = "qweqwe"
#
# # reassign variables
# your_value = "asd"
# print(your_value)
# your_value = 2
# print(your_value)
#
# # id of value in the memory
# print(id(your_value))
#
# findId = 123
# findId2 = 123
#
# print(id(findId))
#
# print(id(findId) == id(findId2))
#
# # variableString = "jkhdfs"
# # print(type(variableString))
#
# print(type(object))
#
# inst = isinstance(234, int)
# inst2 = isinstance("sasha", int)
#
# print(inst)
# print(inst2)
#
# variableString = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."""
# print(variableString)
#
#
# # Built-in func in stings (3)
# exString = "Lorem Ipsum is simply dummy text of the printing"
# print(exString[7:10])  # range
#
# exString2 = "cvb"
# print(len(exString2))
#
# exString3 = "iuy"
# print(exString3[2])
#
#
# # prevent error of quotes
# preventExString = "It's my life"
# print(preventExString)
# # preventExString2 = 'It\'s my life'
#
# # methods stings
# # upper()
# trainForMethod = preventExString.upper()
# print(trainForMethod)
# # replace()/simply instance and with similar variables/
# preventExString.replace("my", "your")
# print(preventExString)
#
# trainForMethod2 = preventExString.replace("my", "your")
# print(trainForMethod2)
# # count()
# trainForMethod3 = preventExString.count(" ")
# print(trainForMethod3)
#
# # index()
# trainForMethod4 = preventExString.index("m")
# print(trainForMethod4)
#
# # capitalize()
# trainForMethod5 = preventExString.capitalize()
# print(trainForMethod5)
#
# # lower()
# trainForMethod6 = preventExString.lower()
# print(trainForMethod6)
#
# # find() /if we have value and no/
# trainForMethod7a = preventExString.find("my")
# print(trainForMethod7a)
#
# trainForMethod7b = preventExString.find("key")
# print(trainForMethod7b)
#
# # split()
# trainForMethod8 = preventExString.split(" ")
# print(trainForMethod8)
#
# # String Concatenation
# # Standard concatenation /simply ex and if we pass not only string, but integer as well:/
# exStringConcat = "Lorem Ipsum is" + "simply dummy text"
# print(exStringConcat)
#
# exStringConcat2 = "Lorem Ipsum is" + "simply dummy text" + str(32)
# print(exStringConcat2)
#
# # f-stings
# firstPartOfSent = "Lorem Ipsum is"
# secondPartOfSent = "simply dummy text"
# someNum = 2134
#
# exStringConcat3 = f"{firstPartOfSent}  {secondPartOfSent} {someNum}"
# print(exStringConcat3)
#
# # method format()
# name = "Sasha"
# town = "Kharkiv"
#
# exStringConcat3 = "hello, i'm {} and i from {}".format(name, town)
# print(exStringConcat3)
#
# # s%
# exStringConcat4 = "hello, i'm %s and i from %s" % (name, town)
# print(exStringConcat4)
#
#
# listInstance = [132, 789.5, "asd", True, False]
# tupleInstance = (132, 789.5, "asd")
#
# example = tupleInstance[0:1]
#
# print(type(tupleInstance))
# print(type(example))
#
# s = {1, 2, 3}
# listS = list(s)
#
#
# # function
# def fruits_func(my_name, fruits):
#     print(id(fruits))
#     for fruit in fruits:
#         print("{} likes {}".format(my_name, fruit))
#
#
# fruits_collection = ["banana", "cherry", "ananas"]
# name = "Oleksandr"
#
# fruits_func(name, fruits_collection)
#
# enumerate()
# main_list = ["sub_first_key", "sub_second_key", "sub_third_key", "sub_fourth_key"]
# test_list = [54, "asd", None, {"sub_first_key": 78, "sub_second_key": "asd"}]
counter = 0


def inc_counter(counter):
    counter += 1


def dec_counter(counter):
    counter -= 1


inc_counter(counter)
print(counter)
