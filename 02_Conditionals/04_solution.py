color = input("Enter banana color : ")


if color=="Green":
    status = "Unripe"
elif color=="Yellow":
    status = "Ripe"
elif color=="Brown":
    status = "Overripe"
else :
    status = "Enter valid color"
    pass

print("Banana is",status)