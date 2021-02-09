weight = input("Weight: ")
typeW = input("lbs or kg:" )

if typeW[0].upper() == "K":
    print("You weigh " + str(float(weight)/0.45) + " pounds")
elif typeW[0].upper() == "L":
    print(f"You weigh {float(weight)*0.45} kilograms")
else:
    print("Invalid input!")