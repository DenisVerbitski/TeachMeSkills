from django.db import models

from django.core.validators import RegexValidator

class User(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    login = models.CharField(max_length=20, validators=[RegexValidator(r"^[0-9]{3}$", message="Bad login", code='Invalid login')])
    email = models.EmailField()

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.first_name} {self.second_name}"

class Post(models.Model):
    title = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
