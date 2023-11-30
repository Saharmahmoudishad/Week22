from django.db import models
from home.models import Staff, Category


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50, unique=True)
    constracting_party = models.CharField(max_length=50, null=True, default=None)
    work_in_progress = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    started = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True, default="1300-01-01")
    delay = models.DateField(null=True,blank=True)
    cost = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    category = models.ManyToManyField(Category, related_name='Project', default=None)
    staff = models.ManyToManyField(Staff, related_name='Project', default=None)

    def __str__(self):
        return f"{self.title} started at {self.started}_{self.work_in_progress}"
