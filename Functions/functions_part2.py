# ****FUNCTIONS PART 2****

# ***OBJECTVIES***
# use the * and ** operator as parameters to a function and outside of a function
# leverage dictionary and tuple unpacking to create more flexible functions
# *args
# a special operator we can pass to functions
# gathers remaining arguments as a tuple
# this is just a parameter - you can call it whatever you want!

# we usually do this:
# def sum_all_nums(num1, num2, num3):
#     return num1 + num2 + num3
# print(sum_all_nums(4,6,9)) # 19
# it would be better to do this:
# def sum_all_nums(*args):
#     # return sum(args)
#     total = 0
#     for num in args:
#         total += num
#     return total
#
# print(sum_all_nums(4,6,9)) # 19

# ANOTHER EXAMPLE
# def ensure_correct_info(*args):
#     if "Colt" in args and "Steele" in args:
#         return "Welcome Back Colt!"
#     return "Not sure who you are..."
# print(ensure_correct_info("Colt", "Steele")) # Welcome Back Colt!
# print(ensure_correct_info()) # Not sure who you are...

# **EXERCISES**
# def contains_purple(*args):
#     if "purple" in args:
#         return True
#     return False
# print(contains_purple("green", False, 37, "blue", "hello world")) # False

# ***KWARGS***

# a special operator we can pass to functions
# gathers remaining keyword arguments as a dictionary
# this is just a parameter - you can call it whatever you want!

# def fav_colors(**kwargs):
#     for x,y in kwargs.items():
#         print(f"{x}'s favorite color is {y}")
#
# fav_colors(colt="purple", ruby="red", ethel="teal")
# print(fav_colors())
#colt's favorite color is purple
# ruby's favorite color is red
# ethel's favorite color is teal

# def special_greeting(**kwargs):
#     '''Output should be
#     print(special_greeting(David="Hello")) # Hello David!
#    print(special_greeting(Bob="Hello")) # Not sure who this is...
#    print(special_greeting(David="special")) # You get a special greeting David!
#    '''
#     print(kwargs)
#     if "David" in kwargs and kwargs["David"] == "special":
#         return "You get a special greeting David!"
#     elif "David" in kwargs:
#         return f"{kwargs['David']} David!"
#     return "Not sure who this is..."
# print(special_greeting(David="Hello"))
# print(special_greeting(Bob="Hello"))
# print(special_greeting(David="special"))

# ***EXERCISES***
# def combine_words(word,**kwargs):
#     if "prefix" in kwargs:
#         return kwargs["prefix"] + word
#     elif "suffix" in kwargs:
#         return word + kwargs["suffix"]
#     return word
#
# print(combine_words("child", prefix="man")) # manchild

# ***PARAMETER ORDERING***
# 1. parameters
# 2. *args
# 3. default paramaters
# 4. **kwargs

# *Example*
# def display_info(a,b,*args,instructor="Colt",**kwargs):
#     return [a,b,args,instructor,kwargs]
# print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))
# [1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]

# ***USING * AS AN ARGUMENT: ARGUMENT UNPACKING***
# we can use * as an argument to a function to "unpack" values

# def sum_all_values(*args):
#     total = 0
#     for num in args:
#         total += num
#     print(total)
# print(sum_all_values(1,30,2,5,6)) # 44
# nums = [1,2,3,4,5,6]
# print(sum_all_values(nums))
# above returns: TypeError: unsupported operand type(s) for +=: 'int' and 'list'
# print(sum_all_values(*nums)) # 21
# use *nums will give each value one at a time

# ***EXERCISES***
# def count_sevens(*args):
#     '''You need to call the function twice'''
#     return args.count(7)
#
# nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
#
# result1 = count_sevens(1,4,7) # 1
# result2 = count_sevens(*nums) # 14
# print(result2)

# ***USING ** AS AN ARGUMENT: DICTIONARY UNPACKING***

# def display_names(first, second):
#     return f"{first} says hello to {second}"
# names = {"first" : "Colt", "second" : "Rusty"}
#
# # print(display_names(first="Charlie", second="Sue")) # Charlie says hello to Sue
# # print(display_names(names)) # TypeError: display_names() missing 1 required positional argument: 'second'
# print(display_names(**names)) # Colt says hello to Rusty

# def add_and_multiply_numbers(a,b,c, **kwargs):
#     print(a + b * c)
#     print("Other Stuff ...")
#     print(kwargs)

# data = dict(a=1,b=2,c=3)
# OR
# data = {"a":1, "b":2, "c":3, "d":55, "name":"Tony"}
# print(add_and_multiply_numbers(**data))
# 7
# Other Stuff ...
# {'d': 55, 'name': 'Tony'}
# None

# ***EXERCISES***
# def calculate(make_float, operation, first, second, message="The result is"):
#     if "divide" in operation and make_float:
#         return f"{message} {float(first / second)}"
#     elif "add" in operation:
#         return f"{message} {first + second}"
# print(calculate(make_float=True, operation="divide", first=3.5, second=5))
# print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
# OR, Colt's way:
# def calculate(**kwargs):
#     operation_lookup = {
#         'add': kwargs.get('first', 0) + kwargs.get('second', 0),
#         'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
#         'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
#         'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
#     }
#     is_float = kwargs.get('make_float', False)
#     operation_value = operation_lookup[kwargs.get('operation', '')]
#     if is_float:
#         final = f"{kwargs.get('message','The result is')} {float(operation_value)}"
#     else:
#         final = f"{kwargs.get('message','The result is')} {int(operation_value)}"
#     return final
# print(calculate(make_float=True, operation="divide", first=3.5, second=5))
# print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))