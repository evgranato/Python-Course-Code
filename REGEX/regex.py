# ***REGEX***
# A WAY OF DESCRIBING PATTERNS WITHIN SEARCH STRINGS

# VALIDATING EMAILS EXAMPLE:
# colt@gmail.com
# HOW DO WE TELL OUR CODE WHAT YOU SHOULD ACCEPT??
# starts with 1 or more letter, number, +, _, -, . then
# a single @ sign then
# 1 or more letter, number or - then
# a single dot then
# ends with 1 or more letter, number, - or .
# LETS USE A REGULAR EXPRESSION!
# (^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)
# ^ means start, the rest is what it could contain
# + letters numbers dash
# + \. means period. you have to use the \ because . means something in regex
# followed by letters, numbers or dashes
# $ is end with that

# **POTENTIAL USE CASES**
# CREDIT CARD NUMBER VALIDATING
# PHONE NUMBER VALIDATING
# ADVANCED FIND/REPLACE IN TEXT
# FORMATTING TEXT/OUTPUT
# SYNTAX HIGHLIGHTING

# THE IDE (PYCHARM) PROBABLY USES REGEX FOR SYNTEX HIGHLIGHTING WHEN YOU ARE CODING:
# def hello_world(thingy):
#     #I do nothing
#     print("Hello World!")

# **WRITING BASIC REGEX**
# this is outside of python

# WENT TO PYTHEX.ORG AND USED THIS TEST STRING INFO:
# hello world aaabbbcccdddeeefffggg
# I like cats :)
# PURPLE
# kitty@gmail.com
# She is 49 years old

# SOME REGEX SYNTAX:
# \d - digit 0-9
# \w - letter, digit or underscore
# \s - whitespace character
# \D - not a digit
# \W - not a word character
# \S - not a whitespace character
#  . - any character except line break

# **SOME REGEX SYNTAX**
# QUANTIFERS
# + - one or more
# {3} - Exactly x times. {3} - 3 times
# {3,5} - Three to five times
# {4,} - Four or more times
# * - Zero or more times
# ? - Once or none (optional item in the characters)

# **REGEX BASICS: CHARACTER CLASSES AND SETS**
# ALLOWS US TO SPECIFY GROUPS OR RANGES OF CHARACTERS IN A []
# **SOME REGEX SYNTAX**
# ANCHORS AND BOUNDARIES:
# ^ - Start of a string or line
# $ - End of string or line
# \b - Word boundary

# **LOGICAL OR**
# | PIPE CHARACTER
# USE () TO GROUP PARTS BEING PIPED

# **INTRODUCTION TO THE RE MODULE**

# import regex module
# import re
#
# # define our phone number regex
# pattern = re.compile(r'\d{3} \d{3}-\d{4}')
#
# # search a string with our regex
# res = pattern.search('Call me at 415 555-4242!')

# import re

# pattern = re.compile(r'\d{3} \d{3}-\d{4}')
#
# res = pattern.search("call me at 210 542-0110 or 310 443-3029")
# print(res) # <re.Match object; span=(11, 23), match='210 542-0110'>
# print(res.group()) # 210 542-0110 ***GIVES THE ACTUAL MATCH WHEN USING RES.GROUP() ONLY GIVES FIRST MATCH
# res = pattern.findall("call me at 210 542-0110 or 310 443-3029")
# print(res) # ['210 542-0110', '310 443-3029']

# WE DON'T HAVE TO USE THE COMPILE:
# no_compile = re.search(r'\d{3} \d{3}-\d{4}', "call me at 310 445-9876").group()
# print(no_compile) # 310 445-9876
# THE REASON TO USE THE COMPILE, IT'S MORE EFFICIENT SINCE YOU DON'T HAVE TO COMPILE
# EVERY TIME YOU SEARCH.

# **VALIDATING PHONE NUMBERS WITH PYTHON**
# import re
#
# def extract_phone(input):
#     phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
#     match = phone_regex.search(input)
#     if match:
#         return match.group()
#     return None
#
# def extract_all_phones(input):
#     phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
#     match = phone_regex.findall(input)
#     if match:
#         return match
#     return None

# print(extract_phone("my number is 432 567-8976"))
# print(extract_phone("my number is 432 567-897654"))
# print(extract_all_phones("my number is 432 567-9876 or call me at 454 339-9382"))

# def is_valid_phone(input):
#     phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
#     match = phone_regex.search(input)
#     if match:
#         return True
#     return False

# def is_valid_phone(input):
#     phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
#     match = phone_regex.fullmatch(input)
#     if match:
#         return True
#     return False
#
# print(is_valid_phone("432 567-8976"))
# print(is_valid_phone("432 567-8976 jdkjd"))

# ***EXERCISES***
# TIME VALIDATING
# import re
#
# def is_valid_time(input):
#     time_regex = re.compile(r'^\d\d?\:\d{2}$')
#     match = time_regex.fullmatch(input)
#     if match:
#         return True
#     return False
#
# print(is_valid_time("9:45"))

# **PARSING URLS WITH PYTHON**
# https?://www\.[A-Za-z-]{2,256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//=]*
# import re
#
# # url_regex = re.compile(r'https?://www\.[A-Za-z-]{2,256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//=]*')
# # match = url_regex.search("http://www.youtube.com/videos")
# # print(match.group()) # http://www.youtube.com/videos
# url_regex = re.compile(r'(https?)://(www\.[A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
# match = url_regex.search("http://www.youtube.com/videos")
# # PUT () AROUND ANYTHING WE WANT TO GROUP AND ANALYZE:
# # print(match.groups()) # ('http', 'www.youtube.com', '/videos')
# print(match.group(0)) # http://www.youtube.com/videos
# print(match.group(1)) # http
# print(match.group(2)) # www.youtube.com
# print(match.group(3)) # /videos

# **EXERCISES**
# PARSING BYTES EXERCISE:
# import re
#
# def parse_bytes(input):
#     byte_regex = re.compile(r'(\b[1,0]{8})\b')
#     match = byte_regex.findall(input)
#     return match
#
# print(parse_bytes("11010101 101 323")) # ['11010101']
# print(parse_bytes("11010101 11100010")) # ['11010101', '11100010']
# print(parse_bytes("afdse")) # []

# **SYMBOLIC GROUP NAMES**
# import re
# def parse_name(input):
#     name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
#     matches = name_regex.search(input)
#     first_name = matches.group('first')
#     last_name = matches.group('last')
#     print(first_name)
# # parse_name("Mrs. Tilda Swinton") # ('Mrs.', 'Tilda', 'Swinton')
# # ?P<label> gives the group a name that you can call in the group() function

# **EXERCISES**
# DATE PARSING EXERCISE:
# import re
#
# def parse_date(input):
#     date_regex = re.compile(r'^(\d\d)[,/.](\d\d)[,/.](\d{4})$')
#     match = date_regex.search(input)
#     if match:
#         return {
#             'd': match.group(1),
#             'm': match.group(2),
#             'y': match.group(3)
#         }
#     return None
#
# print(parse_date("12/11/2003"))

#import re
#
#def grab_email(input):
#	email_regex = re.compile(r'(\b[a-zA-Z0-9]+\@[a-zA-Z0-9]+\.[A-Za-z]+\b)')
#	match = email_regex.findall(input)
#	if match:
#		return match
#	return False
#
#print(grab_email('evgranato@gmail.com and evan@starstek.com and evan@dealerretriever.com ev@.com'))

# **REGEX FLAGS**
# IN THE DOCS, WE CAN USE THE 'VERBOSE' TAG TO ADD COMMENTS THROUGHT THE REGEX TO # EXPLAIN WHAT IS HAPPENING.
# import re
#
# # pat = re.compile(r'^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$')
#
# pattern = re.compile(r"""
# 	^([a-z0-9_\.-]+)	#FIRST PART OF EMAIL
# 	@					#SINGEL @ SIGN
# 	([\da-z\.-]+)		# EMAIL PROVIDER
# 	\.					# SINGLE PERIOD
# 	([a-z\.]{2,6})$		# COM, ORG, NET, ETC.
# """, re.VERBOSE)
#
# match = pattern.search("thomas123@yahoo.com")
# print(match.groups())
# print(match.group())

# **REGEX SUBSTITUTION BASICS**
# .sub(replacement, string, count=0)
# import re
#
# text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"
#
# # pattern = re.compile(r'(Mr.|Mrs.|Ms.) [a-z]+', re.I) # re.I is Ignore Case
# #result = pattern.sub('\g<1> REDACTED', text)
# #print(result) # Last night Mrs. REDACTED and Mr. REDACTED murdered Ms. REDACTED
# # \g<1> refers to a capture group in your regex
# pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
# result = pattern.sub('\g<1> \g<2>', text)
# print(result) # Last night Mrs. D and Mr. w murdered Ms. C

# **EXERCISES**
# REGEX PROFANITY FILTER:
# import re
#
# def censor(input):
#     regex_prof = re.compile(r'\bfrack\w*\b', re.I)
#     result = regex_prof.sub("CENSORED", input)
#     return result
#
# print(censor("Fracking you"))

# **SWAPPING FILE NAMES**
# import re
# titles = [
#     "Significant Others (1987)",
#     "Tales of the City (1978)",
#     "The Days of Anna Madrigal (2014)",
#     "Mary Ann in Autumn (2010)",
#     "Further Tales of the City (1982)",
#     "Babycakes (1984)",
#     "More Tales of the City (1980)",
#     "Sure of You (1989)",
#     "Michael Tolliver LIves (2007)"
# ]
# # This is what we want: 1978 - Tales of the City
# pattern = re.compile(r'(^[\w ]+) \((\d{4})\)')
# fixed_titles = []
# for book in titles:
#     result = pattern.sub("\g<2> - \g<1>", book)
#     fixed_titles.append(result)
#
# fixed_titles.sort()
# print(fixed_titles)

