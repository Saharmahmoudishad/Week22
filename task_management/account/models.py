from django.apps import apps
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin

# Create your models here.




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
        return f"{self.email}_{self.nationalcode}" 

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
    def has_category_permission(self, target_user):

        if not self.is_active or self.is_anonymous:
            return False

        user_category = self.staff.categories.title.lower()
        target_user_category = target_user.staff.categories.title.lower()

        if user_category == "project management":
            # Project Management category has access to all staff profiles
            return True
        elif user_category == "data processing":
            # Data Processing category has access to Survey Operations profiles only
            return target_user_category == "survey operations"
        elif user_category == "research and development":
            # Research and Development has access to Data Processing and Survey Operations profiles
            return target_user_category in ["data processing", "survey operations"]
        return False
    
class LoginRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    login_count = models.PositiveIntegerField(default=0)
    
