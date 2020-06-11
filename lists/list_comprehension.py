# [___for____in____]
# nums = [1,2,3]
# print([x*10 for x in nums])

# numbers = [1,2,3,4,5]
# doubled_numbers = []
#
# for num in numbers:
#     doubled_number = num * 2
#     doubled_numbers.append(doubled_number)
# print(doubled_numbers)

# ***Same As:***
# numbers = [1,2,3,4,5]
# doubled_numbers = [num * 2 for num in numbers]
# print(doubled_numbers)

# name = "Colt"
# print([char.upper() for char in name])
# output is ["C", "O", "L", "T"]

# print([num*10 for num in range(1,6)])

# print([bool(val) for val in [0,[],""]])
# Output is [False, False, False]

# nums = [1,2,3,4,5,6]
#
# print([str(num) for num in nums])

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

print([color.upper() for color in colors])