# numbers = [1,2,3,4,5,6]
# evens = [num for num in numbers if num % 2 == 0]
# odds = [num for num in numbers if num % 2 != 0]
# print(evens)
# print(odds)

# print([num*2 if num % 2 == 0 else num/2 for num in numbers])
# Output: [0.5, 4, 1.5, 8, 2.5, 12]

# with_vowels = "This is so much fun!"
# print("".join(char for char in with_vowels if char not in "aeiou"))
# Output: Ths s s mch fn!

# ****Exercises****

# names = ["Elie", "Tim", "Matt"]
# answer = [person[0] for person in names]
# print(answer)

# list = [1,2,3,4,5,6]
#
# answer2 = [num for num in list if num %2 == 0]
# print(answer2)

# list = [1,2,3,4]
# list2 = [3,4,5,6]
# answer = [num for num in list if num in list2]
# print(answer)

# names = ["Elie", "Tim", "Matt"]
# answer2 = [char[::-1].lower() for char in names]
# print(answer2)

# nums = range(1,101)
# answer = [num for num in nums if num % 12 ==0]
# print(answer)

# string = "amazing"
# answer = [char for char in string if char not in "aeiou"]
# print(answer)