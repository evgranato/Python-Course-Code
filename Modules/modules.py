# ***MODULES***
# OBJECTIVES
# define what a module is
# import code from built-in modules
# import code from other files
# import code from external modules using pip
# describe common module patterns
# describe the request/response cycle in HTTP
# Use the requests module to make requests to web apps

# ** WORKING WITH BUILT-IN MODULES**
# Why use modules?
# - Keep python files small
# - Reuse code across multiple files by importing
# - A module is just a python file!

# **EXAMPLE**
# THERE ARE TONS OF MODULES THAT ARE BUILT IN
# import random
#
# print(random.choice(["apple", "banana", "cherry", "durian"]))
# print(random.shuffle(["apple", "banana", "cherry", "durian"]))

# import random as omg_so_random # giving random a new variable name
#
# print(omg_so_random.choice(["apple", "banana", "cherry", "durian"]))
# print(omg_so_random.shuffle(["apple", "banana", "cherry", "durian"]))

# **IMPORT PARTS OF A MODULE**
# the FROM keyword lets you import parts of a module
# handy rule of thumb; only import what you need!
# if you still want to import everything, you can also use from MODULE import * pattern

# from random import choice, randint
#
# # print(random.choice(["apple", "banana", "cherry", "durian"]))
# # print(random.randint(0,100))
# # above gives error, you have to remove random because you have taken choice and randint out.
# print(choice(["apple", "banana", "cherry", "durian"]))
# print(randint(1,100))

# **DIFFERENT WAYS TO IMPORT**
# - import random
# - import random as omg_so_random
# - from random import *
# - from random import choice, random
# - from random import choice as given_name, shuffle as mix_up_fruits

# **EXERCISES**
# import math
#
# answer = math.sqrt(15129)
# print(answer)

# def contains_keyword(*args):
#     import keyword
#     for val in args:
#         if keyword.iskeyword(val):
#             return True
#         return False
# print(contains_keyword("hello", "goodbye")) # False
# print(contains_keyword("def", "haha", "lol", "chicken", "alaska")) # True

# **CUSTOM MODULES**
# - You can import your own code too
# - The syntax is the same as before
# - Import from the name of the python file

# **EXAMPLE**
# file1.py
# def fn():
#     return "do some stuff"
# def other_fn():
#     return "do some other stuff"
#
# # file2.py
# import file1
# file1.fn() # 'do some stuff'
# file2.fn() # 'do some other stuff'

# **EXAMPLES IN OTHER FILES**
# we made 3 files: bananas.py, apples.py and fruits.py
# fruits.py pulled functions from the other 2 files.

# **EXTERNAL MODULES**
# Built in modules come with Python
# External modules are downloaded from the internet
# Py Pi on the internet
# You can download external modules using pip
# pip is package managements system for Python
# python3 -m pip install NAME_OF_PACKAGE

# **The__name__Variable**

# __name__
# when run, every python file has a __name__ variable
# if the file is the main file being run, it's value is "__main__"
# Otherwise, it's value is the file name
# when you import something:
# 1. it tries to find the module (if it fails, it throws an error)
# 2. runs the code inside of the module being imported

# **IGNORING CODE ON IMPORT**
# if __name__ == "__main__":
# this code will only run
# if the file is the main file