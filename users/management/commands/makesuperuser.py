from typing import Any

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        email = "admin@usersnacks.com"
        new_password = get_random_string(10)

        try:
            user = User.objects.filter(is_superuser=True).exists()

            if not user:
                self.stdout.write("No superuser found, Creating superuser...")
                user = User.objects.create_superuser(email=email, password=new_password)

                self.stdout.write(self.style.SUCCESS("-------------------------------"))
                self.stdout.write(self.style.SUCCESS(f"Superuser created successfully"))
                self.stdout.write(self.style.SUCCESS(f"email: {email}"))
                self.stdout.write(self.style.SUCCESS(f"password: {new_password}"))
                self.stdout.write(self.style.SUCCESS("-------------------------------"))
            else:
                # Super user already exists
                self.stdout.write("Superuser already exists.")
        except Exception as e:
            # Error Creating a new superuser
            self.stdout.write(self.style.ERROR("Error creating superuser."))
            self.stdout.write(f"{e}")
