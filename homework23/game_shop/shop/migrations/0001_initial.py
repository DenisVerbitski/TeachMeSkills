# Generated by Django 4.1.5 on 2023-01-29 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Жанр')),
                ('slug', models.SlugField(max_length=25, verbose_name='Ярлык Категории')),
                ('description', models.TextField(verbose_name='Описание Категории')),
                ('is_active', models.BooleanField(verbose_name='Категория Доступна')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название Игры')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Дата Публикации')),
                ('release_date', models.DateField(verbose_name='Дата Выхода')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена')),
                ('slug', models.SlugField(max_length=35, verbose_name='Ярлык Игры')),
                ('description', models.TextField(verbose_name='Описание Игры')),
                ('game_image', models.ImageField(upload_to='shop/media/games', verbose_name='Изображение Игры')),
                ('is_active', models.BooleanField(verbose_name='Игра Доступна')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.category')),
            ],
        ),
    ]