from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is required')
        if not username:
            raise ValueError('Username is required')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        super_user = self.create_user(email, username, password, **extra_fields)
        super_user.is_staff = True
        super_user.is_superuser = True
        super_user.save(using=self._db)
        return super_user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=250, unique=True,
        verbose_name='email address'
    )
    username = models.CharField(max_length=100, verbose_name='username')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Additional fields for health survey
    age_range = models.CharField(max_length=20, blank=True)
    health_condition = models.CharField(max_length=10, blank=True)
    specify_condition = models.CharField(max_length=255, blank=True)
    dietary_preferences = models.CharField(max_length=50, blank=True)
    food_allergies = models.CharField(max_length=10, blank=True)
    specify_allergies = models.CharField(max_length=255, blank=True)
    fitness_level = models.CharField(max_length=50, blank=True)
    preferred_sports = models.CharField(max_length=50, blank=True)
    height = models.FloatField(null=True, blank=True, verbose_name='height (cm)')
    weight = models.FloatField(null=True, blank=True, verbose_name='weight (kg)')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username