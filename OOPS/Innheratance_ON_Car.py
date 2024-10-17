from Methord_Below_Construtor import Car
class ElectricCar(Car):
    def __init__(self, b, m, battery_size):
        super().__init__(b,m) 
        self.b_size = battery_size
        #print("Battery is:", self.b_size)
    def fullname(self):
        return f"The {self._b} and the car is {self._m} and the battery size is {self.b_size}"



ele_car=ElectricCar("Tesla","Model Spro","85Kwh")
print(ele_car.fullname())