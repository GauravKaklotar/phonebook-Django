from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set', 
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts', null=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

class Spam(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    marked_by = models.ManyToManyField(User, related_name='marked_spam')
