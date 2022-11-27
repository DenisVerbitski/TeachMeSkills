import time

class Auto:

    color = 'blue'
    weight = 300

    def __init__(self, brand, age, mark) -> None:
        self.brand = brand 
        self.age = age
        self.mark = mark
    
    def drive(self):
        print(f'Car: {self.brand} {self.mark} drives')

    def stop(self):
        print(f'Car: {self.brand} {self.mark} stops')

    def use(self):
        print(f"Car age + 1: {self.age + 1}")

class Truck(Auto):

    def __init__(self, brand, age, mark, max_load) -> None:
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def drive(self):
        print("Attention!")
        print(f'Car: {self.brand} {self.mark} drives')
    
    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Sedan(Auto):

    def __init__(self, brand, age, mark, max_speed) -> None:
        super().__init__(brand, age, mark)
        self.max_speed = max_speed
    
    def drive(self):
        print(f'Car: {self.brand} {self.mark} drives')
        print(f'max speed of {self.brand} {self.mark} is {self.max_speed}')

truck_info = Truck("Scania", 10, "R", 1500)
sedan_info = Sedan("BMW", 5, "520", 250)
truck_info.drive()
truck_info.load()
sedan_info.drive()
print(truck_info.max_load)
print(sedan_info.max_speed)