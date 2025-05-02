n=int(input("Enter how many elements do you want to add in List : "))
items=[]
flag=True
for i in range(n):
    ele=input("Enter the value : ")
    items.append(ele)

print(items,"\n")

for i in range(n):
    if items.count(items[i])>1:
        dup=items[i]
        flag=False
        break

if flag==True:
    print("List is Unique")
else:
    print(dup)
