score = int(input("Enter your marks : "))

if score<=100 and score>=0:
    if score<60:
        grade='F'
    elif score<70:
        grade="D"   
    elif score<80:
        grade="C"
    elif score<90:
        grade="B"
    else:
        grade="A"
    print("Your Grade is",grade)
else:
    print("Enter a valid score.")

