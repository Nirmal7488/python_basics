day = input("Enter the day : ")
age = int(input("Enter the age : "))

price=12 if age>=18 else 8
if day=="Wednesday":
    price-=2

print(f"You have to pay : ${price}")




# if day=="Wednesday" or day=="wednesday":
#     if age<18:
#         print(f"You have to pay : ${child_price-discount}")
#     else:
#         print(f"You have to pay : ${adult_price-discount}")
# else:
#     if age<18:
#         print(f"You have to pay : ${child_price}")
#     else:
#         print(f"You have to pay : ${adult_price}")