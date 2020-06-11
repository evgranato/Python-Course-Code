# ****TUPLES****
# an ordered collection or grouping of items that is immutable
# x = (1,2,3,4)
# x[0] = "change me!"
# returns: TypeError: 'tuple' object does not support item assignment

# alphabet = ("a", "b", "c", "d")
# can't do anything with it without and error...
# Why use a touple?
# -Faster than lists
# -Makes safer code. You aren't going to change anything
# -Use touples as a valid key in a dictionary
# ***EXAMPLE***
# months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October"
#           , "November", "December")
# You can access them just like a list
# print(months[0])
# returns: January
# locations = {
#     (35.6905, 39.6917) : "Tokyo Office",
#     (40.7128, 74.0060) : "New York Office",
#     (37.7749, 122.4194) : "San Francisco Office"
# }
# the () above are Touples
# print(locations[(37.7749, 122.4194)])
# returns: San Francisco Office

# ****TUPLE METHODS****
# names= ("Colt", "Blue", "Rusty", "Lassie")
# for name in names:
#     print(name)
# returns: the names above
# for month in months:
#     print(month)

# i = len(months) - 1
# while i >= 0:
#     print(months[i])
#     i -= 1
# returns months listed in reverse
# **TUPLE METHODS**
# **Count**
# x = (1,2,3,3,3)
# x.count(1) # 1
# x.count(3) # 3

# **Index**
# x.index(1) # 0
# x.index(5) # Not in Tuple
# x.index(3) # 2 -only the first index is returned