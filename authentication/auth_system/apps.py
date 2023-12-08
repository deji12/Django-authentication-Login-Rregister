from django.apps import AppConfig


class AuthSystemConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "auth_system"

    def ready(self):
        # Import the function after the models are loaded
        from .models import create_groups

        create_groups()
