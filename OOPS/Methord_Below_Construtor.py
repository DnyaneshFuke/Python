class Car:
    def __init__(self, brand='None', model='None'):
        # Validate that brand and model are not negative numbers
        # Since they are strings, we will check if they are negative values when converted to integers.
        if (brand.startswith('-') and brand[1:].isdigit()) or (model.startswith('-') and model[1:].isdigit()):
            raise ValueError("Values can't be negative.")

        self._b = brand
        self._m = model
    def get_b(self):
        return self._b
    
    def fullname(self):
        return (f"The {self._b} and the car is {self._m}")
        #this is the functionality of object car
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

# These lines will only run if MyCar is successfully created
# If the above raises an error, MyCar will not be defined
# if 'MyCar' in locals():
#     print(MyCar.b)
#     print(MyCar.m)
print(M_Car.fullname())
ele_car=ElectricCar("Tesla","Model Spro","85Kwh")
print(ele_car.fullname())