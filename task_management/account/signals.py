from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from account.models import CustomUser, LoginRecord
from home.models import Staff

@receiver(user_logged_in)
def record_login(sender, request, user, **kwargs):
    try:
        login_record = LoginRecord.objects.get(user=user)
        login_record.login_count += 1
        login_record.save()
    except LoginRecord.DoesNotExist:
        LoginRecord.objects.create(user=user, login_count=1)

User = get_user_model()
@receiver(post_save, sender=CustomUser)
def create_staffprofile(sender, instance, created, **kwargs):
    
    if created:
        Staff.objects.create(user=instance)