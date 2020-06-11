# ***OOP PART 2***
# INHERITANCE AND OBJECTIVES
# OBJECTIVES:
# - Implement inheritance, including multiple
# from random import randint
# suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
# values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#
#
# combined = [[value, suit]for suit in suits for value in values]
#
# print(combined[randint(0,52)])

# ****OOP PART 2****
# OBJECTIVES:
# - Implement inheritance, including multiple
# - Understand Method Resolution Order
# - Understand polymorphism
# - Add Special methods to classes

# **INHERITANCE**
# - A key feature of OOP is the ability to define a class which inherits from another class (a "base" or "parent" class)
# - In Python, inheritance works by passing the parent class as an argument to the definition of a child class:

# class Animal:
#     def make_sound(self, sound):
#         print(f"This animal says {sound}")
#
#     cool = True
#
#
# class Cat(Animal):
#     pass

# a = Cat()
# print(a.make_sound("MEOW")) # This animal says MEOW
#
# a = Animal()
# print(a.make_sound("CHIRP")) # This animal says CHIRP
#
# blue = Cat()
# print(blue.make_sound("MEOW")) # This animal says MEOW
# # THIS HAPPENS BECAUSE ANIMAL AND CAT ARE INHERENTLY LINKED

# print(isinstance(blue, Animal)) # True for both Animal and Cat
# print(isinstance(blue, object)) # True

# ***ALL ABOUT PROPERTIES***
# class Human:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         if age >= 0:
#             self._age = age
#         else:
#             raise ValueError("Age can't be negative!")
#
#     # def get_age(self):
#     #     return self._age
#     #
#     # def set_age(self, new_age):
#     #     if new_age >= 0:
#     #         self._age = new_age
#     #     else:
#     #         self._age = 0
#     @property
#     def age(self):
#         return self._age    # THIS @PROPERTY ENCODES ALL THE DEF ABOVE
#
#     @age.setter # SETTER
#     def age(self, value):
#         if value >= 0:
#              self._age = value
#         else:
#              raise ValueError("Age can't be negative!")
#
#     @property # GETTER
#     def full_name(self):
#         return f"{self.first} {self.last}"
#
#     # DON'T DO THIS. IT WILL RESET THE PROPERTY THAT HAS 2 ATTRIBUTES. JUST SHOWING IT WORKS.
#     @full_name.setter
#     def full_name(self):
#         self.first, self.last = name.split(" ")
#
# jane = Human("Jane", "Goodall", 100)
# jane.age = -100 # YOU COULD MESS IT UP BY DOING THIS

# print(jane.get_age()) # 0
# jane.set_age(45)
# print(jane.get_age()) # 45
# print(jane.age)
# jane.age = 20
# print(jane.age)
# print(jane.full_name)

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def __repr__(self):
#         return f"{self.name} is a {self.species}"
#
#     def make_sound(self, sound):
#         print(f"This animal says {sound}")
#
#
# class Cat(Animal):
#     def __init__(self, name, breed, favorite_toy):
#         super().__init__(name, species="Cat")
#         # Animal.__init__(self, name, species) super() DOES THE SAME THING.
#         self.breed = breed
#         self.favorite_toy = favorite_toy
#
#     def play(self):
#         return f"{self.name} plays with {self.favorite_toy}"
#
# blue = Cat("Blue", "Scottish Fold", "String")
# print(blue)
# print(blue.play())

# ***INHERITANCE EXAMPLE: USER AND MODERATOR***
# EXAMPLE OF REDDIT USERS AND MODERATORS
# class User:
#     active_users = 0
#
#     @classmethod
#     def display_active_users(cls):
#         return f"There are currently {cls.active_users} active users"
#     @classmethod # THIS IS TAKING A .CSV, SPLITTING BY , AND ASSIGNING IT AS A USER USING CLS
#     def from_string(cls, data_string):
#         first,last,age = data_string.split(",")
#         return cls(first,last,int(age))
#
#     def __init__(self, first, last, age):
#         self.first = first     # you will initialize the date to go into the users
#         self.last = last       # THESE ARE INSTANCE ATTRIBUTES
#         self.age = age
#         User.active_users += 1
#
#     def logout(self):
#         User.active_users -= 1
#         return f"{self.first} has logged out"
#
#     def full_name(self):                      # THESE ARE INSTANCE METHODS
#         return f"{self.first} {self.last}"
#
#     def initials(self):
#         return f"{self.first[0:1:]}.{self.last[0:1:]}."
#
#     def likes(self,thing):
#         return f"{self.first} likes {thing}."
#
#     def is_senior(self):
#         return self.age >= 65
#         # OR
#         # if self.age >= 65:
#         #     return f"{self.first} {self.last} is a senior."
#         # else:
#         #     return f"{self.first} {self.last} is not a senior."
#
#     def birthday(self):
#         self.age += 1
#         return f"Happy {self.age}th Birthday, {self.first}"
#
# class Moderator(User):
#     total_mods = 0
#     def __init__(self, first, last, age, community): # Example of Reddit moderators
#         super().__init__(first, last, age)
#         self.community = community
#         Moderator.total_mods += 1 # Lets you know how many moderators are online
#
#     @classmethod
#     def display_active_mods(cls):
#         return f"There are currently {cls.total_mods} active moderators"
#
#     def remove_post(self):
#         return f"{self.full_name()} removed a post from the {self.community}"
#
# print(User.display_active_users()) # There are currently 0 active users
# u1 = User("Tom", "Garcia", 35)
# print(User.display_active_users()) # There are currently 1 active users
# jasmine = Moderator("Jasmine", "O'Conner", 61, "piano")
# print(User.display_active_users()) # There are currently 2 active users
# print(Moderator.display_active_mods()) # There are currently 1 active moderators

# ***EXERCISES***

# class Character():
#     def __init__(self, name, hp, level):
#         self.name = name
#         self.hp = hp
#         self.level = level
#
# class NPC(Character):
#     def __init__(self, name, hp, level):
#         super().__init__(name, hp, level)
#
#
#     def speak(self):
#         return "I heard there were monsters running around last night"
#
# villager = NPC("Bob", 100, 12)
# print(villager.name)
# print(villager.speak())

# ***THE CRAZY WORLD OF MULTIPLE INHERITANCE***

# class Aquatic:
#     def __init__(self, name):
#         print("AQUATIC INIT!")
#         self.name = name
#
#     def swim(self):
#         return f"{self.name} is swimming"
#
#     def greet(self):
#         return f"I am {self.name} of the sea"
#
# class Ambulatory:
#     def __init__(self, name):
#         print("AMBULATORY INIT!")
#         self.name = name
#
#     def walk(self):
#         return f"{self.name} is walking"
#
#     def greet(self):
#         return f"I am {self.name} of the land"
#
# class Penguin(Ambulatory, Aquatic):
#     def __init__(self, name):
#         print("PENGUIN INIT!")
#         super().__init__(name=name)
#
# # jaws = Aquatic("Jaws")
# # lassie = Ambulatory("Lassie")
# # captain_cook = Penguin("Captain Cook")
#
# # print(captain_cook.swim()) # Captain Cook is swimming
# # print(captain_cook.walk()) # Captain Cook is walking
# # print(captain_cook.greet()) # I am Captain Cook of the land
# # PYTHON SEES CAPTAIN COOK AS PENGUIN, AMBULATORY AND AQUATIC
#
# # AFTER ADDING THE PRINT "BLANK INIT"
# captain_cook = Penguin("Captain Cook") # PENGUIN INIT!  AND AMBULATORY INIT!

# **WTF IS METHOD RESOLUTION ORDER**
# Penguin inherits from both Aquatic and Ambulatory, therefore instances of Penguin can call both
# the walk and swim methods.
# What about the greet method for our instance of Penguin?
# Is it calling the Aquatic.greet() instead of Ambulatory.greet()?
# METHOD RESOLUTION ORDER (MRO):
# - Whenever you create a class, Python sets a Method Resolution Order, or MRO, for that class,
#   which is the order in which Python will look for methods on instances of that class.
# YOU CAN PROGRAMMATICALLY REFERENCE THE MRO THREE WAYS:
# 1- __mro__ attribute on the class
# 2- Use the mro() method on the class
# 3- Use the built-in help(cls) method **BEST WAY TO READ**

# **EXERCISES**
#
# class Mother:
#     def __init__(self):
#         self.eye_color = "brown"
#         self.hair_color = "dark brown"
#         self.hair_type = "curly"
#
# class Father:
#     def __init__(self):
#         self.eye_color = "blue"
#         self.hair_color = "blonde"
#         self.hair_type = "straight"
#
# class Child(Mother, Father):
#     pass

# ***POLYMORPHISM INTRODUCTION***
# - A key principle in OOP is the idea of polymorphism - an object can take on may (poly) forms (morph).
# - While a formal definition of polymorphism is more difficult, here are two important practical
#   applications:
# 1 - The same class method works in a similar way for different classes:
# Cat.speak()
# Dog.speak()
# Human.speak()
# 2 - The same operation works for different kinds of objects:
# sample_list = [1,2,3]
# sample_tuple = (1,2,3)
# sample_string = "akfdjlsjf"
# len(sample_list)
# len(sample_tuple)
# len (sample_string)

# **POLYMORPHISM & INHERITANCE**
# 1 - The same method in a class works in a similar way for different classes
#  - A common implementation of this is to have a method in a base (or parent)
#    class that is overridden by a subclass. This is called METHOD OVERRIDING
# - Each subclass will have a different implementation of the method
# class Animal():
#     def speak(self):
#         raise NotImplementedError("Subclass needs to implement before this method")
# class Dog(Animal):
#     def speak(self):
#         return "WOOF"
# class Cat(Animal):
#     def speak(self):
#         return "MEOW"
# d = Animal.speak("Roar")
# print(d) # NotImplementedError: Subclass needs to implement before this method

# 2 - (Polymorphism) The same operation works for different kinds of objects
# - How does the following work in Python?
# 8 + 2 # 10
# "8" + "2" # 82
# - The answer is "special methods"!
# - Python classes have special (also "magic") methods, that are dunders (i.e. double underscore named)
# - These are methods with special names that give instructions to Python for how to deal with objects

# **SPECIAL __MAGIC__ METHODS**
# SPECIAL METHODS EXAMPLE:
# print(8 + 2) # 10
# The + operator is shorthand for a special method called __add__() that gets called on the first operand
# If the first (left) operand is an instance of int, __add__() does the mathematical ADDITION.
# If it's a STRING, it does string CONCATENATION.

# *SPECIAL METHODS APPLIED*
# - Therefore, you can declare special methods on your own classes to mimic the behavior of
#   built in objects, like so using __len__().
# class Human:
#     def __init__(self, height):
#         self.height = height
#
#     def __len__(self):
#         return self.height
# colt = Human(60)
# print(len(colt)) # 60

# *STRING REPRESENTATION*
# - The most common use-case for special methods is to make classes "look pretty" in strings.
# - By default, our classes look ugly
# class Human:
#     pass
#
# colt = Human()
# print(colt) # <__main__.Human object at 0x10bbd9d30>
# WE CAN USE THE __REPR__ METHOD TO PROVIDE ANOTHER STRING REPRESENTATION:
# class Human:
#     def __init__(self, name="somebody"):
#         self.name = name
#     def __repr__(self):
#         return self.name
#
# dude = Human()
# print(dude) # somebody

# from copy import copy
# class Human:
#     def __init__(self, first, last, age, gender):
#         self.first = first
#         self.last = last
#         self.age = age
#         self.gender = gender

#     def __repr__(self):
#         return f"Human named {self.first} {self.last} aged {self.age}"

#     def __len__(self):
#         return self.age

#     def __add__(self, other):
#         if isinstance(other, Human):
#             if self.gender == "male":
#                 last = self.last
#             else:
#                 last = other.last
#             return Human(first="Newborn", last=last, gender="unknown", age=0)
#         return "You can't add that"

#     def __mul__(self, other):
#         if isinstance(other, int):
#             return [copy(self) for i in range (other)]
#         return "CAN'T MULTIPLY"

# j = Human("Jenny", "Larson", 47, "female")
# k = Human("Kevin", "Jones", 49, "male")
# print(j)
# print(len(j))
# print(j + k) # Human named Newborn Jones *I ADDED THE GENDER FOR LAST PART
# print(j * 2) # [Human named Jenny Larson aged 47, Human named Jenny Larson aged 47]
# triplets = j * 3
# triplets[1].first = "Jessica"
# print(triplets) # [Human named Jessica Larson aged 47, Human named Jessica Larson aged 47, Human named Jessica Larson aged 47]
# REASON IT DIDN'T JUST NAME THE MIDDLE KID "JESSICA" IS BECAUSE THEY ARE IDENTICAL AND LINKED.
# WE ADDED "FROM COPY IMPORT COPY" AND PUT COPY(SELF) IN THE MUL CODE:
# print(triplets) # [Human named Jenny Larson aged 47, Human named Jessica Larson aged 47, Human named Jenny Larson aged 47]

# **MAKING A GRUMPY DICTIONARY**
# class GrumpyDict(dict):
#     def __repr__(self):
#         print("NONE OF YOUR BUSINESS") # returns: NONE OF YOUR BUSINESS
#         return super().__repr__() # returns: {'first': 'Tom', 'animal': 'cat'}
#
#     def __missing__(self, key):
#         print(f"YOU WANT {key}? WELL IT AIN'T HERE") # returns: YOU WANT city? WELL IT AIN'T HERE
#
#     def __setitem__(self, key, value):
#         print("YOU WANT TO CHANGE THE DICTIOARY?")
#         print("OK FINE...")
#         super().__setitem__(key, value) # {'first': 'Tom', 'animal': 'cat', 'city': 'Tokyo'}
#
# data = GrumpyDict({"first" : "Tom", "animal" : "cat"})
# print(data) # NONE OF YOUR BUSINESS {'first': 'Tom', 'animal': 'cat'}
# print(data["city"]) # YOU WANT city? WELL IT AIN'T HERE
# data["city"] = "Tokyo"
# print(data) # {'first': 'Tom', 'animal': 'cat', 'city': 'Tokyo'}

# **EXERCISES**
# class Train:
#     def __init__(self, num_cars):
#         self.num_cars = num_cars
#
#     def __repr__(self):
#         return f"{self.num_cars} car train"
#
#     def __len__(self):
#         return self.num_cars
# a_train = Train(4)
# print(a_train)