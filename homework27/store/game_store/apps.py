from django.apps import AppConfig
class GameStoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'game_store'

    def ready(self):
        import game_store.signals