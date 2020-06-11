# instructor = {
#     "name" : "Colt",
#     "owns_dog" : True,
#     "num_courses" : 4,
#     "favorite_language" : "Python",
#     "is_hilarious" : False,
#     44: "my favorite number!"
# }

# cat = {"name" : "blue", "age" : 3.5, "isCute" : True}
# print(cat)
# prints: {'name': 'blue', 'age': 3.5, 'isCute': True}

# cat2 = dict(name = "kitty")
# print(cat2)
# prints: {'name': 'kitty'}
# cat2 = dict(name = "kitty", age = 0.5)
# print(cat2)
# ****Exercises****
# user_info = {"name" : "Tim", "admin_access" : True, "department" : "IT"}
# print(user_info)

# print(instructor["name"])
# returns: "Colt"
# property = "isCute"
# print(cat[property])
# returns isCute from dictionary cat above.

# ****EXERCISE****
# artist = {"first" : "Neil", "last" : "Young"}
# full_name = artist["first"] + " " + artist["last"]
# print(full_name)
# returns: Neil Young with a space between them.

# ITERATING OVER DICTIONARY USING LOOPS

# instructor = {
#     "name" : "Colt",
#     "owns_dog" : True,
#     "num_courses" : 4,
#     "favorite_language" : "Python",
#     "is_hilarious" : False,
#     44: "my favorite number!"
# }
# for val in instructor.values():
#     print(val)
# returns values on each line
# print(instructor.values())
# returns: dict_values(['Colt', True, 4, 'Python', False, 'my favorite number!'])
# for val in instructor.keys():
#     print(val)
# prints the keys

#MOST OF THE TIME, YOU WILL WANT TO ACCESS ITEMS
# print(instructor.items())
# returns: dict_items([('name', 'Colt'), ('owns_dog', True), ('num_courses', 4), ('favorite_language', 'Python'), ('is_hilarious', False), (44, 'my favorite number!')])
# for k,v in instructor.items():
#     print(f"Key is {k} and {v} is value")
# ****EXERCISE****
# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# total_donations = 0
# for donation in donations.values():
#     total_donations += donation
# MORE ADVANCED FUNCTION IS JUST THIS LINE: total_donations = sum(donations.values())
# print(total_donations)

# HOW TO TEST FOR AN INSTANCE OF SOMETHING IN A DICTIONARY

# print("phone" in instructor)
# Returns False
# if "phone" in instructor:
#     print("phone")
# else:
#     print("nope")
# print(False in instructor.values())
# returns True

