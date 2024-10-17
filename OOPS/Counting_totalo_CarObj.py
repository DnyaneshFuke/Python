class Car:
    __total_car=0
    def __init__(self, brand='None', model='None'):
        Car.__total_car+=1
        # Validate that brand and model are not negative numbers
        # Since they are strings, we will check if they are negative values when converted to integers.
        if (brand.startswith('-') and brand[1:].isdigit()) or (model.startswith('-') and model[1:].isdigit()):
            raise ValueError("Values can't be negative.")

        self._b = brand
        self.__m = model
    def get_b(self):
        return self._b
    
    @classmethod
    def get_t(cls):    
        return cls.__total_car
    
    def fullname(self):
        return (f"The {self._b} and the car is {self.m}")
        #this is the functionality of object car
    @property
    def m(self):
        return self.__m
    @staticmethod
    def Dis():
        return f"THE CAR iS A medium of transport"
class ElectricCar(Car):
    def __init__(self, b, m, battery_size):
        super().__init__(b,m) 
        self.b_size = battery_size
        #print("Battery is:", self.b_size)
    def fullname(self):
        return super().fullname()+f" the battery size is {self.b_size}"


try:         
    M_Car = Car("BMW", "M2")  # This will raise an error
except ValueError as e:
     print(e)

# print(M_Car.fullname())
ele_car=ElectricCar("Tesla","Model Spro","85Kwh")
print(isinstance (ele_car,ElectricCar))
print(isinstance (ele_car,Car))
# M_Car.m="Rasnashdjh"
# print(M_Car.m)

# print(ele_car.fullname())
# print(Car.Dis())
class Battry():
    def battryinfo(self):
        return "The battery is 1000mah"
class Engine():
    def engineinfo(self):
        return "The engine is 1000cc"
class ele23(Battry,Engine,Car):
    pass


ele=ele23("Tesla","Model Spro")
print(ele.battryinfo())
print(ele.engineinfo())