# weight conversion

weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    converted = weight / 0.4536
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.4536
    print("Weight in Kgs: " + str(converted))
