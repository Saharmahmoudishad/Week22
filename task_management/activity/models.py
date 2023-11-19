from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from home.models import Category,Staff

# Create your models here.
class Project(models.Model):
    Title = models.CharField(max_length=50) 
    staffs = models.ManyToManyField(Staff,related_name='project')
    categories = models.ManyToManyField(Category,related_name='project')
    contracting_party = models.CharField(max_length=50) 
    started = models.DateTimeField() 
    deadline = models.DateTimeField()
    Work_in_progress_percentage = models.DecimalField(max_digits=3,decimal_places=2, default=0.0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    Delay = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits= 20,decimal_places=3)

    
