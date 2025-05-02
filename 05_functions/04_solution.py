import math
def calculate(r):
    area=math.pi*r*r
    circ=2*math.pi*r
    return area,circ

area,circum=calculate(7)
print(area)
print(circum)