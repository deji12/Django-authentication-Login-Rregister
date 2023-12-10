from django.apps import AppConfig
from django.apps.registry import Apps
from django.db import OperationalError


class AuthSystemConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "auth_system"

    def ready(self):
        try:
            # Check if the Group model is available in the database
            from django.contrib.auth.models import Group

            Group.objects.exists()
        except OperationalError:
            # Handle the exception (e.g., log it) and exit gracefully
            print("Error checking if Group model exists: Database not ready.")
            return

        # Import the function after the models are loaded
        from .models import create_groups

        # Create groups only if the Group model exists
        create_groups()

        # If there are other models or functions that need to be imported,
        # add them here inside the try-except block.
