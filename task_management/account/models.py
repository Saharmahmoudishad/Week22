from django.db import models
from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# # Create your models here.
# class CustomUser(AbstractUser):
#     nationalcode=models.IntegerField(unique=True,default=1234)
#     adress=models.TextField()

#     USERNAME_FIELD="nationalcode"
#     REQUIRED_FIELDS=[]




# class CustomUser(AbstractBaseUser):
#     identifier = models.CharField(max_length=40, unique=True)
#     date_of_birth = models.DateField()
#     height = models.FloatField()

#     USERNAME_FIELD = "identifier"

#     REQUIRED_FIELDS = ["date_of_birth", "height"]
# class CustomUserManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, nationatlcode, email, password, **extra_fields):
#         """
#         Create and save a user with the nationatlcode, email, and password.
#         """
#         if not nationatlcode:
#             raise ValueError("The given nationatlcode must be valid")
#         email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        # GlobalUserModel = apps.get_model(
        #     self.model._meta.app_label, self.model._meta.object_name
        # )
        # username = GlobalUserModel.normalize_username(username)
    #     user = self.model(nationatlcode=nationatlcode, email=email, **extra_fields)
    #     user.password = make_password(password)
    #     user.save(using=self._db)
    #     return user

    # def create_user(self, nationatlcode, email=None, password=None, **extra_fields):
    #     extra_fields.setdefault("is_staff", False)
    #     extra_fields.setdefault("is_superuser", False)
    #     return self._create_user(nationatlcode, email, password, **extra_fields)

    # def create_superuser(self, nationatlcode, email=None, password=None, **extra_fields):
    #     extra_fields.setdefault("is_staff", True)
    #     extra_fields.setdefault("is_superuser", True)

    #     if extra_fields.get("is_staff") is not True:
    #         raise ValueError("Superuser must have is_staff=True.")
    #     if extra_fields.get("is_superuser") is not True:
    #         raise ValueError("Superuser must have is_superuser=True.")

    #     return self._create_user(nationatlcode, email, password, **extra_fields)




from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, nationatlcode, email, date_of_birth, adress, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not nationatlcode or not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            nationatlcode=nationatlcode,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            adress=adress
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nationatlcode, email, date_of_birth, adress, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            nationatlcode,
            email,
            password=password,
            date_of_birth=date_of_birth,
            adress=adress,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
    )
    nationatlcode = models.CharField(max_length=40, unique=True)
    adress = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "nationatlcode"
    REQUIRED_FIELDS = ["date_of_birth","adress","email"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    
