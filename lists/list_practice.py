# string = "amazing"
# answer = [char for char in string if char in "aeiou"]
# print(answer)

# numbers = [1,2,3,4,5,6]
# evens = [num for num in numbers if num % 2 == 0]
# print(evens)
# odds = [num for num in numbers if num % 2 != 0]
# OR odds = [num for num in numbers if not num % 2 == 0]
# print(odds)

num1 = [1,3,5,7,9]
num2 = [2,4,6,8,10]
# num3 = zip(num1, num2)
# print(list(num3))
combined = [val for val in zip(num1, num2) for val in val]
print(combined)
