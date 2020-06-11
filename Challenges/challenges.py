# **REVERSE STRING**
# def reverse_string(input):
#     return input[::-1]
# print(reverse_string("awesome"))

# **LIST CHECK**
# def list_check(vals):
#     return all(type(l) == list for l in vals)
#
# print(list_check([[],[1],[2,3],(1,2)]))

# **REMOVE EVERY OTHER**
# def remove_every_other(l):
#     return l[::2]
#
# print(remove_every_other([1,2,3,4,5]))

# **SUM PAIRS**
# def sum_pairs(ints,s):
#     already_visited = set()
#     for i in ints:
#         difference = s - i
#         # 6-4 = 2
#         # 6-2 = 4
#         if difference in already_visited:
#             # if 2 in 4, nope
#             # if 4 in 4, yep
#             return [difference, i]
#             # 4, 2
#         already_visited.add(i)
#     return []
#     # returned [4, 2]
#
# print(sum_pairs([4,2,10,5,1], 6))

# **COUNT VOWELS**
# def vowel_count(input):
#     lower_input = input.lower()
#     return {letter: lower_input.count(letter) for letter in lower_input if letter in "aeiou"}
# print(vowel_count("awesome"))

# **TITLEIZE**

# def titleize(input):
#     return ' '.join(s[0].upper() + s[1:] for s in input.split(' '))
#
# print(titleize('this is awesome')) # 'This Is Awesome

# **FIND FACTORS**
# def find_factors(input):
#     num_list = []
#     i = 1
#     while(i <= input):
#         if (input % i ==0):
#             num_list.append(i)
#         i += 1
#     return num_list
#
# print(find_factors(10)) # [1, 2, 5, 10]

# **INCLUDES**
# def includes(collection, value, start=None):
#     # return true if value exists in collection from the optional start
#     if start:
#         if value in collection[start:]:
#             return True
#         else:
#             return False
#     else:
#         if isinstance(collection, list) or isinstance(collection, str):
#             if value in collection:
#                 return True
#             else:
#                 return False
#         else:
#             if value in collection.values():
#                 return True
#             else:
#                 return False
#
# print(includes([1,2,3], 3, 2))

# **REPEAT**
# def repeat(string1, num):
#     return ' '.join(string1 * num)
# COLT'S WAY:
# def repeat(string, num):
#     if num == 0:
#         return ''
#     i = 0
#     new_str = ''
#     while i < num:
#         new_str += string
#         i += 1
#     return new_str

# print(repeat('abc', 3))

# **TRUNCATE**
# def truncate(string, num):
#     if num < 3:
#         return 'Truncation must be at least 3 characters'
#     new_string = ''
#     i = 0
#     while i < num - 3:
#         new_string += string[i]
#         i += 1
#     return new_string + " ..."
#
#
# print(truncate("Problem solving is the best", 10))

# **TWO LIST DICTIONARY**
# def two_list_dictionary(keys, values):
#     if len(keys) > len(values):
#         diff = len(keys) - len(values)
#         values.append("None" * diff)
#         return dict(zip(keys, values))

#     else:
#         return dict(zip(keys, values))

# print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))

# def range_in_list(list, start=0, end=None):
#     end = end or list[-1]
#     return sum(list[start:end+1])

# print(range_in_list(range_in_list([],0,1)))

# def same_frequency(num1, num2):
#     result = []
#     for t in str(num1):
#         result.append(t)
#     result.sort()
#     result2 = []
#     for t in str(num2):
#         result2.append(t)
#     result2.sort()
#     if result == result2:
#         return True
#     else:
#         return False
    

# print(same_frequency(551122,221515))

# def nth(list, num):
#     return list[num]

# print(nth(['a', 'b', 'c', 'd'], -4))

# def find_the_duplicate(list):
#     counter= {}
#     for val in list:
#         if val in counter:
#             counter[val] += 1
#             print(counter)
#         else:
#             counter[val] = 1
#     for key in counter.keys():
#         if counter[key] > 1:
#             return int(key)

# print(find_the_duplicate([6,1,9,5,3,4,9]))

# list1 = [
#   [ 1, 2 ],
#   [ 3, 4 ]
# ]
# list2 = [
#   [ 1, 2, 3 ],
#   [ 4, 5, 6 ],
#   [ 7, 8, 9 ]
# ]
# list3 = [
#   [ 4, 1, 0 ],
#   [ -1, -1, 0],
#   [ 0, 0, 9]
# ]
# list4 = [
#   [ 1, 2, 3, 4 ],
#   [ 5, 6, 7, 8 ],
#   [ 9, 10, 11, 12 ],
#   [ 13, 14, 15, 16 ]
# ]
# def sum_up_diagonals(list):
#     length = len(list) - 1
#     length2 = len(list) - length - 1
#     print(length2)
#     summing = []
#     for l in list:
#         summing.append(l[length])
#         length -= 1
#     for l in list:
#         summing.append(l[length2])
#         length2 += 1
#     return sum(summing)

# print(sum_up_diagonals(list1))

# def min_max_key_in_dictionary(input):
#     output = []
#     for x, y in input.items():
#         output.append(x)
#     return [min(output), max(input)]

# print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}))

# def find_greater_numbers(list):
#     count = 0
#     i = 0
#     j = 1
#     while i < len(list):
#         while j < len(list):
#             if list[j] > list[i]:
#                 count += 1
#             j += 1
#             i += 1
#         return count


# print(find_greater_numbers([1,2,3]))

# def two_oldest_ages(list):
#     return sorted(list)[-2:]

# print(two_oldest_ages( [1, 2, 10, 8] ))

# def is_odd_string(vals):
#     total = sum((ord(c) - 96) for c in vals.lower()) or 0
#     return total % == 1

# def valid_parentheses(string):
#     count = 0
#     i = 0
#     while i < len(string):
#         if string[i] == '(':
#             count += 1
#         elif string[i] == ')':
#             count -= 1
#         elif count < 0:
#             return False
#         i += 1
#     return count == 0

# print(valid_parentheses("(()(()))"))

# def reverse_vowels(s):
#     vowels = 'aeiou'
#     string = list(s)
#     i, j = 0, len(s) - 1
#     while i < j:
#         if string[i].lower() not in vowels:
#             i += 1
#         elif string[j].lower() not in vowels:
#             j -= 1
#         else:
#             string[i], string[j] = string[j], string[i]
#     return "".join(string)

# print(reverse_vowels("Hello!"))