password = input("Enter your passowrd : ")
length = len(password)
if length<6:
    status = "Weak"
elif length<10:
    status = "Medium"
else:
    status = "Strong"

print("your password is",status)