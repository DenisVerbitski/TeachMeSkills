# Generated by Django 4.1.5 on 2023-01-28 15:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_store', '0003_category_games_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Название Игры'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=25, unique=True, verbose_name='Индивидуальный ярлык'),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Название Игры'),
        ),
        migrations.AlterField(
            model_name='game',
            name='slug',
            field=models.SlugField(max_length=25, unique=True, verbose_name='Индивидуальный ярлык'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='game_store_category_name_index'),
        ),
        migrations.AddIndex(
            model_name='game',
            index=models.Index(fields=['name'], name='game_store_game_name_index'),
        ),
    ]