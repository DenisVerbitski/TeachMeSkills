from django.db import models


class ShopInfoMixin(models.Model):
    slug = models.SlugField('Индивидуальный ярлык', max_length=25)
    description = models.TextField('Описание')
    is_active = models.BooleanField('Доступен')

    class Meta:
        abstract = True


class Category(ShopInfoMixin):
    title = models.CharField('Жанр', max_length=20)
    games_amount = models.IntegerField('Колличество игр', default=0)

    def __str__(self):
        return f'{self.title}'


class Game(ShopInfoMixin):
    name = models.CharField('Название Игры', max_length=50)
    pub_date = models.DateField('Дата Публикации', auto_now_add=True)
    release_date = models.DateField('Дата Выхода')
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None)
    game_image = models.ImageField('Изображение Игры', upload_to='game_store/media/games')

    def __str__(self):
        return f'{self.name}'