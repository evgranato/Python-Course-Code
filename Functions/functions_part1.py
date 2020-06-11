# ****FUNCTIONS PART 1****
# **OBJECTIVES**
# describe what a function is and how they are useful
# explain exactly what the return keyword does and some of the side effects of using it
# add parameters to functions to output different data
# define and diagram how scope works in a function
# add keyword arguments to functions

# What is a function?
# a process for executing a task
# it can accept input and return an output
# useful for executing similar procedures over and over

# colors = ["red", "orange", 'yellow', "green", "blue", 'indigo']
# print(colors)
# print() is a function
# colors.append("violet")
# print(colors)

# Why use functions?
# stay DRY- Don't - Repeat - Yourself! Opposite is WET Write - Everything - Twice
# Clean up and prevent code duplication
# "Abstract away" code for other users
#     Imagine having to write the "print()" function for every program you wrote

# **FUNCTION STRUCTURE**
# def name__of__function():
#   block of runnable code

# def say_hi():
#     print("Hi")
# say_hi()
# returns: "Hi"
# def sing_happy_birthday():
#     print("Happy Birthday To You")
#     print("Happy Birthday To You")
#     print("Happy Birthday Dear You")
#     print("Happy Birthday To You")
# sing_happy_birthday()

# ***EXERCISES***
# def make_noise():
#     print("THE CROWD GOES WILD")
# make_noise()

# ***RETURNING VALUES FROM FUNCTIONS***
# def print_square_of_7():
#     print(7**2)
# print_square_of_7()

# def square_of_7():
#     7**2
# result = square_of_7()
# print(result)
# returns: None
# if we do this instead:
# def square_of_7():
#     return 7**2
# result = square_of_7()
# print(result)

# ***RETURN***
# Exits the function
# Outputs whatever value is placed after the return keyword
# Pops the function off of the call stack
# if you want to learn more about this: https://www.cs.ucsb.edu/~pconrad/cs8/topics.beta/theStack/02/

# ***COIN FLIP FUNCTION***
# from random import random

# def flip_coin():
#     # generate random number 0-1
#     r = random()
#     if r > 0.5:
#         return "Heads"
#     else:
#         return "Tails"
# print(flip_coin())

# OR this is better

# def flip_coin():
#     if random() > 0.5:
#         return "Heads"
#     else:
#         return "Tails"
# print(flip_coin())

# ***EXERCISE***
# def speak_pig():
#     return "oink"

# def generate_evens():
#     return [num for num in range(1,50) if num % 2 == 0]
# print (generate_evens())

# ***PARAMETERS***
# How to accept inputs
# def square(num):
#     return num * num
#
# print(square(4))
# print(square (8))

# def sing_happy_birthday(name):
#     print("Happy Birthday To You")
#     print("Happy Birthday To You")
#     print(f"Happy Birthday Dear {name}")
#     print("Happy Birthday To You")
#
# sing_happy_birthday("Evan")

# **ADD**
# def add(a,b):
# #     return a + b
# # print(add(1,2))
# returns: 3
# **MULTIPLY**
# def multiply(a,b):
#     return a + b
# print(multiply(2,2))
# returns: 4

# **NAMING PARAMETERS**
# not great
# def print_full_name(string1 ,string2):
#     return(f"Your Full name is {string1} {string2}")
# print(print_full_name("Evan", "Granato"))
# BETTER TO USE:
# def print_full_name(first_name ,last_name):
#     return(f"Your Full name is {first_name} {last_name}")
# print(print_full_name("Evan", "Granato"))

# **PARAMETERS VS ARGUMENTS**
# a PARAMETER is a variable in a method definition
# when a method is called, the ARGUMENTS are the data you pass into the method's PARAMETERS
# PARAMETER is a variable in the declaration of function
# ARGUMENT is the actual value of this variable that gets passed to function

# def divide(num1, num2):
#     return num1/num2
#
# print(divide(2,5))
# print(divide(5,2))

# ***EXERCISES***
# def yell(word):
#     return word.upper() + "!"
# print(yell("go away"))

# **COMMON RETURN MISTAKES**
# WRONG VERSION
# def sum_odd_numbers(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 != 0:
#             total += num
#         return total
#
# print(sum_odd_numbers([1,2,3,4,5,6,7]))
# returns 1 instead of 16
# should indent return under the for.
# RIGHT FUNCTION:
# def sum_odd_numbers(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 != 0:
#             total += num
#     return total
#
# print(sum_odd_numbers([1,2,3,4,5,6,7]))

# def is_odd_number(num):
#     if num % 2 != 0:
#         return True
    # else:
    #     return False
    # YOU DON'T NEED TO DO ELSE: JUST INDENT TO RETURN FALSE IF PREVIOUS CHECK
    # return False

# print(is_odd_number(4))
# print(is_odd_number(9))

# ***EXERCISES***
# FIGURE OUT THE BROKEN FUNCTION
# def count_dollar_signs(word):
#     count = 0
#     for char in word:
#         if char == '$':
#             count += 1
#     return count
#
# print(count_dollar_signs("$uper $ize"))

# ***DEFAULT PARAMETERS***
# def exponent(num, power=2): # the =2 is a default parameter
#     return num ** power
#
# print(exponent(2,3)) # 8
# print(exponent(3,2)) # 9
# print(exponent(7)) # 49

# def add(a=10, b=20):
#     return a + b
# print(add()) # 30
# print(add(1,10)) # 11

# MORE COMPLEX EXAMPLE
# def show_information(first_name = "Colt", is_instructor = False):
#     if first_name == "Colt"and is_instructor:
#         return "Welcome Back Instructor Colt"
#     elif first_name == "Colt":
#         return "I really thought you were an instructor..."
#     else:
#         return f"Hello {first_name} !"
#
# print(show_information()) # I really thought you were an instructor...
# print(show_information(is_instructor=True)) # Welcome Back Instructor Colt
# print("Molly") # Molly

# WHY HAVE DEFAULT PARAMETERS?
# Allows you to be more defensive
# Avoids errors with incorrect parameters
# More readable examples!

# WHAT CAN DEFAULT PARAMETERS BE?
# Anything! Functions, lists, dictionaries, strings, booleans

# def add(a,b):
#     return a + b
# def math(a,b,fn=add):
#     return fn(a,b)
# def subtract(a,b):
#     return a-b
# print(math(2,2)) # 4
# print(math(2,2,subtract

# ***EXERCISES***
# def speak(animal="dog"):
#     if animal == "pig":
#         return "oink"
#     elif animal == "duck":
#         return "quack"
#     elif animal == "cat":
#         return "meow"
#     elif animal == "dog":
#         return "woof"
#     else:
#         return "?"
# print(speak())

# OR

# def speak(animal="dog"):
#     noises = {"pig": "oink", "duck": "quack", "cat": "meow", "dog": "woof"}
#     noise = noises.get(animal)
#     if noise:
#         return noise
#     return "?"
# print(speak("llama"))

# ***KEYWORD ARGUMENTS***
# def full_name(first, last):
#     return f"Your name is {first} {last}"
# print(full_name("evan","granato")) # Your name is evan granato
# print(full_name(last="Granato", first="Evan")) # Your name is Evan Granato
# WHY USE KEYWORD ARGUMENTS?
# It's useful when passing a dictionary to a function and unpacking it's values
# Different than defining a function. When you are invoking a function like above, you are making a keyword argument, not defining default parameters

# ***SCOPE***
# Scope is where our variables can be accessed.
# variables created in functions are scoped to that function
# instructor = "Colt"
# def say_hello():
#     return f"Hello {instructor}"
# print(say_hello()) # Hello Colt
# the instructor variable is "GLOBAL" because it's outside of the function
# def say_hello():
#     instructor = "Colt"
#     return f"Hello {instructor}"
# print(say_hello()) # Hello Colt
# print(instructor) # NameError: name 'instructor' is not defined

# GLOBAL
# total = 0
#
# def increment():
#     total = 0 # this will return 1, unlike total above
#     total += 1
#     return total
# print(increment()) # UnboundLocalError: local variable 'total' referenced before assignment
# Or you could do this:
# total = 0
#
# def increment():
#     global total # using global will pull it in to the function
#     total += 1
#     return total
# print(increment())

# **NONLOCAL**
# lets us modify a parent's variables in a child (aka nested) function
# def outer():
#     count = 0
#     def inner():
#         nonlocal count # count isn't global, but nonlocal
#         count += 1
#         return count
#     return inner()
# You won't use global or nonlocal frequently, but it's essential to understand scope

# ****DOCUMENTING FUNCTIONS****
# Use """ """
# Essential when writing complex functions
# def say_hello():
#     """A simple function that returns the string hello"""
#     return "Hello!"
# print(say_hello()) # Hello!
# print(say_hello.__doc__) # A simple function that returns the string hello
# print(print.__doc__)

# ****RECAP****
# functions are procedures for executing code. They accept inputs and return outputs when the return keyword is used
# to create inputs, we make parameters which can have default values, we call those default parameters
# variables defined inside of functions are scoped to that function - watch out for that!
# when invoking a function, we can pass in keyword arguments in any order, we'll see this more later
# be careful to not return too early in your conditional logic and refactor when you can to remove unecessary conditional logic.
# Make sure you don't return in a loop too early as well.
