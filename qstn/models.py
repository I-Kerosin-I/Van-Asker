from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class StudentManager(BaseUserManager):
    def create_user(self, login, password=None, **extra_fields):
        if not login:
            raise ValueError('Login is required')
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(login, password, **extra_fields)


class Student(AbstractBaseUser):
    login = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True, null=True)
    birth = models.DateField()
    educational_institution = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = StudentManager()

    USERNAME_FIELD = 'login'  # Используем email в качестве уникального идентификатора
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'birth', 'educational_institution']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
