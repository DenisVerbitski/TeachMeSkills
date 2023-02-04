from django.db import models


class Category(models.Model):
    title = models.CharField('Жанр', max_length=20)
    slug = models.SlugField('Ярлык Категории', max_length=25)
    description = models.TextField('Описание Категории')
    is_active = models.BooleanField('Категория Доступна')

    def __str__(self):
        return f'{self.title}'


class Game(models.Model):
    name = models.CharField('Название Игры', max_length=50)
    pub_date = models.DateField('Дата Публикации', auto_now_add=True)
    release_date = models.DateField('Дата Выхода')
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)
    slug = models.SlugField('Ярлык Игры', max_length=35)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None)
    description = models.TextField('Описание Игры')
    game_image = models.ImageField('Изображение Игры', upload_to='shop/media/games')
    is_active = models.BooleanField('Игра Доступна')

    def __str__(self):
        return f'{self.name}'