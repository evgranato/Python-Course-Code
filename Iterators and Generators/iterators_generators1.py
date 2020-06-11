# ***ITERATORS AND GENERATORS***
# OBJECTIVES:
# - Define ITERATOR and ITERABLE
# - Understand the iter() and next() methods
# - Build our own for loop
# - Define what generators are and how they can be used
# - Compare generator functions and generator expressions
# - Use generators to pause execution of expensive functions

# **ITERATORS? ITERABLES?
# ITERATOR: an object that can be iterated upon. An object which returns data, one element
# at a time when next() is called on it.
# ITERABLE: An object which will return an iterator when iter() is called on it.

# EXAMPLE:
# "HELLO" is an iterable, but is not an iterator.
# iter("HELLO") returns an iterator.

# name = "Oprah"
#next(name) # TypeError: 'str' object is not an iterator
# it = iter(name)
# print(it) # <str_iterator object at 0x108030ee0>
# for char in "Oprah"
# print(next(it)) # O
# print(next(it)) # p
# print(next(it)) # r
# print(next(it)) # a
# print(next(it)) # h
# print(next(it)) # StopIteration

# *NEXT*
# - When next() is called on an iterator, the iterator returns the next item.
#   It keeps doing so until it raises a StopIteration error.

# nums = [1,2,3,4,5]
# next(nums) # TypeError: 'list' object is not an iterator
# it = iter(nums)
# print(it) # <list_iterator object at 0x10dee5f40>
# print(next(it))

# **WRITING OUR OWN VERSION OF FOR LOOPS**
# custom For Loop just to understand how things work in the background
#for num in [1,2,3]
#for char in "hi there"
# for is calling the iter()
# in is calling the next()
# def my_for(iterable, func):
#     iterator = iter(iterable)
#     while True:
#         try:
#             thing = next(iterator)
#         except StopIteration:
#             print("END OF ITERATOR!")
#             break
#         else:
#             func(thing)
# def square(x):
#     print(x*x)
# # print(my_for("HELLO"))
# # H
# # E
# # L
# # L
# # O
# # END OF ITERATOR!
# my_for([1,2,3,4], print) # returns the printed 1,2,3,4
# my_for([1,2,3,4,5], square) # returns the squared list

# **WRITING A CUSTOM ITERATOR**
# class Counter:
#     def __init__(self, low, high):
#         self.current = low
#         self.high = high
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.high:
#             num = self.current
#             self.current += 1
#             return num
#         raise StopIteration
#
# for n in Counter(0,55):
#         print(n)
# prints 0 - 54
# THIS WHOLE CODE JUST REWRITES RANGE()

# **MAKING OUR DECK CLASS ITERABLE**

# from random import shuffle
#
# class Card:
#     def __init__(self, value, suit):
#         self.suit = suit
#         self.value = value
#
#     def __repr__(self):
#         return f"{self.value} of {self.suit}"
# #
# class Deck:
#     def __init__(self):
#         suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
#         values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#         self.cards =[Card(value, suit) for suit in suits for value in values]
#
#     def __repr__(self):
#         return f"Deck of {self.count()} cards"
#
#     def __iter__(self):
#         return iter(self.cards)
#
#     def count(self):
#         return len(self.cards)
#
#     def _deal(self, num):
#         count = self.count()
#         actual = min([count,num])
#         if count == 0:
#             raise ValueError("All the cards have been dealt")
#         cards = self.cards[-actual:]
#         self.cards = self.cards[:-actual] # We do this to make sure we are removing them from the deck.
#         return cards
#
#     def deal_card(self):
#         return self._deal(1)[0]
#
#     def deal_hand(self, hand_size):
#         return self._deal(hand_size)
#
#     def shuffle(self):
#         if self.count() < 52:
#             raise ValueError("Only full decks can be shuffled")
#         return shuffle(self.cards)
#
# my_deck = Deck()
# my_deck.shuffle()
#
# for card in my_deck:
#     print(card)

# **GENERATORS**
# - Generators are iterators
# - Generators can be created with generator functions
# - Generator functions use the yield keyword
# - Generators can be created with generator expressions
# - Generator Functions:
#       - Use Yield
#       - Can yield multiple times
#       - When invoked, returns a generator

# *OUR FIRST GENERATOR*
# def count_up_to(max):
#     count = 1
#     while count <= max:
#         yield count
#         count += 1
#
# counter = count_up_to(5)
# # print(counter) # <generator object count_up_to at 0x10a62af90>
# print(next(counter)) # 1
# print(next(counter)) # 2
# print(next(counter)) # 3
# print(next(counter)) # 4
# print(next(counter)) # 5
# print(next(counter)) # StopIteration
# THE ABOVE GENERATOR HANDLES ALL THE CLASS __INIT__ __REPR__ AND __ITER__ FROM ABOVE CODE

# *EXERCISES*
# def week():
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     for d in days:
#         yield d
#
#
# days = week()
# print(next(days)) # printed each day until end of list

# def yes_or_no():
#     answer = "yes"
#     while True:
#         yield answer
#         answer = "no" if answer == "yes" else "yes"
#
# gen = yes_or_no()
# print(next(gen))
# print(next(gen))

# **WRITING A BEAT MAKING GENERATOR**
# UNCOMMON INFINATE GENERATOR
# lets say I'm a DJ and want to create a code that makes beats:
# def current_beat():
#     max = 100
#     nums = (1,2,3,4)
#     i = 0
#     result = []
#     while len(result) < max:
#         if i >= len(nums): i = 0
#         result.append(nums[i])
#         i += 1
#     return result
# print(current_beat()) # [1,2,3,4,1,2,3,4,1,2,3,4.....and on] BUT THIS ISN'T WHAT I WANT!!!
# def play_kick_drum()
#     if current_beat() == 1
#         play_sound()
# def current_beat():
#     nums = (1,2,3,4)
#     i = 0
#     while True:
#         if i >= len(nums): i = 0
#         yield nums[i]
#         i += 1
# beat = current_beat()
# print(next(beat)) # 1
# print(next(beat)) # 2
# THIS GIVES ONE BEAT AT AT TIME, FOREVER
# THIS ALSO GENERATES WAAAY LESS MEMORY USE

# **EXERCISES**
# def make_song(count, beverage):
#     max = 99
#     for num in range(count, -1, -1): # Function syntax and arguments: range(start, stop, step)
#         if num > 1 and num < max:
#             yield f"{num} bottles of {beverage} on the wall"
#         elif num == 1:
#             yield f"Only one bottle of {beverage} left!"
#         else:
#             yield f"No more {beverage}"
# kombucha_song = make_song(5, "kombucha")
#
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(kombucha_song))
# # 5 bottles of kombucha on the wall
# # 4 bottles of kombucha on the wall
# # 3 bottles of kombucha on the wall
# # 2 bottles of kombucha on the wall
# # Only one bottle of kombucha left!
# # No more kombucha

# **TESTING MEMORY USAGE WITH GENERATORS**
# def fib_list(max): # 600+mb
#     nums = []
#     a, b = 0, 1
#     while len(nums) < max:
#         nums.append(b)
#         a, b = b, a + b
#     return nums
#
# def fib_gen(max): # 6.7mb
#     x = 0
#     y = 1
#     count = 0
#     while count < max:
#         x, y = y, x + y
#         yield x
#         count += 1
#
# for n in fib_gen(100):
#     print(n)

# **EXERCISES**
# def get_multiples(num, count):
#     count_val = 0
#     default_multiples = [1,2,3,4,5,6,7,8,9,10]
#     for val in default_multiples:
#         val_count = val * num
#         if count_val < count:
#             yield val_count
#             count_val += 1
#
# # def get_multiples(num=1, count=10):
# #     next_num = num
# #     while count > 0:
# #         yield next_num
# #         count -= 1
# #         next_num += num
#
# evens = get_multiples(2,3)
# print(next(evens)) # 2
# print(next(evens))
# print(next(evens))
# print(next(evens))

# def get_unlimited_multiples(num=1):
#     next_num = num
#     while True:
#         yield next_num
#         next_num += num
#
# ones = get_unlimited_multiples(7)
# print(next(ones))
# print(next(ones))
# print(next(ones))

# **GENERATOR EXPRESSIONS**
# - You can create generators from GENERATOR EXPRESSIONS
# - Generator expressions look a lot like list comprehensions
# - Generator expressions use () instead of []

# def nums():
#     for num in range(1,10):
#         yield num
#
# g = nums()
# print(next(g))
# print(next(g))
# # print(next(g))
# g = (num for num in range(1,10))
# print(g)
# print(next(g))
# # If we did it with [], it would be a list, not a generator object
# g2 = [num for num in range(1,10)]
# print(g2) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# import time
# gen_start_time = time.time()
# print(sum(n for n in range(10000000)))
# gen_stop = time.time() - gen_start_time
#
# list_start_time = time.time()
# print(sum([n for n in range(10000000)]))
# list_stop = time.time() - list_start_time
#
# print(f"sum(n for n in range (10000000)) took: {gen_stop}") # sum(n for n in range (10000000)) took: 0.7027010917663574
# print(f"sum(n for n in range (10000000)) took: {list_stop}") # sum(n for n in range (10000000)) took: 1.1403977870941162