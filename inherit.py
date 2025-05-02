class Animal:
    def speak(self):
        print("Animal speak")

class Dog(Animal):
    def __init__(self):
        super().__init__()
    def bark(self,name):
        print("Dog bark")

d1=Dog("")
d1.speak()
d1.bark()