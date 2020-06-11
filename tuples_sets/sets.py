# ****SETS****
# sets are like formal mathematical sets
# sets do not have duplicate values (any type of value)
# elements in sets aren't ordered
# you cannot access items in a set by index
# sets are useful are useful if you need to keep track of a collection of elements, but don't care about ordering, keys or values and duplicates.
# s = set({1,2,3,4,5,5,5})
# print(s)
# returns: {1, 2, 3, 4, 5}, the other 5s are not returned
# You can access all the values in a set with a good old for loop
# numbers = {1,2,3,4}
# for number in numbers:
#     print(number)
# returns the contents on separate lines
# ***USE CASE FOR SETS**
# IF YOU HAVE A LIST OF ITEMS, EXAMPLE IS CITIES THAT ATTENDEES OF A CONFERENCE ARE FROM.
# YOU WANT THOSE CITIES TO BE UNIQUE, YOU CAN MAKE A SET (cities = set({"tokyo", "New York", etc})
# MAKE IT A SET, THEN CONVERT TO A LIST AND THE DUPLICATES ARE REMOVED
# print(list(set(cities))) will return a list of cities

# ***SET METHODS***
# *ADD*
# s = set([1,2,3])
# s.add(4)
# print(s)
# returns: {1, 2, 3, 4}
# cities = {"Los Angeles", "Florence", "Boulder", "Oslo", "Tokyo", "Santiago", "Kyoto", "San Francisco", "Shanghai"}
# cities.add("Vancouver")
# print(cities)
# *REMOVE*
# removes a value from the set - returns a KeyError if the value is not found
# set1 = {1,2,3,4,5,6}
# set1.remove(3)
# print(set1)
# returns: {1, 2, 4, 5, 6}
# cities.remove("Oslo")
# print(cities)
# Removed "Oslo"
# *DISCARD*
# cities.discard("moscow")
# print(cities)
# You don't get an error when it isn't there
# *COPY*
# creates a copy of the set
# s = set([1,2,3])
# another_s = s.copy()
# print(another_s)
# returns: {1, 2, 3}
# *CLEAR*
# removes all the contents of the set
# s = set([1,2,3])
# s.clear()
# print(s)
# returns: set()
# *SET MATH*
# sets have a few other mathematical methods
# math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
# biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}
# Let's say I'm sending out report cards and I'm generating a set of all of my students.
# I want to bring the sets together, but not have duplicates
# print(math_students | biology_students)
# we use the | or "pipe" symbol to bring them together
# returns: {'Aparna', 'James', 'Charlotte', 'Jane', 'Matthew', 'Prashant', 'Helen', 'Oliver', 'Mesut'}
# if we want to find the duplicates (set intersections), we use &
# print(math_students & biology_students)
# returns: {'James', 'Matthew'}

# ****EXERCISES****
# numbers = (1,2,3,4)
# value = (1)
# static_values = (value)
# stuff = [1,3,1,5,2,5,1,2,5]
# unique_stuff = set(stuff)
# print(unique_stuff)

# ***SET COMPREHENSION***
# print({x**2 for x in range(10)})
# ** is squared
# same as dictionary comprehension, just without :
# returns: {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
# print({char.upper() for char in "hello"})
# returns: {'L', 'O', 'H', 'E'}
# string = "hello"
# print(len({char for char in string if char in "aeiou"}) == 5)
# returns: False because the length of returned vowels aren't 5
# def are_all_vowels_in_string(string):
#     return len({char for char in string if char in "aeiou"}) == 5
