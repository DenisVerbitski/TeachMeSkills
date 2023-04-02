from django.db import models
from django.urls import reverse
from decimal import Decimal
from django.contrib.auth.models import User

class ShopInfoMixin(models.Model):
    name = models.CharField('Название', max_length=50, null=True)
    slug = models.SlugField('Индивидуальный ярлык', max_length=25)
    description = models.TextField('Описание')
    is_active = models.BooleanField('Доступен')

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['name'], name='%(app_label)s_%(class)s_name_index'),
        ]


class Category(ShopInfoMixin):
    games_amount = models.IntegerField('Колличество игр в категории', default=0)

    def __str__(self):
        return f'{self.name}'


class Game(ShopInfoMixin):
    pub_date = models.DateField('Дата Публикации', auto_now_add=True)
    release_date = models.DateField('Дата Выхода')
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None)
    game_image = models.ImageField('Изображение Игры', upload_to='game_store/media/games')

    def __str__(self):
        return f'{self.name}'



class Comment(models.Model):
    choices = [
        (Decimal("1.0"), "★☆☆☆☆ (1/5)"),
        (Decimal("2.0"), "★★☆☆☆ (2/5)"),
        (Decimal("3.0"), "★★★☆☆ (3/5)"),
        (Decimal("4.0"), "★★★★☆ (4/5)"),
        (Decimal("5.0"), "★★★★★ (5/5)"),
    ]
    game = models.ForeignKey(Game, blank=True, null=True, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='users')
    text = models.TextField('Комментарий')
    pub_date = models.DateTimeField(auto_now_add=True)
    grade = models.DecimalField('Оценка игры', decimal_places=1, max_digits=2, choices=choices)

    def __str__(self):
        return f"{self.user} {self.text}"

    def get_absolute_url(self):
        return reverse("game:game_slug", kwargs={"game_slug": self.game.slug})