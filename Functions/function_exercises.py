# ****EXERCISES****

# def product(num1,num2):
#     '''product(2,2) # 4 product(2,-2) # -4'''
#     return num1 * num2
# print(product(2,-2))

# def return_day(days=None):
#     '''return_day(1) # "Sunday"
#     return_day(2) # "Monday"
#     return_day(3) # "Tuesday"
#     return_day(4) # "Wednesday"
#     return_day(5) # "Thursday"
#     return_day(6) # "Friday"
#     return_day(7) # "Saturday"
#     return_day(41) # None'''
#     day = {2 : "Monday", 3 : "Tuesday", 4 : "Wednesday", 5 : "Thursday", 6 : "Friday", 7 : "Saturday", 1 : "Sunday"}
#     days = day.get(days)
#     if days:
#         return(days)
#
# print(return_day(10))
# ABOVE IS CORRECT, BUT COLT DID IT THIS WAY:
# def return_day(num):
#     '''return_day(1) # "Sunday"
#     return_day(2) # "Monday"
#     return_day(3) # "Tuesday"
#     return_day(4) # "Wednesday"
#     return_day(5) # "Thursday"
#     return_day(6) # "Friday"
#     return_day(7) # "Saturday"
#     return_day(41) # None'''
#     days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     if num > 0 and num <= len(days):
#         return days[num-1]
#     return None
# print(return_day(1))

# def last_element(l):
#     '''last_element([1,2,3]) # 3 last_element([]) # None'''
#     if l:
#         return l[-1]
#     else:
#         return None
# print(last_element([1,2,3,4])) # 4

# def number_compare(num1,num2):
#     '''number_compare(1,1) # "Numbers are equal" number_compare(1,0) # "First is greater" number_compare(2,4) # "Second is greater"'''
#     if num1 > num2:
#         return "First is greater"
#     elif num1 == num2:
#         return "Numbers are equal"
#     else:
#         return "Second is greater"
# print(number_compare(4,4) # Numbers are equal

# def single_letter_count(word, letter):
#     '''single_letter_count("Hello World", "h") # 1 single_letter_count("Hello World", "z") # 0 single_letter_count("HelLo World", "l") # 3'''
#     if letter in word:
#         return word.count(letter)
#     else:
#         return 0
# print(single_letter_count("jimmy johnson", "j")) # 2

# def multiple_letter_count(string):
#     '''multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}'''
#     if string:
#         return {letter : string.count(letter) for letter in string}
# print(multiple_letter_count("aeiou")) # {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

# def list_manipulation(list,command,location,value=None):
#     '''
#     list_manipulation([1,2,3], "remove", "end") # 3
#     list_manipulation([1,2,3], "remove", "beginning") #  1
#     list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
#     list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
#     '''
#     if (command == "remove" and location == "end"):
#         return list.pop()
#     elif (command == "remove" and location == "begining"):
#         return list.pop(0)
#     elif (command == "add" and location == "begining"):
#         list.insert(0,value)
#         return list
#     elif (command == "add" and location == "end"):
#         list.append(value)
#         return list
# print(list_manipulation([1,2,3], "add", "end", 30))

# def is_palindrome(char):
#     '''
#     is_palindrome('testing') # False
#     is_palindrome('tacocat') # True
#     is_palindrome('hannah') # True
#     is_palindrome('robert') # False
#     is_palindrome('amanaplanacanalpanama') # True
#     '''
#     if char == char[::-1]:
#         return True
#
# print(is_palindrome("aeiouoifa")) # False

# def frequency(list,num):
#     '''
#     frequency([1,2,3,4,4,4], 4) # 3
#     frequency([True, False, True, True], False) # 1
#     '''
#     return list.count(num)
# print(frequency([1,2,3,3,3,3],3)) # 4

# def multiply_even_numbers(list):
#     '''
#     multiply_even_numbers([2,3,4,5,6]) # 48
#     '''
#     total = 1
#     for val in list:
#         if val % 2 == 0:
#             total = total * val
#     return total
#
# print(multiply_even_numbers([2,3,4,5,6]))

# def capitalize(word):
#     '''
#     capitalize("tim") # "Tim"
#     capitalize("matt") # "Matt"
#     '''
#     return word[:1:].upper() + word[1::]
# print(capitalize("telling"))

# def compact(list):
#     """You enter list with any value and it returns the truthy values"""
#     return [val for val in list if val]
#
# print(compact([0,1,2,"",[], False, {}, None, "All done"])) # [1,2, "All done"])

# def intersection(list1,list2):
#     return [val for val in list1 if val in list2]
# print(intersection([1,2,3], [2,3,4]))

# def partition(list1,fn):
#     trues = []
#     falses = []
#     for val in list1:
#         if fn(val):
#             trues.append(val)
#         else:
#             falses.append(val)
#     return [trues, falses]

# OR

# def partition(list1, fn):
#     """A function that takes list and callback function to return list if True"""
#     return[[val for val in list1 if fn(val)], [val for val in list1 if not fn(val)]]
#
# print(partition([1,2,3,4], isEven)) # [[2,4],[1,3]])
