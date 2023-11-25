from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "specialscolor"}), max_length=150,
                               help_text=(
                                   "Required max 50 & min 7 letter(using both uppercase and lowercase) and digits,"
                                   "acually  with no spaces or special characters &,=,-,',+,,, <,>, or ."),
                               validators=[UnicodeUsernameValidator()],
                               error_messages={
                                   'unique': "A user with that username already exists.",
                               }, )
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "specialscolor"}))
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput(attrs={"class": "specialscolor"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "specialscolor"}),
                             help_text="Please enter a valid email address.", )
    # nationalcode = forms.IntegerField(help_text="Please enter a valid NationalCode")
    # adress = forms.CharField(widget=forms.Textarea(attrs={"class": "specialscolor"}))

    # validators = [UnicodeUsernameValidator()],

    def clean_email(self):
        email_input = self.cleaned_data["email"]
        validator = RegexValidator(
            "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:["
            "a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
        user = User.objects.filter(email=email_input).exists()
        try:
            validator(email_input)
            if user:
                self.add_error("email", "this email is alreadly exists")
        except ValidationError:
            self.add_error("email", "Invalid email format")
        return email_input
    
    def clean_nationalcode(self):
        nationalcode =self.cleaned_data["nationalcode"]
        if nationalcode:
            user = User.objects.filter(nationalcode=nationalcode).exists()
            if user:
                self.add_error("username", "this username is already exists")
            return nationalcode
        return "plese enter your national code"

    def clean_username(self):
        username = self.cleaned_data["username"]
        user = User.objects.filter(username=username).exists()
        if user:
            self.add_error("username", "this username is already exists")
        return username

    def clean(self):
        datas = super().clean()
        p1 = datas.get("password")
        p2 = datas.get("password2")
        if p1 and p2 and p1 != p2:
            self.add_error('password2', "your confirm password and password does not match")


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "specialscolor", "autocomplete": "off"}),
                               max_length=150, )
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "specialscolor", "autocomplete": "off"}),
                               help_text="forgot your "
                                         "password", )
