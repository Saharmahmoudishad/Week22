from django import forms
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['firstname', 'lastname', 'expert', 'experience', 'user', 'categories','profile_image']