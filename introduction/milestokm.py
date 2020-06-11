print("How many miles did you run?")
miles = float(input())
kms = miles * 1.60934
kms = round(kms, 2)
print(f"Your {int(miles)} mile run was {kms} kilometers long!")
