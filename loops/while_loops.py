# msg = input("What's the secret password?")
# while msg != "bananas":
#     print("Wrong")
#     msg = input("What's the secret password?")
# print("Correct")

# both of below codes get the same result
# for num in range(1,11):
#     print(num)

# num = 1
# while num < 11:
#     print(num)
#     num += 1
# for num in range(1,10)
#     print("\U0001f600" * num)


for x in range(3):
    num = 1
    while num <= 10:
        print("\U0001f600" * num)
        num += 1

# Nasty Loop:
# for num in range(1,11):
#     count = 1
#     smileys = ""
#     while count <= num:
#         smileys += "\U0001f600"
#         count += 1
#     print(smileys)