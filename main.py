#Python weight converter

weight = float(input("Enter your weight: "))
units = input("Kilograms or Pounds (K OR L)")

if units == "K":
    weight = weight * 2.205
    units = "Lbs"
    print(f"Your weight is: {weight}{units}")

elif units == "L":
    weight = weight / 2.205
    units = "Kgs"
    print(f"Your weight is: {weight}{units}")

else:
    print(f"{units} is not valid")