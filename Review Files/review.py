# miles = input("How many miles did you run?  ")
# kilo = round((float(miles) * 1.609340), 2)
# print(f"Your {miles} mile run was {kilo} kilometers!")

# from random import choice
# from pyfiglet import figlet_format
# from termcolor import colored
#
# def game_setup():
#     ascii_art = figlet_format("Rock..\nPaper..\nScissors")
#     colored_ascii = colored(ascii_art, color="blue")
#     print(colored_ascii)
#     player = input("Enter Your Choice...").lower()
#     return player
#
# def game_play(player,computer):
#     if player == "scissors" and computer == "rock":
#         print(f"Computer plays {computer}, you lose.")
#     elif player == "rock" and computer == "paper":
#         print(f"Computer plays {computer}, you lose.")
#     elif player == "paper" and computer == "scissors":
#         print(f"Computer plays {computer}, you lose.")
#     elif player == "scissors" and computer == "paper":
#         print(f"Computer plays {computer}, you win.")
#     elif player == "rock" and computer == "scissors":
#         print(f"Computer plays {computer}, you win.")
#     elif player == "paper" and computer == "rock":
#         print(f"Computer plays {computer}, you win.")
#     else:
#         print(f"Computer plays {computer}, it's a draw.")
#
# # game_setup()
#
# while True:
#     computer = choice(["rock", "paper", "scissors"])
#     game_play(game_setup(), computer)
#     play_again = input("Would you like to play again? (y or n)...").lower()
#     if play_again == 'y':
#         computer = choice(["rock", "paper", "scissors"])
#     else:
#         print("Thanks for playing!")
#         break

# for num in range(1,8):
#     print(num)
# i = 0
# while i <= 7:
#     print(i)
#     i += 1

# for char in "hello":
#     count = 1
#     uppers = ''
#     while count < len(char):
#         uppers += str(char.upper())
#         count += 1
#     print(uppers)

# times = int(input("How many times do I have to tell you?  "))
#
# for time in range(times):
#     print("CLEAN UP YOUR ROOM")

# for num in range(1,21):
#     if num == 4 or num == 13:
#         print(f"{num} is unlucky")
#     elif num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")

# msg = input("What's the secret password?").lower()
# while msg != 'bananas':
#     print("WRONG!!")
#     msg = input("What's the secret password?").lower()
# print("CORRECT!")
# i = 1
# while i <= 100:
#     for num in range(1,11):
#         print("\U0001f600" * num)
#         i += 1

# for num in range(1,11):
#     count = 1
#     smileys = ""
#     while count < num:
#         smileys += "\U0001f600"
#         count += 1
#     print(smileys)
# i = 1
# j = 10
# while i <= 20:
#     print(" " * j + "\U0001f600" * i)
#     i += 2
#     j -= 1

# from random import randint
#
# num = randint(1,10)
#
# while True:
#     guess = int(input("Guess a number between 1 and 10..."))
#     if guess < num:
#         print("Higher...")
#     elif guess > num:
#         print("Lower...")
#     else:
#         print("You guessed it!")
#         play_again = input("Do you want to play again? (y or n)...").lower()
#         if play_again == 'y':
#             num = randint(1, 10)
#             guess = None
#         else:
#             print("Thank you for playing!")
#             break

# TWO LIST DICTIONARY
# def two_list_dictionary(list1, list2):
    # first list keys, second values
    # if len(list1) > len(list2):
    #     length = len(list1) - len(list2)
    #     print(length)
    #     print(list2)
    #     return {x:y for x in list1 for y in list2}
    # else:
    #     return {x: y for x in list1 for y in list2}
    # collection = {}
    # for x, y in enumerate(list1):
    #     if x < len(list2):
    #         collection[list1[x]] = list2[x]
    #     else:
    #         collection[list1[x]] = None
    # return collection

# print(two_list_dictionary(['a', 'b', 'c', 'd'], [1,2,3]))

# def range_in_list(list, start=0, end=None):
#     popped = list[start:end + 1]
#     if popped:
#         return sum(popped)
#     else:
#         return 0
#
# print(range_in_list([1,2,3,4], 0, 2))

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# result = ''
# for s in sounds:
#     result += s.upper()
# print(result)
# char = 0
# result = ''.join(sounds).upper()
# while char < len(sounds):
#     result += sounds[char].upper()
#     char += 1
# print(result)

# list = [1,2,3,4]
# list.extend(["purple", "Jake", 1, True])
# print(len(list))

# instructors = []
# instructors.extend(["Colt", "Lisa", "Blue"])
# print(instructors)
# instructors.sort()

# numbers = [1,2,3,4,5]
# numbers2 = [num*200 for num in numbers]
# print(numbers2)

# name = 'evan'
# upper = [char.upper() for char in name]
# print(upper)

# vars = [4, -1, "e", 0]
# bools_list = [bool(val) for val in vars]
# print(bools_list)

# with_vowels = "This is so much fun!"
# without_vowels = ''.join(char for char in with_vowels if char not in 'aeiou')
# print(without_vowels)
# names = ["Elie", "Tim", "Matt"]
# answer = [name[0] for name in names]
# print(answer)
# nums = [1,2,3,4,5,6]
# answer2 = [num for num in nums if num % 2 == 0]
# print(answer2)

# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# answer = [x for x in list1 if x in list2]
# print(answer)

# names = ["Elie", "Tim", "Matt"]
# answer2 = [char[::-1].lower() for char in names]
# print(answer2)

# coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 32.572]]
# [[print(val) for val in l] for l in coords]
#
# print([["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)])
#
# print([["*" for num in range(1,4)] for val in range(1,4)])

# answer = [[num for num in range(0,10)] for val in range(1,11)]
# print(answer)
#
# instructor = {"first": "Colt",
#               "last": "Steele",
#               "age": 25
#               }
# print(instructor["last"])

# user_info = {"name": "testington",
#              "date of hire": "April 10, 2020",
#              "age": 30
#              }

# artist = {
#     "first": "Neil",
#     "last": "Young"
# }
#
# full_name = artist["first"] + ' ' + artist["last"]
# print(full_name)
# instructor = {"first": "Colt",
#               "last": "Steele",
#               "age": 25
#               }
#
# for x, y in instructor.items():
#     print(x,y)

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
#
# total_donations = sum(donation for donation in donations.values())
# print(total_donations)

# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!
#
# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }
# print(food)
# if food in bakery_stock:
#     print(f"{bakery_stock.get(food)} left")
# else:
#     print("We don't make that.")

# food = bakery_stock.pop("almond croissant")

# playlist = {
#     "Title": "Patagonia Bus",
#     "Author": "Evan",
#     "Songs":
#         [{"Song": "Turn it off", "Artist": ["Culture Abuse"], "Album": "Tinker", "Order": 1, "Duration": 2.55},
#         {"Song": "Turn Down For What", "Artist": ["Lil Jon", "Twista"], "Album": "Turn Down for What", "Order": 2, "Duration": 3.4},
#         {"Song": "Red Camero", "Artist": ["Elvis"], "Album": "Greatest Hits", "Order": 3, "Duration": 1.56}]
# }
#
# songs = playlist.get("Songs")
# # for item in songs:
# #     song_list = []
# #     song_list.append(item.get("Song"))
# #     print(song_list)
# song_list = [item.get("Song") for item in songs]
# print(song_list)
# duration = [item.get("Duration") for item in songs]
# print(sum(duration))
# total_length = 0
# for song in playlist["Songs"]:
#     total_length += song["Duration"]
# print(total_length)

# alphabet = ('a', 'b', 'c', 'd')

# months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# locations = {
#     (35.6895, 39.6917): "Tokyo Office",
#     (40.7128, 74.0060): "New York Office",
#     (37.7749, 112.4194): "San Francisco Office"
# }
# coords = []
# for x in locations.keys():
#     coords.append(x)
# print(coords)

# for month in months:
#     print(month)

# i = len(months) - 1
# while i >= 0:
#     print(months[i])
#     i -= 1

# print(months.count("January"))
# print(months.index("November"))
# print(months[10])
# from random import random
# def coin_flip():
#     num = random()
#     if num > 0.5:
#         return "Heads"
#     else:
#         return "Tails"

# print(coin_flip())

# def square(input=5):
#     return input ** 2

# print(square(4))

# def sum_odd_numbers(list):
#     return sum([num for num in list if num %2 != 0])

# def sum_odd_numbers(list):
#     total = 0
#     for num in list:
#         if num % 2 != 0:
#             total += num
#     return total

# print(sum_odd_numbers([1,2,3,4,5,6,7]))

# import requests
# from bs4 import BeautifulSoup

# site = requests.get("https://www.drudgereport.com")
# soup = BeautifulSoup(site.text, "html.parser")

# headline_link = soup.find("b")

# print(headline_link)
# links = headline_link.find("a")["href"]

# for val in headline_link:
#     links.append(val.find("a")["href"])
# print(links)

# import bs4
# print(bs4.__doc__)

# names = ['austin', 'penny', 'anthony', 'angel', 'billy']
# print([val for val in names if val[0] == 'a'])

# people = ["Charlie", "Casey", "Cody", "Carly", "Cristina"]
# print(all([char[0] == "C" for char in people]))

# class User:
#     active_users = 0 

#     @classmethod
#     def display_active_users(cls):
#         return f"There are currently {cls.active_users} active users"

#     @classmethod
#     def from_string(cls, data_str):
#         first,last,age = data_str.split(",")
#         return cls(first, last, int(age))

#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         User.active_users += 1

#     def __repr__(self):
#         return f"{self.first}{self.last} is {self.age}"

#     def logout(self):
#         User.active_users -= 1
#         return f"{self.first} has logged out"

#     def full_name(self):
#         return f"{self.first} {self.last}"

#     def initials(self):
#         return f"{self.first[0]}.{self.last[0]}."

#     def likes(self, thing):
#         return f"{self.first} likes {thing}"

#     def is_senior(self):
#         if self.age >= 65:
#             return f"{self.first} {self.last} is a senior."
#         else:
#             return "You're young...good for you!"

#     def birthday(self):
#         self.age += 1
#         return f"Happy Birthday {self.first}! You're {self.age} today!"

# # user1 = User("Joe", "Garcia", 66)
# # user2 = User("Blanca", "Smith", 28)
# # print(User.display_active_users())
# # user3 = User("Abigail", "Granato", 6)
# # user4 = User("Olivia", "Granato", 4)
# # print(User.display_active_users())
# # user1.logout()
# # print(User.display_active_users())
# tom = User.from_string("Tom, Jones,89")
# print(tom.first)
# print(tom.full_name())
# print(tom)

# class Person:
#     def __init__(self):
#         self.name = "Tony"
#         self._secret = "Hi"

# p = Person()
# print(p.name)

# class Pet:
#     allowed = ["cat", "dog", "fish", "rat"]
#     def __init__(self, name, species):
#         if species.lower() not in Pet.allowed:
#             raise ValueError(f"You can't have a {species} pet!")
#         self.name = name
#         self.species = species

#     def set_species(self, species):
#         if species.lower() not in Pet.allowed:
#             raise ValueError(f"You can't have a {species} pet!")
#         self.species = species


# cat = Pet("Blue", "cat")
# dog = Pet("Wyatt", "dog")
# Pet.allowed.append("cobra")
# print(Pet.allowed)
# cat.set_species("cobra")
# print(cat.species)
# Pet.allowed.append("pig")
# print(Pet.allowed)
# print(cat.allowed)

# class Chicken:
#     total_eggs = 0
#     def __init__(self, species, name, eggs=0):
#         self.species = species
#         self.name = name
#         self.eggs = eggs

#     def lay_egg(self):
#         self.eggs += 1
#         Chicken.total_eggs += 1

# c1 = Chicken("Alice", "Partridge Silkie")
# c2 = Chicken("Amelia", "Speckled Sussex")

# print(Chicken.total_eggs)
# c1.lay_egg()
# print(Chicken.total_eggs)
# c2.lay_egg()
# c2.lay_egg()
# print(Chicken.total_eggs)
# print(c2.eggs)
# print(c1.eggs)

# DECK OF CARDS EXERCISE
# from random import shuffle
# class Card:
#     def __init__(self, value, suit):
#         self.value = value
#         self.suit = suit
    
#     def __repr__(self):
#         return f"{self.value} of {self.suit}"

# class Deck:
#     def __init__(self):
#         values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
#         suits = ['Heart', 'Spade', 'Club', 'Diamond']
#         self.cards = [Card(value, suit) for value in values for suit in suits]

#     def __repr__(self):
#         return f"Deck of {self.count()} cards"
    
#     def count(self):
#         return len(self.cards)

#     def deal(self, num_cards):
#         count = self.count()
#         actual = min(count, num_cards)
#         if count == 0:
#             raise ValueError("Only full decks can be dealt")
#         cards = self.cards[-actual:]
#         self.cards = self.cards[:-actual]
#         return cards

#     def deal_card(self):
#         return self.deal(1)[0]

#     def shuffle(self):
#         if self.count() < 52:
#             raise ValueError("Only full decks can be shuffled.")
#         return shuffle(self.cards)

# deck = Deck()
# print(deck.shuffle())
# print(deck.cards)
# print(deck.deal(5))
# print(deck.deal_card())
# print(deck.count())

# def testing(input):
#     return input.split("|")

# print(testing("I|AM|TESTING|THIS"))

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def __repr__(self):
#         return f"{self.name} is a {self.species}"

#     def make_sound(self, sound):
#         print(f"This animal says {sound}")

# class Cat(Animal):
#     def __init__(self, name, breed, toy):
#         super().__init__(name, species="Cat")
#         self.breed = breed
#         self.toy = toy

#     def play(self):
#         return f"{self.name} plays with {self.toy}"

# blue = Cat("Blue", "Scottish Fold", "String")
# print(blue)
# print(blue.play())
    
# class User:
#     active_users = 0 

#     @classmethod
#     def display_active_users(cls):
#         return f"There are currently {cls.active_users} active users"

#     @classmethod
#     def from_string(cls, data_str):
#         first,last,age = data_str.split(",")
#         return cls(first, last, int(age))

#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         User.active_users += 1

#     def __repr__(self):
#         return f"{self.first}{self.last} is {self.age}"

#     def logout(self):
#         User.active_users -= 1
#         return f"{self.first} has logged out"

#     def full_name(self):
#         return f"{self.first} {self.last}"

#     def initials(self):
#         return f"{self.first[0]}.{self.last[0]}."

#     def likes(self, thing):
#         return f"{self.first} likes {thing}"

#     def is_senior(self):
#         if self.age >= 65:
#             return f"{self.first} {self.last} is a senior."
#         else:
#             return "You're young...good for you!"

#     def birthday(self):
#         self.age += 1
#         return f"Happy Birthday {self.first}! You're {self.age} today!"

# class Moderator(User):
#     total_mods = 0
#     def __init__(self, first, last, age, community):
#         super().__init__(first, last, age)
#         self.community = community
#         Moderator.total_mods += 1
    
#     @classmethod
#     def display_active_mods(cls):
#         return f"There are currently {cls.total_mods} active moderators."

#     def remove_post(self):
#         return f"{self.full_name()} removed a post from the {self.community}"

# user1 = User("Evan", "Granato", 36)
# user2 = User("Tom", "Garcia", 35)
# print(User.display_active_users())
# print(user1)
# user1.logout()
# print(User.display_active_users())
# jasmine = Moderator("Jasmine", "O'Connor", 61, "Piano")
# timmy = Moderator("Timmy", "Timmerson", 12, "Jokes")
# print(jasmine.community)
# print(User.display_active_users())
# print(jasmine.remove_post())
# print(Moderator.display_active_mods())

# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclass needs to implement this method")

# class Dog(Animal):
#     def speak(self):
#         return "woof"

# class Cat(Animal):
#     def speak(self):
#         return "meow"

# cat = Cat()
# dog = Dog()
# animal = Animal()
# print(cat.speak())
# print(dog.speak())
# print(animal.speak())

# class GrumpyDict(dict):
#     def __repr__(self):
#         print("None of your business")
#         return super().__repr__()

#     def __missing__(self, key):
#         print("YOU WANT {key}, WELL, IT AIN'T HERE")
#         print('OK, FINE...')
#         super().__setitem__(key, value)


# d = GrumpyDict({"name": "Yoko", "city": "New York"})
# data = GrumpyDict({"first": "Tom", "animal": "cat"})
# print(d)
# print(data)
# data["city"] = "San Francisco"
# print(data)