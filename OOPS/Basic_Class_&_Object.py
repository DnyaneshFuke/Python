class Car:
    def __init__(self, brand='None', model='None'):
        # Validate that brand and model are not negative numbers
        # Since they are strings, we will check if they are negative values when converted to integers.
        if (brand.startswith('-') and brand[1:].isdigit()) or (model.startswith('-') and model[1:].isdigit()):
            raise ValueError("Values can't be negative.")

        self.brand = brand
        self.model = model
        print("Car brand is:", self.brand)
        print("Car model is:", self.model)

try:         
    MyCar = Car("ABC", "2001")  # This will raise an error
except ValueError as e:
    print(e)

# These lines will only run if MyCar is successfully created
# If the above raises an error, MyCar will not be defined
if 'MyCar' in locals():
    print(MyCar.brand)
    print(MyCar.model)
