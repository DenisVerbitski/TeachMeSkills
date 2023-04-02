from django.db import models
from django.contrib.auth.models import User

from game_store.models import Game


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.customer} {self.product.name}"

    def total_amount(self):
        return self.product.price * self.quantity