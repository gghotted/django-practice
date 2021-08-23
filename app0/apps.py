from django.apps import AppConfig


class App0Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app0'

    def ready(self):
        import app0.signals
