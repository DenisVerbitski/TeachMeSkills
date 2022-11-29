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


auto_info = Auto("Audi", 10, "A5")
auto_info.drive()
auto_info.stop()
auto_info.use()