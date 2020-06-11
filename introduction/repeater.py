# times = input("How many times do I have to tell you?")
# times = int(times)
#
# for time in range(times):
#     print(F"time {time} CLEAN UP YOUR ROOM!")



# import random
# num = random.randint(1,20)
# print (num)

# Below is the exercise. Above is if you wanted a random number generated and the code to check what value the numbers have.
for num in range(1,21):
    if num == 4 or num == 13:
        print(f"{num} is unlucky")
    elif num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


