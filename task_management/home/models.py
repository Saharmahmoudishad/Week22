from django.db import models
from account.models import CustomUser
import os, uuid


# def user_image_file_path(instance, filename: str):
#     """generate file path for user profile image"""
#     ext = filename.split('.')[-1]
#     filename = f'{uuid.uuid4()}.{ext}'
#     return os.path.join('uploads/user/', filename)


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    employe_rewards = models.CharField(max_length=250,
                                       choices=[("To", "Time off"), ("G", "Gifts"), ("WH", "Work from home days"),
                                                ("Gc", "Gift cards"), ("C", "Certificates")], default="None")

    def __str__(self):
        return f"{self.title}"


class Staff(models.Model):
    firstname = models.CharField(max_length=50, null=True, default=None)
    lastname = models.CharField(max_length=50, null=True, default=None)
    expert = models.CharField(max_length=50, null=True, default=None)
    experience = models.IntegerField(null=True, default=None)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='staff', null=True, default=None)
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} in {self.categories.title}"
