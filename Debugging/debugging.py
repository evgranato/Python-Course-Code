# *** DEBUGGING***
# Objectives
# Explaing common errors and how they occur in Python
# Use pdb to set breakpoints and step through code
# Use try and except blocks to handle errors

# **COMMON TYPES OF ERRORS**
# you're going to make mistakes
# so how do you fix them?
# understand them

# SyntaxError
# occurs when python encounters incorrect syntax
# usually due to typos or not knowing python well enough

# NameError
# occurs when a variable hasn't been defined.
# print(test)

# TypeError
# an operation or function is applied to the wrong type
# python can't interpret an operation on two different data types

# IndexError
# occurs when you try to access an element in a list using an invalid index

# ValueError
# this occurs when a built-in operation or function receives an argument that hast the right type but inappropriate value
# print(int("f"))

# KeyError
# occurs when a directory does not have a specific key

# AttributeError
# occurs when a variable does not have an attribute
# [1,2,3].hello #AttributeError: 'list' object has no attribute 'hello'

# **RAISE YOUR OWN EXCEPTION**
# if you write your own code, you can throw errors using the raise keyword

# raise ValueError("invalid value")

# def colorize(text, color):
#     colors = ("cyan", "yellow", "blue", "green", "magenta")
#     # if type(text) is not str:
#     #     raise TypeError("text must be a string")
#     if color not in colors:
#         raise ValueError(f"{color} is not a color")
#     print(f"Printed {text} in {color}")
#
# # colorize(3, "red") # TypeError: text must be a string
# colorize("dog", "red") # ValueError: red is not a color

# **HANDLE ERRORS**
# in python, it is STRONGLY encouraged to use try/except blocks, to catch exceptions
# when we can do something about them. Let's see what this looks like:

# foobar # NameError: name 'foobar' is not defined
# try:
#     foobar
# except NameError as err:
#     print("PROBLEM!") # PROBLEM!
# print("after the try") # after the try

# what we are doing here is catching every error, which means we are not able
# to correctly identify "what" went wrong. It is highly discouraged to do this.

# try:
#     foobar
# except NameError:
#     print("PROBLEM!")


# def get(d,key):
#     try:
#         return d[key]
#     except KeyError:
#         return None
#
# d = {"name" : "Ricky"}
#
# print(get(d, "city")) # None

# **ELSE AND FINALLY**

# try:
#     num = int(input("Please enter a number: "))
# except:
#     print("That's not a number")
# else:
#     print("I'M IN THE ELSE")
# finally:
#     print("RUNS NO MATTER WHAT")

# while True:
#     try:
#         num = int(input("Please enter a number: "))
#     except ValueError:
#         print("That's not a number")
#     else:
#         print("GOOD JOB. YOU ENTERED A NUMBER")
#         break
#     finally:
#         print("RUNS NO MATTER WHAT")
# print("Rest of Game Logic Runs")

# def divide(a,b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("don't divide by zero please")
#     except TypeError as err:
#         print("a and b must be int or float")
#         print(err)
#     else:
#         print(f"{a} divided by {b} is {result}")
#
#
# print(divide(1,2)) # 0.5
# print(divide(1,0)) # something went wrong...
# print(divide(1,"a")) # unsupported operand type(s) for /: 'int' and 'str'

# **DEBUGGING WITH PDB**
# python debugger
# module that we need to import to our code
# import pdb; pdb.set_trace()
# import pdb
# first = "First"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)
# type l and you get list of where you are in (pdb.set_trace())
# type n and it will move to the next line of code
# type c and it will "continue". This is useful to quit

# def add_numbers(a,b,c,d):
#     import pdb; pdb.set_trace()
#
#     return a + b + c + d
# print(add_numbers(1,2,3,4))

# **EXERCISES**
# Write a function called divide, which accepts two parameters (you can call them
# num1 and num2). The function should return the result of num1 divided by num2.
# If you do not pass the correct amount of arguments to the function,
# it should return the string "Please provide two integers or floats".
# If you pass as the second argument a 0, Python will raise a ZeroDivisionError,
# so if this function is invoked with a 0 as the value of num2, return the string
# "Please do not divide by zero"

# Examples

# divide(4,2)  2
# divide([],"1")  "Please provide two integers or floats"
# divide(1,0)  "Please do not divide by zero"

# def divide(num1, num2):
#     # return num1 / num2
#     try:
#         return int(num1 / num2)
#     except ZeroDivisionError:
#         return "Please do not divide by zero"
#     except TypeError:
#         return "Please provide two integers or floats"
#
# print(divide(4,2)) # 2
# divide([],"1")  #"Please provide two integers or floats"
# divide(1,0)  #"Please do not divide by zero"