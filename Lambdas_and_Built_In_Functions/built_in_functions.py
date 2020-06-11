# ***Built in List Functions***
# **map**
# a standard function that accepts at least 2 arguments, a function and "iterable"
# iterable - something that can be iterated over (lists, strings, dictionaries, sets, touples
# runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure

# nums = [2,4,6,8,10]
#
# doubles = map(lambda x : x*2, nums)
# print(list(doubles)) # [4,8,12,16,20]
# OR
# for num in doubles:
#     print(num)
# OR
# doubles = list(map(lambda x: x*2,nums))
# print(doubles)

# map objects can only run once.
# typically you want create a list

# people = ["Darcy", "Christina", "Dana", "Annabel"]
# want uppercased names
# caps = list(map(lambda name:name.upper(),people))
# print(caps) # ['DARCY', 'CHRISTINA', 'DANA', 'ANNABEL']

# names = [
#     {"first" : "Rusty", "last" : "Steele"},
#     {"first" : "Colt", "last" : "Steele"},
#     {"first" : "Blue", "last" : "Steele"}
# ]
#
# first_names = list(map(lambda x: x["first"], names))
# print(first_names) # ['Rusty', 'Colt', 'Blue']

# def double(x):
#     return x * 2
# doubles = map(double,nums)
# print(list(doubles)) # [4, 8, 12, 16, 20]
 # The list comprehension way would be this:
# nums = [2,4,6,8,10]
# print(list(num*2 for num in nums)) # [4, 8, 12, 16, 20]

# def decrement_list(l):
#     return list(map(lambda x: x - 1,l))

# **filter**
# there is a lambda for each value in the iterable
# returns filter object which can be converted into other iterables
# the object contains only the values that return true to the lambda

# l = [1,2,3,4]
# evens = list(filter(lambda x: x % 2 == 0,l))
# print(evens) # [2,4]

# names = ["austin", "penny", "anthony", "angel", "billy"]
# a_names = list(filter(lambda x: x[0] == "a",names))
# print(a_names) # ['austin', 'anthony', 'angel']

# users = [
#     {"username" : "samuel", "tweets" : ["I love cake", "I love pie"]},
#     {"username" : "katie", "tweets" : ["I love my cat"]},
#     {"username" : "jeff", "tweets" : []},
#     {"username" : "bob123", "tweets" : []},
#     {"username" : "doggo_luvr", "tweets" : ["dogs are the best", "I'm hungry"]},
#     {"username" : "guitar_gal", "tweets" : []},
# ]
#
# inactive_users = list(filter(lambda x: not x["tweets"],users))
# print(inactive_users) # gives inactive users

# **COMBINING filter AND map**
# given this list of names:
# names = ["Lassie", "Colt", "Rusty"]
# # return a new list with the string "Your instructor is" + each value in the array,
# # but only if the value is less than 5 characters
#
# char_5 = list(map(lambda y: f"Your instructor is {y}", filter(lambda x: len(x) < 5, names)))
# print(char_5) # ['Your instructor is Colt']

# users = [
#     {"username" : "samuel", "tweets" : ["I love cake", "I love pie"]},
#     {"username" : "katie", "tweets" : ["I love my cat"]},
#     {"username" : "jeff", "tweets" : []},
#     {"username" : "bob123", "tweets" : []},
#     {"username" : "doggo_luvr", "tweets" : ["dogs are the best", "I'm hungry"]},
#     {"username" : "guitar_gal", "tweets" : []},
# ]
# inactive_usernames = list(map(lambda x: x["username"].upper(), filter(lambda y: not y["tweets"], users)))
# print(inactive_usernames) # ['JEFF', 'BOB123', 'GUITAR_GAL']
# # List Comprehension for above example would be:
# print([user["username"].upper() for user in users if not user["tweets"]])
# gives the same answer
# What about list comprehension?
# names = ["Lassie", "Colt", "Rusty"]
# print([f"Your instructor is {name}" for name in names if len(name) < 5])

# **EXERCISES**
# def remove_negatives(l):
#     return list(filter(lambda x: not x < 0,l))
# print(remove_negatives([-1,3,4,-99])) # [3,4]

# **ANY AND ALL**
# *all*
# return True if all elements are iterable and truthy (or if the iterable is empty)
# print(all([0,1,2,3])) # False
# print(all([char for char in "aio" if char in "aeiou"])) # True
# print(all([num for num in [4,2,10,6,8] if num % 2 == 0])) # True

# people = ["Charlie", "Casey", "Cody", "Carly", "Cristina"]
# print(all([char[0] == "C" for char in people])) # True
# people.append("Kristy")
# print(all([char[0] == "C" for char in people])) # False

# nums = [2,60,26,18]
# print(all([num for num in nums if num % 2 == 0]))

# *any*
# returns True if any element of iterable is truthy. if the iterable is empty, return False
# print(any([0,2,3])) # True
# print(any([val for val in [1,2,3] if val > 2])) # True
# print(any([val for val in [1,2,3] if val > 5])) # False

# nums = [2,60,26,18, 21]
# print(any([num for num in nums if num % 2 != 0])) # True
# print([num for num in nums if num % 2 != 0]) # 21

# people = ["Charlie", "Casey", "Cody", "Carly", "Cristina"]
# print((name[0] == "C" for name in people)) # <generator object <genexpr> at 0x1086b2900>
# returns a generator expression

# Reason to not use the brackets is size of the bytes in the code:
# import sys
# list_comp = sys.getsizeof([x * 10 for x in range(1000)])
# gen_exp = sys.getsizeof(x * 10 for x in range(1000))
#
# print("To do the same thing, it takes...") # To do the same thing, it takes...
# print(f"List Comprehension: {list_comp} bytes") # List Comprehension: 9016 bytes
# print(f"Generator Expression: {gen_exp} bytes") # Generator Expression: 112 bytes

# def is_all_strings(x):
#     return all(val == str(val) for val in x)
# print(is_all_strings(["a", "b", "c"])) # True
# print(is_all_strings([2,"a","b","c"])) # False

# **sorted**
# returns a new sorted list from the items iterable.
# Can sort tuples also, but returns a list.

# more_numbers = [6,1,8,2]
# print(sorted(more_numbers)) # [1,2,6,8]
# unlike SORT, SORTED returns the sorted items once and more_numbers still = [6,1,8,2]

# nums = [4,6,1,30,55,23]
# nums.sort()
# print(nums) # [1, 4, 6, 23, 30, 55]
# print(sorted(nums)) # [1, 4, 6, 23, 30, 55]
# print(nums) # [4, 6, 1, 30, 55, 23]

# nums = [4,6,1,30,55,23]
# print(sorted(nums, reverse=True)) # [55, 30, 23, 6, 4, 1]

# users = [
#     {"username" : "samuel", "tweets" : ["I love cake", "I love pie"]},
#     {"username" : "katie", "tweets" : ["I love my cat"]},
#     {"username" : "jeff", "tweets" : []},
#     {"username" : "bob123", "tweets" : []},
#     {"username" : "doggo_luvr", "tweets" : ["dogs are the best", "I'm hungry"]},
#     {"username" : "guitar_gal", "tweets" : []},
# ]

# print(sorted([user["username"] for user in users])) # ['bob123', 'doggo_luvr', 'guitar_gal', 'jeff', 'katie', 'samuel']
# print(sorted(users,key=lambda user: user["username"])) # [{'username': 'bob123', 'tweets': []}, {'username': 'doggo_luvr', 'tweets': ['dogs are the best', "I'm hungry"]}, {'username': 'guitar_gal', 'tweets': []}, {'username': 'jeff', 'tweets': []}, {'username': 'katie', 'tweets': ['I love my cat']}, {'username': 'samuel', 'tweets': ['I love cake', 'I love pie']}]
# if I want to sort by number of tweets:
# print(sorted(users,key=lambda user: len(user["tweets"]))) # [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'guitar_gal', 'tweets': []}, {'username': 'katie', 'tweets': ['I love my cat']}, {'username': 'samuel', 'tweets': ['I love cake', 'I love pie']}, {'username': 'doggo_luvr', 'tweets': ['dogs are the best', "I'm hungry"]}]

# **MAX AND MIN**
# return the largest item in an iterable or the largest of two or more arguments

# print(max(3,67,99)) # 99
# nums = [40,32,6,5,10]
# print(max(nums)) # 40
# print(min(nums)) # 5

# names = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]
# print(max(len(name) for name in names)) # 10, the length of the longest string
# print(max(names, key=lambda n:len(n))) # Ollivander

# EXERCISES
# def extremes(l):
#     return (min(l),max(l))
# print(extremes([1,2,3,4,5])) # (1,5)

# **REVERSED**
# returns a reverse iterator

# nums = [1,2,3,4]
# nums.reverse()
# print(nums) # [4, 3, 2, 1]
# print(reversed(nums)) # <list_reverseiterator object at 0x104b8beb0>

# for char in reversed("hello world"):
#     print(char) # prints reverse of hello world (each letter on a line)
# print([char for char in reversed("hello world")]) # ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
# def backwards(l):
#     return [char for char in reversed(l)]
# print(backwards("hello world")) # ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']

# print("hello"[::-1]) # olleh

# print("".join(list(reversed("hello")))) # olleh

# for x in reversed(range(0,10)):
#     print(x) # prints 9-0 in reverse

# **LEN**
# returns the length (number of items) of an object.
# the argument may be a sequence (string, tuple, list or range) or collection (dictionary, set)

# print(len("asdasdas")) # 8

# "hello".__len__() # 5
# this is being called when you use the len() function

# we can define our own lengths of things like a deck of cards
# ADVANCED EXAMPLE:
# class SpeciaList:
#
#     def __init__(self,data):
#         self.__data = data
#
#     def __len__(self): # JUST LOOK AT THIS LINE
#         return 50
#
# l1 = SpeciaList([1,40,30,100])
# l2 = SpeciaList([])
# print((len(l1))) # 50

# **ABS() SUM() AND ROUND()**
# *abs()*
# return the absolute value of a number. The argument may be an integer or a floating point number
# absolute value: the magnitude of a real number without regard to its sign
# just drops the negative
# print(abs(-123)) # 123
# print(abs(-123.34)) # 123.34

# *sum()*
# takes an iterable and optional start.
# returns the sum of start and the items of an iterable from left to right and returns the total
# start is 0 by default

# print(sum([1,2,3,4])) # 10
# print(sum([1,2,3],10)) # 16
# print(sum([1,2,3], -6)) # 0

# *round()*
# return number rounded to ndigits precision after the decimal point.
# if ndigits is omitted or is None, it returns the nearest integer to it input

# print(round(3.43564)) # 3
# print(round(3.43564, 3)) # 3.436
# print(round(3.54564,None)) # 4

# **EXERCISES**

# def max_magnitude(l):
#     return max(abs(num) for num in l)
#
# print(max_magnitude([300, 20, -900]))

# def sum_even_values(*args):
#     return sum(num for num in args if num % 2 == 0)
#
# print(sum_even_values(1,2,3,4,5,6)) # 12
# print(sum_even_values(4,2,1,10)) # 16
# print(sum_even_values(1)) # 0

# def sum_floats(*args):
#     return sum(num for num in args if type(num) == float)
#
# print(sum_floats(1.5, 2.4, 'awesome', [], 1)) # 3.9

# **ZIP**
# It takes 2 lists of the same length and zips them together into pairs as a tuple
# left to right. order matters
# if iterables are different lengths, it will stop at the shortest length

# first_zip = zip([1,2,3], [4,5,6])
# print(list(first_zip)) # [(1, 4), (2, 5), (3, 6)]
# print(dict(first_zip))

# nums1 = [1,2,3,4,5]
# nums2 = [6,7,8,9,10]
# print(zip(nums1,nums2)) # <zip object at 0x10ada46c0>
# print(list(zip(nums1,nums2))) # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
# print(dict(zip(nums1,nums2))) # {1: 6, 2: 7, 3: 8, 4: 9, 5: 10}

# five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
# print(list(zip(*five_by_two))) # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]
# took first item out and pulled them together and took second into antoher

# midterms = [80,91,78]
# finals = [98,89,53]
# students = ['dan', "ang", "kate"]
# final = {"dan" : 98, "ang" : 91, "kate": 78}

# final_grades = [pair for pair in zip(midterms, finals)]
# print(final_grades) # [(80, 98), (91, 89), (78, 53)]
# lets find the max:
# final_grades = [max(pair) for pair in zip(midterms, finals)]
# print(final_grades) # [98, 91, 78]
#
# print(dict(zip(students, final_grades))) # {'dan': 98, 'ang': 91, 'kate': 78}
# OR
# final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
# print(final_grades)
# OR
# final_grades = dict(
#     zip(
#         students,
#         map(
#             lambda pair: max(pair),
#              zip(midterms, finals)
#         )
#     )
# )
# print(final_grades) # {'dan': 98, 'ang': 91, 'kate': 78}

# avg_grades = dict(
#     zip(
#         students,
#         map(
#             lambda pair: sum(pair) / 2,
#              zip(midterms, finals)
#         )
#     )
# )
# print(avg_grades)

# **EXERCISES**

# def interleave(x,y):
#     return "".join("".join(val) for val in (zip(x,y)))
#
# print(interleave("hi","ha")) # hhia

# def triple_and_filter(list1):
#     return list(filter(lambda x: (x % 4 == 0), map(lambda x: x*3, list1)))
#
# print(triple_and_filter([1,2,3,4])) # 12

# def extract_full_name(list1):
#     return list(map(lambda val: f"{val['first']} {val['last']}", list1))
#
# names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
# print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']
