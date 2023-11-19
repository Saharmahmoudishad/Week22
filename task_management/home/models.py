from django.db import models


# Create your models here.
class Staff(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    expert = models.CharField(max_length=50) 
    experience = models.IntegerField()
    
    

class Category(models.Model):
    title = models.CharField(max_length=50)
    employe_rewards = models.CharField(max_length=250, choices=[("To","Time off"),("G","Gifts"),("WH","Work from home days"),("Gc","Gift cards"),("C","Certificates")],default="None")
    staffs =models.ForeignKey(Staff,on_delete=models.CASCADE,related_name='category')


