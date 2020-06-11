# ***Dictionary Methods***
# Clear
# instructor.clear()
# this will erase everything
# instructor = {
#     "name" : "Colt",
#     "owns_dog" : True,
#     "num_courses" : 4,
#     "favorite_language" : "Python",
#     "is_hilarious" : False,
#     44: "my favorite number!"
# }
# Copy
# c = instructor.copy()
# now c has instructor in it

# fromkeys
# {}.fromkeys()
# new_user = {}.fromkeys(["name", "score", "email", "profile_bio"], "unknown")
# print(new_user)
# returns: {'name': 'unknown', 'score': 'unknown', 'email': 'unknown', 'profile_bio': 'unknown'}

# Get
# if a key is in a dictionary, it will return None if it isn't there
# print(instructor.get("Tim"))
# returns None

# ****EXERCISE****
# from random import choice
# food = choice(["cheese pizza", "quiche", "morning bun", "gummy bear", "tea cake"])
# bakery_stock = {"almond crouissant" : 12, "toffee cookie" : 3, "morning bun" : 1, "chocolate chunk cookie" : 9, "tea cake" : 25}
#
# print(food)
# for x,y in bakery_stock.items():
#     if x == food:
#         print(f"{y} left")
#         break
# else:
#     print("We don't make that")

# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]
# initial_game_state = dict.fromkeys(game_properties, 0)
# print(initial_game_state)

# ***Pop, Popitems, and update***
# d = dict(a=1, b=2, c=3)
# z = d.pop("a")
# returns 1
# instructor = {
#     "name" : "Colt",
#     "owns_dog" : True,
#     "num_courses" : 4,
#     "favorite_language" : "Python",
#     "is_hilarious" : False,
#     44: "my favorite number!"
# }

# print(instructor.pop("owns_dog"))

# ***popitem*** removes a random key in the dictionary
# print(instructor.popitem())
# returns: (44, 'my favorite number!')

# ***update*** updates keys and values in a dictionary with another set of key value parts
# person = {"city" : "Antigua"}
# instructor.update(person)
# ABOVE UPDATES THE DICT INSTRUCTOR TO ADD PERSON
# person.update(instructor)
# ABOVE UPDATES THE DICT PERSON TO ADD INSTRUCTOR
# person["name"] = "Evelia"
# Overwrites the "name in the dictionary
# print(person)
# print(instructor)
# Update only ADDS!!!!

# ****EXERCISE****
# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
# stock_list = inventory.copy()


# add the value 18 to stock_list under the key "cookie"
# stock_list["cookie"] = 18


# remove 'cake' from stock_list USE A DICTIONARY METHOD
# stock_list.pop("cake")
# print(stock_list)

# ****DATA MODELING USING DICTIONARIES****
# Spotify Playlist
# playlist = {
#     "title" : "running songs",
#     "author" : "Evan",
#     "songs" : [
#     {"title" : "all along the watchtower", "artist" : ["Dave Matthews"], "duration" : 2.5},
#     {"title" : "crash", "artist" : ["Dave Matthews"], "duration" : 5.25},
#     {"title" : "ants marching", "artist" : ["Dave Matthews", "Tim Reynolds"], "duration" : 2.0},
# ]
# }
# total_length = 0
# for song in playlist["songs"]:
#     total_length += song["duration"]
# print(total_length)
# returns 9.75

# ***DICTIONARY COMPREHENSION***
# Syntax:
# {____:____for___in___}
# iterates over keys by default
# to iterate over keys and values using . items()

# numbers = dict(first=1, second=2, third=3)
# squared_numbers = {key : value ** 2 for key,value in numbers.items()}
# print(squared_numbers)
# returns: {'first': 1, 'second': 4, 'third': 9}
# print({num : num**2 for num in [1,2,3,4,5]})
# returns: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# str1 = "ABC"
# str2 = "123"
# combo = {str1[i] : str2[i] for i in range(0,len(str1))}
# print(combo)
# returns: {'A': '1', 'B': '2', 'C': '3'}

# instructor = {"name" : "colt", "city" : "san francisco", "color" : "purple"}
#
# yelling_instructor = {k.upper() : v.upper() for k,v in instructor.items()}
# print(yelling_instructor)
# returns: {'NAME': 'COLT', 'CITY': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}

# num_list = [1,2,3,4]
# print({num:("even" if num % 2 == 0 else "odd") for num in num_list})
# returns: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}

