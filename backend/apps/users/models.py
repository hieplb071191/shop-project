import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        print(':::extra_fields', extra_fields)
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        USER = "USER", "User"
        MANAGER = "MANAGER", "Manager"

    class PlatForm(models.TextChoices):
        GOOGLE = "GOOGLE", "Google"
        FACEBOOK = "FACEBOOK", "Facebook"
        LOCAL = "LOCAL", "Local"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    street_address = models.TextField(blank=True, null=True)
    town = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    role = models.TextField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
    )
    platform = models.TextField(
        max_length=20,
        choices=PlatForm.choices,
        null=False,
        default=PlatForm.LOCAL,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.email


# Create your models here.
