# ***FILE/IO***
# File input/Output
# Objectives:
# - Read test files in Python
# - Write text files in Python
# - Use "with" blocks when reading/writing files
# - Describe the different ways to open a file
# - Read CSV files in Python
# - Write CSV files in Python
# - How JSON meshes with Python

# **READING FILES**
# - You can read a file with the open function
# - open returns a file object to you
# - You can read a file object with the read method

# file = open("story.txt")
# print(file.read()) # This short story is really short.
# print(file.read()) # NOTHING PRINTS
# print(file) # <_io.TextIOWrapper name='story.txt' mode='r' encoding='UTF-8'>
# help(file) # gives all of the details of what you can do.

# *CURSOR MOVEMENT* (WHY COULDN'T WE READ THE FILE TWICE????)
# - Python reads files by using a cursor
# - This is like the cursor you see when you're typing
# - After a file is read, the cursor is at the end
# - To move the cursor, use the seek method

# file = open("story.txt")
# print(file.read()) # This short story is really short.
# print(file.read()) # Now it's a little longer /n The end.
# print(file.seek(0)) # THIS MOVES THE CURSOR TO THE BEGINING
# print(file.read())
# file.seek(2)
# print(file.read()) # is short story is really short. ........

# SOMETIMES YOU JUST NEED TO READ A LINE:
# print(file.readline()) # This short story is really short.
# print(file.readline()) # Now it's a little longer
# print(file.readline()) # The end.

# READLINES returns a list of lines (PRESERVES THEM AS SEPERATE LINES
# file.seek(0)
# print(file.readlines()) # ['This short story is really short.\n', "Now it's a little longer\n", 'The end.']

# YOU HAVE TO CLOSE THE FILES MANUALLY AND IT IS VERY IMPORTANT
# **CLOSING A FILE**
# - You can close a file with the close method
# - You can check if a file is closed with the closed attribute
# - Once closed, a file can't be read unless you open it again.
# print(file.closed) # False
# file.close()
# print(file.closed) # True

# **WITH BLOCKS**       SLIGHTLY DIFFERENT, COMMON SYNTAX
# OPTION 1:
# file = open("story.txt")
# file.read()
# file.close()
# print(file.closed) # True

# OPTION 2:
# with open("story.txt") as file:
#     file.read()
#  print(file.closed) # True

# *****************************************IMPORTANT*****************************************
# with open("story.txt") as f:
#     data = f.read()
# print(f) # <_io.TextIOWrapper name='story.txt' mode='r' encoding='UTF-8'>
# print(f.closed) # True
# IN "WITH" STATEMENTS:
# - THERE'S A __enter__ METHOD
# - WHEN THE "WITH" STATEMENT IS DONE IT USES __exit__

# **WRITING TEXT FILES**
# WRITING FILES:
# - You can also use open to write to a file
# - Need to specify the "w" flag as the second argument

# EXAMPLE:
# with open("haiku.txt", "w") as file:
#     file.write("Writing files is great\n")
#     file.write("Here's another line of text\n")
#     file.write("Closing now, goodbye!")

# LEARNED THE "w" IS REALLY IMPORTANT. WON'T WORK WITHOUT IT.

# with open("haiku.txt", "w") as file:
#     file.write("Here's one more haiku\n")
#     file.write("What about the older one?\n")
#     file.write("Let's go check it out")

# WE DIDN'T PRESERVE THE OLD HAIKU, IT WAS **REPLACED**

# with open("haiku.txt", "w") as file:
#     file.write("Writing files is great\n")
#     file.write("Here's another line of text\n")
#     file.write("Closing now, goodbye!")

# with open("haiku.txt", "a") as file:
#     file.write("Here's one more haiku\n")
#     file.write("What about the older one?\n")
#     file.write("Let's go check it out")

# THE ABOVE "a" APPENDED THE HAIKU

# YOU DON'T HAVE TO HAVE A FILE CREATED ALREADY TO MAKE ONE:
# with open("lol.txt", "w") as file:
#     file.write("haha" * 10000)
# WROTE 10000 HAHAs TO A NEW FILE NAMED lol.txt

# **MODES FOR OPENING FILES**
# - r - Read a file (no writing)- this is the default
# - w - Writes to the file
# - a - Appends the file ALWAYS TO THE END, NEVER THE BEGINING OR ANYWHERE ELSE
# - r+ - Read and write to a file (writing based on cursor
# - "w" and "a" CAN MAKE NEW FILES IF THEY DON'T EXIST

# with open("haiku.txt", "r+") as file:
#     file.write("ADDED USING R+")
# ALWAYS STARTS AT THE BEGINING AND OVERWRITES WHATEVER'S THERE

# with open("haiku.txt", "r+") as file:
#     file.write(":)")
#     file.seek(10)
#     file.write(":(")
# result: :)WAS HERE:(IRST

# **EXERCISES**
# COPY CONTENTS OF ONE FILE TO ANOTHER:
# def copy(file_name, new_file_name):
#     with open(file_name) as file:
#         data = file.read()
#     with open(new_file_name, "w") as file2:
#         file2.write(data)

# COPY CONTENTS OF ONE FILE, REVERSE AND WRITE TO ANOTHER:
# def copy_and_reverse(file_name, new_file_name):
#     with open(file_name) as file:
#         data = file.read()
#     with open(new_file_name, "w") as file2:
#         file2.write(data[::-1])

# FUNCTION THAT TAKES FILE AND RETURNS DICTIONARY WITH NUMBER OF LINES, WORDS AND CHARACTERS IN FILE:
# def statistics(file_name):
#     with open(file_name) as file:
#         data2 = file.readlines()
#     return {"lines" : len(data2),
#             "words" : sum(len(line.split(" ")) for line in data2),
#             "characters" : sum(len(line) for line in data2)}

# FUNCTION THAT SEARCHES FOR WORD THEN REPLACES IT. REPLACES ALL INSTANCES:
# def find_and_replace(file_name, word, new_word):
#     with open(file_name, "r+") as file:
#         data = file.read()
#         new_word = data.replace(word, new_word)
#         file.seek(0)
#         file.write(new_word)
#         file.truncate()

