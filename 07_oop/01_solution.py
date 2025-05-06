class Car:
    total_car=0
    def __init__(self,brand, model):
        self.__brand=brand
        self.model=model
        Car.total_car+=1

    def get_brand(self):
        return self.__brand

    def set_brand(self,brand):
        self.__brand=brand
    
    def showFullName(self):
        return f"{self.__brand} {self.model}"

    def fule_type(self):
        return "Petrol or Diesel"

    def general_description():
        return "car is the means of transport."
    


class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand,model)
        self.batterySize=batterySize
    
    def fule_type(self):
        return "Electric Charge."
    


class Battery():
    def batter_info(self):
        return "this is battery"

class Engine():
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass




myNewTesla=ElectricCarTwo("Tesla","Model S")
print(myNewTesla.engine_info())
print(myNewTesla.batter_info())







# teslaCar=ElectricCar("Tesla","Model S","85kWh")

# print(isinstance(teslaCar,Car))
# print(isinstance(teslaCar,ElectricCar))

# print(teslaCar.brand)
# teslaCar.set_brand("volvo")
# print(teslaCar.get_brand())

# print(teslaCar.fule_type())

# safari = Car("Tata","Safari")
# safari.model="Nexon"
# print(safari.showFullName())
# print(safari.total_car)

# print(safari.general_description())
# print(Car.general_description())













# my_Car=Car("Volvo","XC90")
# print(my_Car.brand)
# print(my_Car.model)

# my_new_car=Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.showFullName())
