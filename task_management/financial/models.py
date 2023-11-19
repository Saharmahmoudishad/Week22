from django.db import models
from home.models import Staff

# Create your models here.
class PaySlip (models.Model):
    staffs = models.ForeignKey(Staff,on_delete=models.CASCADE,related_name='payslip')
    overtime = models.IntegerField()
    FinancialReward = models.DecimalField(max_digits= 20,decimal_places=3) 
    tax = models.DecimalField(max_digits= 20,decimal_places=3)
    salary = models.DecimalField(max_digits= 20,decimal_places=3)
