string = input("Enter a string : ")

for char in string:
    if string.count(char)==1:
        print(f"'{char}' is first non repeating character.")
        break