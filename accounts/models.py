from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_superuser(self, email, password, first_name, last_name, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
        'SuperUser must be assigned to is_staff=True.'
        )

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
            'SuperUser must be assigned to is_superuser=True.'
        )

        return self.create_user(email, first_name, last_name, password, **other_fields)

    def create_user(self, email, first_name, last_name, password, **other_fields):
        if not email:
            raise ValueError('You must provide an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    mob = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        '''
        Returns the first name and the last name together with a space
        '''
        fullname = self.first_name + " " + self.last_name
        return fullname

    def get_short_name(self):
        '''
        Returns the short name of the user
        '''
        return self.first_name

    def __str__(self):
        return self.first_name
