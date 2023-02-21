from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Category, Game


@receiver(post_save, sender=Game)
def category_games_amount_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.category.games_amount += 1
        print(f"Плюс игра в категории {instance.category}")
        instance.category.save()


@receiver(post_delete, sender=Game)
def category_games_amount_post_delete(sender, instance, *args, **kwargs):
    instance.category.games_amount -= 1
    print(f"Минус игра в категории {instance.category}")
    instance.category.save()