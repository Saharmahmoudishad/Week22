from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# # Create your models here.
# class CustomUser(AbstractUser):
#     nationalcode=models.IntegerField(unique=True,default=1234)
#     adress=models.TextField()

#     USERNAME_FIELD="nationalcode"
#     REQUIRED_FIELDS=[]


from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, nationalcode, email, date_of_birth="Y-m-d", adress=" ", password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not nationalcode or not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            nationalcode=nationalcode,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            adress=adress
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nationalcode, email, date_of_birth="1300-01-01", adress=" ", password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            nationalcode,
            email,
            password=password,
            date_of_birth=date_of_birth,
            adress=adress,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    nationalcode = models.CharField(
        max_length=40, unique=True)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
    )
    adress = models.CharField(max_length=40)
    date_of_birth = models.DateField(null=True, blank=True, default="1300-01-01")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "nationalcode"
    REQUIRED_FIELDS = ["email"]

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

    
