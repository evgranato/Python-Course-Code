# ***DECORATORS***
# *INTRODUCING DECORATORS*
# Higher Order Function:
# def sum(n, func):
#     total = 0
#     for num in range(1,n+1):
#         total += func(num)
#     return total
# def square(x):
#     return x*x
#
# def cube(x):
#     return x*x*x
#
# print(sum(3, square)) # 14
# print(sum(3, cube)) # 36

# from random import choice
#
# def greet(person):
#     def get_mood():
#         msg = choice(("Hello there ", "Go away ", "I love you "))
#         return msg
#     result = get_mood() + person
#     return result
#
# print(greet("Toby"))

# from random import choice
#
# def make_laugh_func():
#     def get_laugh():
#         l = choice(("HAHAHA", "lol", "tehehe"))
#         return l
#     return get_laugh
#
# laugh = make_laugh_func()
# print(laugh())

# from random import choice
#
# def make_laugh_at_func(person):
#     def get_laugh():
#         laugh = choice(("HAHAHA", "LOL", "TEHEHE"))
#         return f"{laugh} {person}"
#     return get_laugh
#
# laugh_at = make_laugh_at_func("Linda")
# print(laugh_at())
# print(laugh_at())
# print(laugh_at())
# print(laugh_at())

# *INTRODUCTION TO DECORATORS*
# - Decorators are functions
# - Decorators wrap functions and enhance their behavior
# - Decorators are examples of higher order functions
# - Decorators have their own syntax, using "@" (syntactic sugar)
# WITHOUT SYNTACTIC SUGAR:
# def be_polite(fn):
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper
# def greet():
#     print("My name is Colt.")
#
# def rage():
#     print("I HATE YOU")
#
# greet = be_polite(greet)
# polite_rage = be_polite(rage)
# print(greet())
# print(polite_rage())

# WITH SYNTACTIC SUGAR:
# def be_polite(fn):
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper
#
# @be_polite
# def greet():
#     print("My name is Matt.")
#
# @be_polite
# def rage():
#     print("I HATE YOU!")
#
# print(greet())
# print(rage())

# **DECORATORS WITH DIFFERENT SIGNATURES**

# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper
# @shout
# def greet(name):
#     return f"Hi, I'm {name}"
# @shout
# def order(main, side):
#     return f"Hi, I'd like the {main}, with a side of {side}, please."
#
# print(greet("evan")) # HI, I'M EVAN
# print(order("Eggplant Parmesan", "pasta")) # TypeError: wrapper() takes 1 positional argument but 2 were given
# WE NEED TO USE *args and **kwargs

# def shout(fn):
#     def wrapper(*args, **kwargs):
#         return fn(*args, **kwargs).upper()
#     return wrapper
# @shout
# def greet(name):
#     return f"Hi, I'm {name}"
# @shout
# def order(main, side):
#     return f"Hi, I'd like the {main}, with a side of {side}, please."
#
# @shout
# def lol():
#     return "lol"
#
# print(greet("evan")) # HI, I'M EVAN
# print(order("Eggplant Parmesan", "pasta")) # HI, I'D LIKE THE EGGPLANT PARMESAN, WITH A SIDE OF PASTA, PLEASE.
# print(lol()) # LOL

# **USING WRAPS TO PRESERVE METADATA**

# def log_function_data(fn):
#     def wrapper(*args, **kwargs):
#         '''I AM WRAPPER FUNCTION'''
#         print(f"You are about to call {fn.__name__}")
#         print(f"Here's the documentation: {fn.__doc__}")
#         return fn(*args, **kwargs)
#     return wrapper
#
# @log_function_data
# def add(x,y):
#     '''Adds two numbers together.'''
#     return x + y

# print(add(10,30)) # returns below:
# You are about to call add
# Here's the documentation: adds two numbers together.
# 40
# THESE ALL GIVE THE '''I AM WRAPPER FUNCTION''', NOT THE REAL DOCUMENTATION
# print(add.__doc__)
# print(add.__name__)
# print(help(add))
# YOU CAN USE A DECORATOR PATTERN BY USING: from functools import wraps
# from functools import wraps
# def log_function_data(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         '''I AM WRAPPER FUNCTION'''
#         print(f"You are about to call {fn.__name__}")
#         print(f"Here's the documentation: {fn.__doc__}")
#         return fn(*args, **kwargs)
#     return wrapper
#
# @log_function_data
# def add(x,y):
#     '''Adds two numbers together.'''
#     return x + y
#
# print(add.__doc__)
# print(add.__name__)
# print(help(add))

# **BUILDING A SPEED-TEST DECORATOR**
# from time import time
# from functools import wraps
# def speed_test(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         start_time = time()
#         result = fn(*args, **kwargs)
#         end_time = time()
#         print(f" Executing {fn.__name__}")
#         print(f"Time Elapsed: {end_time - start_time}")
#         return result
#     return wrapper
#
# @speed_test
# def sum_nums_gen():
#     return sum(x for x in range(50000000))
#
# @speed_test
# def sum_nums_list():
#     return sum([x for x in range(50000000)])
#
# print(sum_nums_gen())
# print(sum_nums_list())
# RESULTS:
# Time Elapsed for list: 3.2763640880584717
# 1249999975000000
#  Executing sum_nums_list
# Time Elapsed for list: 3.703742027282715
# 1249999975000000

# **EXERCISES**
# from functools import wraps
#
# def show_args(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print(f"Here are the args {(args)}")
#         print(f"Here are the kwargs: {dict(kwargs)}")
#     return wrapper
#
# @show_args
# def do_nothing():
#     pass
#
# print(do_nothing(1,2,3, a="hi", b="bye"))

# **ANOTHER EXAMPLE: ENSURING ARGS WITH A DECORATOR**

# from functools import wraps
#
# def ensure_no_kwargs(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if kwargs:
#             raise ValueError("No kwargs allowed! Sorry :(")
#         return fn(*args, **kwargs)
#     return wrapper
#
# @ensure_no_kwargs
# def greet(name):
#     print(f"Hi there {name}")
#
# print(greet("Tony")) # Hi there Tony
# print(greet(name="Tony")) # ValueError: No kwargs allowed! Sorry :(

# **EXERCISES**
# from functools import wraps
#
# def double_return(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         argument = fn(*args, **kwargs)
#         return [argument , argument]
#     return wrapper
#
# @double_return
# # def add(x,y):
# #     return x + y
# #
# # print(add(1,2))
# def greet(name):
#     return f"Hi, I'm {name}."
#
# print(greet("Tom"))

# from functools import wraps
#
# def ensure_fewer_than_three_args(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if len(args) < 3:
#             return fn(*args, **kwargs)
#         else:
#             raise ValueError("Too many arguments!")
#     return wrapper
#
# @ensure_fewer_than_three_args
# def add_all(*nums):
#     return sum(nums)
#
# print(add_all(1,2,3,4))

# from functools import wraps
#
# def only_ints(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if any([arg for arg in args if type(arg) != int]):
#             raise ValueError("Please only invoke with integers.")
#         else:
#             return fn(*args, **kwargs)
#     return wrapper
#
# @only_ints
# def add(x,y):
#     return x + y
#
# print(add(1, 2))

# from functools import wraps
#
# def ensure_authorized(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if kwargs.get("role") == "admin":
#             return fn(*args, **kwargs)
#         else:
#             return "Unauthorized"
#     return wrapper
#
# @ensure_authorized
# def show_secrets(*args, **kwargs):
#     return "Shh! Don't tell anybody!"
#
# print(show_secrets(role="nobody"))

# **WRITING AN ENSURE_FIRST_ARG_IS DECORATOR**
# from functools import wraps
#
# def ensure_first_arg_is(val):
#     def inner(fn):
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#             if args and args[0] != val:
#                 return f"First arg needs to be {val}"
#             return fn(*args, **kwargs)
#         return wrapper
#     return inner
#
# @ensure_first_arg_is("burrito")
# def fav_foods(*foods):
#     print(foods)
# print(fav_foods("burrito", "ice cream"))
# print(fav_foods("ice cream", "burrito"))
#
# @ensure_first_arg_is(10)
# def add_to_ten(num1, num2):
#     return num1 + num2
# print(add_to_ten(10,12))
# print(add_to_ten(1,2)) # RETURNS:
# # ('burrito', 'ice cream')
# # None
# # First arg needs to be burrito
# # 22
# # First arg needs to be 10

# **ENFORCING ARGUMENT TYPES WITH A DECORATOR**
# Example from StackOverflow:
# def enforce(*types):
#     def decorator(fn):
#         def new_func(*args, **kwargs):
#             #convert args into something mutable
#             newargs = []
#             for (a, t) in zip(args,types):
#                 newargs.append(t(a))
#             return fn(*newargs, **kwargs)
#         return new_func
#     return decorator
#
# @enforce(str, int)
# def repeat_msg(msg, times):
#     for time in range(times):
#         print(msg)
#
# @enforce(float, float)
# def divide(a,b):
#     print(a/b)
#
# print(divide("1","4"))

# print(repeat_msg("hello", "5")) # Returns:
# hello
# hello
# hello
# hello
# hello

# **EXERCISES**
# from functools import wraps
# from time import sleep
#
# def delay(timer):
#     def inner(fn):
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#             print(f"Waiting {timer}s before running say_hi")
#             sleep(timer)
#             return fn(*args, *kwargs)
#         return wrapper
#     return inner
#
# @delay(3)
# def say_hi():
#     return "hi"
# print(say_hi()) # RETURNS:
# # Waiting 3s before running say_hi
# # hi

