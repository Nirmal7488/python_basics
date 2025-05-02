number = int(input("Enter a number : "))
sum=0
for i in range(1,number):
    if i%2==0:
        sum+=i

print(f"Sum of even number upto {number} is {sum}")