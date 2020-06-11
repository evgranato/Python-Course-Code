# ask for age
# age = input("How old are you?")
# if age:
#     age = int(age)
#     if age >= 18 and age < 21:
#         print("You can enter, but you need a wristband.")
#     # 18-21 wristband
#     elif age >= 21:
#         print("Come on in and drink it up!")
#     # 21+ drink, normal entry
#     else:
#         print("Too young, sorry.")
#     # too young, sorry
# else:
#     print("Please enter an age.")
#     #anything else is caught by this.

#could also do this:
#if age and (age >= 18 and < 21):
    #print("You can enter, but need a wristband")
#elif age and age >=21:
    #print("Come on in and drink it up!")

age = input("How old are you?")
if age:
    age = int(age)
    if age >= 21:
        print("Come on in and drink it up!.")
    # 21
    elif age >= 18:
        print("Come on in and drink it up!")
    # need wristband
    else:
        print("Too young, sorry.")
    # too young, sorry
else:
    print("Please enter an age.")
    #anything else is caught by this.