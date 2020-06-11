# **READING CSV FILES**
# - CSV files are common for tabulated data
# - We can read CSV files just like text files
# - Python has a built-in CSV module to read/write CSVs more easily

# **CSV MODULE**
# - reader - lets you iterate over rows of the CSV as lists
# - DictReader - lets you iterate over rows of the CSV as OrderedDicts

# reader:
# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     next(csv_reader) # This gets rid of the header
#     for row in csv_reader:
#         print(row)
# PRINTS THEM AS LISTS ON SEPARATE LINES

# DictReader:
# from csv import DictReader
# with open("fighters.csv") as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader:
#         print(row)
# PRINTS THEM AS DICTIONARY WITH KEY AS FIRST LINE, VALUE AS CORRESPONDING VALUE

# from csv import DictReader
# with open("fighters.csv") as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader:
#         print(row["Name"], row["Country"]) # prints names countries on separate lines

# OTHER DELIMITERS:
# - Readers accept a delimiter kwarg in case your data isn't separated by commas.
# from csv import reader
# with open("example.csv") as file:
#     csv_reader = reader(file, delimiter="|")
#     for row in csv_reader:
#         print(row) # EACH ROW IS A LIST!
# from csv import reader
# with open("fighters2.csv") as file:
#     csv_reader = reader(file, delimiter=" ")
#     for row in csv_reader:
#         print(row) # I USED SPACES AS THE DELIMITER IN THE NEW CSV. RETURNED SEPARATED VALUES.

# **WRITING TO CSV FILES**
# - USING LISTS:
# - writer - creates a writer object for writing to CSV
# - writerow - method on a writer to write a row to the CSV

# from csv import writer
# with open("fighters.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Character", "Move"])
#     csv_writer.writerow(["Ryu", "Hadouken"])

# ONE FILE OPEN AT A TIME:
# from csv import reader, writer
#
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     fighters = [[s.upper() for s in row] for row in csv_reader] # UPPER CASING THE ROWS WITH LIST COMP.
#     for row in fighters:
#         print(row)
#
# with open("fighters3.csv", "w") as file:
#     csv_writer = writer(file)
#     for fighter in fighters:
#         csv_writer.writerow(fighter) # WROTE FIGHTERS.CSV IN UPPER CASE IN THE NEW FILE.
# **OR, USING NESTED WITH STATEMENTS:
# from csv import reader, writer
#
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     with open("fighters3.csv", "w") as file:
#         csv_writer = writer(file)
#         for fighter in csv_reader:
#             csv_writer.writerow([s.upper() for s in fighter])

# WRITING CSV FILES
# USING DICTIONARIES
# - DictWriter - creates a writer object for writing using dictionaries
# - fieldnames - kwarg for the DictWriter specifying headers
# - writeheader - method on a writer to write a header row
# - writerow - method on a writer to write a row based on a dictionary

# from csv import DictWriter
# with open("fighters4.csv", "w") as file:
#     headers = ["Character", "Move"]
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({"Character" : "Ryu", "Move" : "Hadouken"})
# TAKE FIGHTERS.CSV AND MAKE NEW CSV WITH HEIGHT IN INCHES:
# from csv import DictReader, DictWriter
#
# def cm_to_in(cm):
#     return round(float(cm) * 0.393701, 2)
#
# with open("fighters.csv") as file:
#     csv_read = DictReader(file)
#     fighters = list(csv_read)
#
# with open("fighters5.csv", "w") as file:
#     headers = ("Name", "Country", "Height (in in)")
#     csv_write = DictWriter(file, fieldnames=headers)
#     csv_write.writeheader()
#     for f in fighters:
#         csv_write.writerow({
#             "Name" : f["Name"],
#             "Country" : f["Country"],
#             "Height (in in)" : cm_to_in(f["Height (in cm)"])
#         })

# **EXERCISES**
# from csv import reader, writer
#
# def add_user(first, last):
#     with open("users.csv", "a") as file:
#         csv_write = writer(file)
#         csv_write.writerow([first, last])
#
# add_user("Dewayne", "Johnson")
# from csv import reader
# def print_users():
#     with open("users.csv") as file:
#         csv_read = reader(file)
#         next(csv_read)
#         for line in csv_read:
#             print(f"{line[0]} {line[1]}")
#         #     print(line["First Name"], line["Last Name"])
# print_users()

# from csv import DictReader
#
# def find_user(first, last):
#     with open("users.csv") as file:
#         csv_read = DictReader(file)
#         i = 1
#         for val in csv_read:
#             if first in val["First Name"] and last in val["Last Name"]:
#                 return f"# {i}"
#             i += 1
#         return f"{first} {last} not found"
#
# print(find_user("Dewayne", "Johnson"))
# COLT'S ANSWER:
# import csv
#
#
# def find_user(first_name, last_name):
#     with open("users.csv") as file:
#         csv_reader = csv.reader(file)
#         for (index, row) in enumerate(csv_reader):
#             first_name_match = first_name == row[0]
#             last_name_match = last_name == row[1]
#             if first_name_match and last_name_match:
#                 return index
#         return "{} {} not found.".format(first_name, last_name)

# **PICKLING**
# - Module "Pickling in a Jar"
# BASICALLY SAVING A FILE FOR NEXT TIME YOU OPEN THE FILE
# import pickle
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
# class Cat(Animal):
#     def __init__(self, name, breed, toy):
#         super().__init__(name, species="Cat")
#         self.breed = breed
#         self.toy = toy
#
#     def play(self):
#         print(f"{self.name} plays with {self.toy}")
# #
# # blue = Cat("Blue", "Scottish Fold", "String")
# #
# # with open("pets.pickle", "wb") as file:
# #     pickle.dump(blue, file)
#
# with open("pets.pickle", "rb") as file:
#     zombie_blue = pickle.load(file)
#     print(zombie_blue)
#     print(zombie_blue.play())
# RETURNED:
# Blue is a Cat
# Blue plays with String

# **EXTRA FANCY JSON PICKLING**
# JSON.DUMPS - CONVERTS PYTHON CODE TO JSON FORMAT AUTOMATICALLY
# import json
#
# class Cat:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
# c = Cat("Charles", "Tabby")
# print(c.__dict__)
# # j = json.dumps(['foo', {'bar' : ('baz', None, 1.0, 2)}])
# j = json.dumps(c.__dict__)
# print(j) # ["foo", {"bar": ["baz", null, 1.0, 2]}]

# JSON PICKLING MODULE IS HOW TO DO ALL OF THIS.
# import jsonpickle
# class Cat:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
# c = Cat("Charles", "Tabby")
# SHOWING HOW WE CAN ENCODE AS JSON:
# frozen = jsonpickle.encode(c)
# print(frozen) # {"py/object": "__main__.Cat", "name": "Charles", "breed": "Tabby"}
# with open("cat.json", "w") as file:
#     frozen = jsonpickle.encode(c)
#     file.write(frozen)

# NOW WE CAN SHOW HOW IT WOULD DECODE:
# with open("cat.json", "r") as file:
#     contents = file.read()
#     unfrozen = jsonpickle.decode(contents)
#     print(unfrozen)

# **EXERCISES**
# from csv import reader, writer
# def update_users(old_first, old_last, new_first, new_last):
#     with open("users.csv") as file:
#         csv_read = reader(file)
#         rows = list(csv_read)
#     i = 0
#     with open("users.csv", "w") as file:
#         csv_write = writer(file)
#         for row in rows:
#             if row[0] == old_first and row[1] == old_last:
#                 csv_write.writerow([new_first, new_last])
#                 i += 1
#             else:
#                 csv_write.writerow(row)
#         return f"Users Updated : {i}"
#
# print(update_users("Colt", "Steele", "RamRod", "Steele"))
# from csv import reader, writer
# def delete_users(first, last):
#     with open("users.csv") as file:
#         csv_reader = reader(file)
#         data = list(csv_reader)
#     i = 0
#     with open("users.csv", "w") as file:
#         csv_writer = writer(file)
#         for row in data:
#             if row[0] == first and row[1] == last:
#                 i += 1
#             else:
#                 csv_writer.writerow(row)
#         return f"Users deleted: {i}"
#
# print(delete_users("Ramrod", "Steele"))