from django.apps import AppConfig

class SenderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sender'

    def ready(self):
        from .tasks import start_background_task
        start_background_task()
