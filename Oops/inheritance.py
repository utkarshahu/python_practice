class Car:
    # Class variable shared among all Car and ElectricCar instances
    count = 0

    # Constructor
    def __init__(self, model, brand):
        self.__model = model              # instance variable
        self.__brand = brand            # private instance variable (name mangling)
        Car.count += 1                  # increment class-level count properly

    # Getter method for brand (with exclamation mark!)
    def get_brand(self):
        return self.__brand + "!"

    # Setter method to update brand
    def set_brand(self, value):
        self.__brand = value

    # Regular instance method - returns fuel type
    def fuel_type(self):
        return "Petrol"
    @property
    def model(self):
        return self.__model
    # Static method - no self/cls needed, doesn't access object or class data
    @staticmethod
    def description():
        print("It is a very fast and efficient car.")

# Inheriting from Car
class ElectricCar(Car):
    # Constructor for ElectricCar adds battery info
    def __init__(self, model, brand, battery):
        super().__init__(model, brand)   # call parent constructor
        self.battery = battery           # new property for ElectricCar

    # Overriding fuel_type method
    def fuel_type(self):
        return "Electric"


# 🔽 Using the classes 🔽

# Create a Car object
car2 = Car("Tata", "Nano")
print(car2.fuel_type())  # Output: Petrol

# Create an ElectricCar object
my_car = ElectricCar("S6", "BMW", "10kmh")
print(my_car.fuel_type())  # Output: Electric
# my_car.model = "Rose"
print(my_car.model)
# Update battery value
my_car.battery = 2777
print(my_car.battery)  # Output: 2777

# Access model (public)
print(my_car.model)  # Output: S6

# Get and set private brand using getter/setter
print(my_car.get_brand())  # Output: BMW!
my_car.set_brand("Mastang")
print(my_car.get_brand())  # Output: Mastang!

# Show total number of cars created (Car + ElectricCar)
print(Car.count)  # Output: 2

# Call static method using class name — no need to create an object
Car.description()           # Output: It is a very fast and efficient car.
ElectricCar.description()   # ✅ Also works due to inheritance
