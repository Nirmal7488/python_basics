string = input("Enter a string : ")
new_str=""
for i in range(-1,-(len(string)+1),-1):
    print(string[i],end="")
    new_str+=string[i]

print(new_str)