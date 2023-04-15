# for commit

weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")
unit = str(unit.upper())

if unit == "L":
    converted_weight = weight * 0.45359237
    converted_unit = "Kg"
elif unit == "K":
    converted_weight = weight / 0.45359237
    converted_unit = "Lbs"
else:
    print("Please enter a valid unit")

print("You are " + str(converted_weight) + converted_unit)
