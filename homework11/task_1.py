from dataclasses import dataclass


@dataclass
class Dish:
    amount: int
    name: str
    price: int
    weight: int

dish_1 = Dish(1, 'Тушеная свинина', 1500, 650)
dish_2 = Dish(1, 'Тушеная говядина', 2000, 700)

class Order:
    def __init__(self) -> None:
        self.amount = 0
        self.price = 0
        self.weight = 0
        self.dish_list = []
        self.sum = 0
        self.money = 0

    def order(self, *args):

        dish_list = [args]

        for dish in dish_list:
            for value in dish:
                self.amount += value.amount
                self.price += value.price
                self.weight += value.weight

        return self.amount, self.price, self.weight

    def pay(self, money: int):

        self.money = money
        self.sum = self.price - self.money
        if self.sum > 0:
            print(f'Доплата составляет: {self.sum}')
        else:
            print(f'Ваша сдача: {abs(self.sum)}')

    def check(self):
        return print(f'Вы заказали {self.amount} блюда стоимостью {self.price}\nВнесено денег: {self.money}\n')

order_1 = Order()
order_1.order(dish_1, dish_2)
order_1.pay(5000)
order_1.check()
