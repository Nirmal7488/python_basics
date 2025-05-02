class Student:
    def __init__(this,name,age):
        this.name=name
        this.age=age
    
    def display(this):
        print(f"Name : {this.name}, age : {this.age}")

s1=Student("Nirmal",23)
s1.display()