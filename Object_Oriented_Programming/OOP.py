# ***OBJECT ORIENTED PROGRAMMING**

# OBJECTIVES:
# - Define what Object Oriented Programming is
# - Understand encapsulation and abstraction
# - Create classes and instances and attach methods and properties to each

# **DEFINING CLASSES AND OBJECTS**
# WHAT IS OOP?
# - Not unique to Python
# - Object Oriented Programming is a method of programming that attempts to
#   model some process or thing in the world as a CLASS or OBJECT.
# - CLASS- a blueprint for objects. Classes can contain methods (functions)
#   and attributes (similar to keys in a dict).
# - INSTANCE- objects that are constructed from a class blueprint that
#   contain their class's methods and properties.

# **WHY OOP?**
# with OOP, the goal is to encapsulate your code into LOGICAL, HEIRARCHICAL GROUPINGS USING CLASSES so
# that you can reason about your code at a higher level.

# *EXAMPLE*
# Say we want to model a game of POKER in our program.
# We could have the following entities:
# - Game
# - Player
# - Card
# - Deck
# - Hand
# - Chip
# - Bet

# Card Deck Possible Implementation:
#           Deck {class}
# _cards          {private list attribute} # _ in front means private
# _max_cards      {private int attribute}  # _ in front means private
# shuffle         {public method}
# deal_card       {public method}
# deal_hand       {public method}
# count           {public method}

# *ENCAPSULATION*
# - the grouping of public and private attributes and methods into a programmatic class, making
#   abstractions possible.
# *EXAMPLE:
# -designing the Deck class, I make CARDS a private attribute (a list)
# -I decide that the length of the cards should be accessed via a public method called count()--ie. Deck.count()

# *ABSTRACTION*
# - exposing only "relevant" data in a class interface, hiding private attributes and methods
#   (aka the "inner workings") from users

# ***CREATING CLASSES AND INSTANCES***
# DEFINING THE SIMPLEST POSSIBLE CLASS

# class User: # use camelcase
#     pass # means I'm done, move on
# user1 = User()
# user2 = User()
# print(user1) # <__main__.User object at 0x10f8b2d30>
# print(user2) # <__main__.User object at 0x10e27a820> # THEY ARE DIFFERENT, EVEN THOUGH THEY ARE IN THE SAME CLASS
# print(type(user1)) # <class '__main__.User'>

# **EXERCISES**
# class Vehicle:
#     pass
# car = Vehicle()
# boat = Vehicle()

# **THE __init__ METHOD**
# Classes in Python have a special __init__ method, which gets called every time
# you create an instance of the class (instantiate).
# SELF must always be the first parameter to __init__ and any methods and properties on class instances
# class Vehicle:
#   def __init__(self, make, model, year):
#       self.make = make
#       self.model = model
#       self.year = year
# class User:
#     def __init__(self, first, last, age):
#         self.first = first     # you will initialize the date to go into the users
#         self.last = last
#         self.age = age
#
#
# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(user1.first, user1.last) # Joe Smith
# print(user2.first, user2.last) # Blanca Lopez

# **EXERCISES**

# class Comment:
#     def __init__(self, username, text, likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes
# c = Comment("davey123", "lol you're so silly", 3)
# print(c.username)
# print(c.text)
# print(c.likes)

# **UNDERSCORES: DUNDER METHODS, NAME MANGLINIG, AND MORE!**

# _name    # This tells developers that this is private. It's not really private, just tells people info.
# __name   # Mangles the message. Don't use.
# __name__ # DUNDER - special things that Python looks for

# class Person:
#     def __init__(self):
#         self.name = "Tony"
#         self._secret = "hi!"
#         self.__message = "I like turtles" # don't do this.
#
# p = Person()
#
# print(p.name)
# print(p._secret)

# **ADDING INSTANCE METHODS**
# INSTANCE ATTRIBUTES AND METHODS:
#
# class User:
#     def __init__(self, first, last, age):
#         self.first = first     # you will initialize the date to go into the users
#         self.last = last       # THESE ARE INSTANCE ATTRIBUTES
#         self.age = age
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
#         if self.age >= 65:
#             return f"{self.first} {self.last} is a senior."
#         else:
#             return f"{self.first} {self.last} is not a senior."
#        #OR
#        #return self.age >= 65
#     def birthday(self):
#         self.age += 1
#         return f"Happy {self.age}th Birthday, {self.first}"
#
# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# # print(user1.first, user1.last) # Joe Smith
# # print(user2.first, user2.last) # Blanca Lopez
# print(user2.full_name()) # Blanca Lopez
# print(user1.initials()) # J.S.
# print(user1.likes("candy")) # Joe likes candy
# print(user1.is_senior()) # Joe Smith is a senior
# print(user2.is_senior()) # Blanca Lopez is not a senior
# print(user1.birthday()) #  Happy 69th Birthday, Joe

# **EXERCISE**
# class BankAccount:
#     def __init__(acct,owner,balance=0):
#         acct.owner = owner
#         acct.balance = balance
#
#     def deposit(acct,deposit):
#         acct.balance = acct.balance + deposit
#         return f"You deposited {deposit} and your new balance is now {acct.balance}"
#
#     def withdraw(acct,withdraw):
#         acct.balance = acct.balance - withdraw
#         return f"You withdrew {withdraw} and your new balance is now {acct.balance}"
#
# owner1 = BankAccount("Charlie", 12)
# print(owner1.deposit(10)) # You deposited 10 and your new balance is now 22
# print(owner1.withdraw(3)) # You withdrew 3 and your new balance is now 19

# **INTRODUCING CLASS ATTRIBUTES**
# INSTANCE ATTRIBUTES AND METHODS:
# CLASS ATTRIBUTES:
# - We can also define attributes directly on a class that are shared by all
#   instances of a class and the class itself.
# class User:
#
#     active_users = 0
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
#
#     def birthday(self):
#         self.age += 1
#         return f"Happy {self.age}th Birthday, {self.first}"
#
# # user1 = User("Joe", "Smith", 68)
# # user2 = User("Blanca", "Lopez", 41)
#
# print(User.active_users) # 0
# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.active_users) # 2
# print(user2.logout()) # Blanca has logged out
# print(User.active_users) # 1

# class Pet:
#     allowed = ['cat', 'dog', 'fish', 'rat'] # ****
#
#     def __init__(self, name, species):
#         if species.casefold() not in Pet.allowed:
#             raise ValueError(f"You can't have a {species} pet")
#         self.name = name
#         self.species = species
#
#     def set_species(self, species):
#         if species not in Pet.allowed:
#             raise ValueError(f"You can't have a {species} pet")
#         self.species = species
#
# cat = Pet("Blue", "cat")
# dog = Pet("Wyatt", "dog")
#
# # Pet("tony", "tiger")
# p = Pet("Jack", "Dog")
# print(p.species)
# When you use allowed in the code, it is referencing the class attribute **** the whole time.

# ***EXERCISES***
# class Chicken:
#     total_eggs = 0
#     def __init__(self, species, name, eggs=0):
#         self.species = species
#         self.name = name
#         self.eggs = eggs
#
#     def lay_egg(self):
#         self.eggs += 1
#         Chicken.total_eggs += 1
#
# c1 = Chicken("Alice", "Partridge Silkie")
# c2 = Chicken("Amelia", "Speckled Sussex")
# print(Chicken.total_eggs) # 0
# print(c1.lay_egg())
# print(Chicken.total_eggs) # 1

# ***CLASS METHODS***
# Not all that commonly used
# - methods (with the @classmethod decorator) that are not concerned with instances, but the class itself

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
#
#     def birthday(self):
#         self.age += 1
#         return f"Happy {self.age}th Birthday, {self.first}"
#
# # user1 = User("Joe", "Smith", 68)
# # user2 = User("Blanca", "Lopez", 41)
#
# # print(User.active_users) # 0
# # user1 = User("Joe", "Smith", 68)
# # user2 = User("Blanca", "Lopez", 41)
# # print(User.active_users) # 2
# # print(user2.logout()) # Blanca has logged out
# # print(User.active_users) # 1
# # print(User.display_active_users()) # 1
#
# # lets say we are passing .csv data in:
# u = User.from_string("tom,jones,89")
# # "tom,jones,89"
# # "sue,prichet,12"
# print(u.first) # tom
# print(u.full_name()) # tom jones

# ***THE __repr__ METHOD***
# - The ___repr__ method is one of several ways to provide a nicer string representation.
# - There are also several other dunders to return classes in string formats
#   (notably __str__ and __format__), and choosing one is A BIT COMPLICATED!

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
#     def __repr__(self):
#         return f"{self.first} is {self.age}"
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
#
#     def birthday(self):
#         self.age += 1
#         return f"Happy {self.age}th Birthday, {self.first}"

# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)

# print(User.active_users) # 0
# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.active_users) # 2
# print(user2.logout()) # Blanca has logged out
# print(User.active_users) # 1
# print(User.display_active_users()) # 1

# lets say we are passing .csv data in:
# u = User.from_string("tom,jones,89")
# "tom,jones,89"
# "sue,prichet,12"
# print(u.first) # tom
# print(u.full_name()) # tom jones

# print(u) #<__main__.User object at 0x1051d5fa0>
# ADDED __repr__ AS A INSTANCE METHOD AND NOW WE GET:
# print(u) # tom is 89

