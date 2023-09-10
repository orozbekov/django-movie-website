from typing import Any
from django.contrib.auth.base_user import BaseUserManager

ADMIN: str = "admin"
USER: str = "user"

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is requaired.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('user_role', USER)
        return self._create_user(email, password, **extra_fields)

    def creat_admin(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('user_role', ADMIN)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )
        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )

        return self._create_user(email, password, **extra_fields)
        