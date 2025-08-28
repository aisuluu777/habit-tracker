from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, PermissionsMixin
from .managers import UserManager

class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(null=True, blank=True, max_length=50)
    full_name = models.CharField('full name', max_length=100)
    email = models.EmailField('email account', unique=True)
    is_active = models.BooleanField('is_active', default=False)
    is_verified = models.BooleanField('is_verified', default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = ("Пользователь")
        verbose_name_plural = ("Пользователи")

    groups = models.ManyToManyField(
            Group,
            verbose_name=('groups'),
            blank=True,
            related_name='customuser_set',
            help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.')
        )
    user_permissions = models.ManyToManyField(
            Permission,
            verbose_name=('user permissions'),
            blank=True,
            related_name='customuser_set',
            help_text=('Specific permissions for this user.')
        )
    





