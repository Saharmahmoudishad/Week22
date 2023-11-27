from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import CustomUser
from django.http import HttpResponseRedirect
import hashlib


# Create your views here.
class UserRegisterView(View):
    form_user = UserRegisterForm
    template_name = 'account/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_user()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_user(request.POST)
        if form.is_valid():
            datas = form.cleaned_data
            CustomUser.objects.create_user(
                nationalcode=datas["nationalcode"],
                email=datas["email"],
                date_of_birth=datas["date_of_birth"],
                adress=datas["adress"],
                password=datas["password"]
            )
            messages.success(request, "your registered successfully", "success")
            return redirect('account:User_register')
        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_login = UserLoginForm
    template_name = 'account/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_login()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        log = self.form_login(request.POST)
        if log.is_valid():
            datas = log.cleaned_data
            user = authenticate(request, username=datas["nationalcode"], password=datas["password"])
            if user is not None:
                login(request, user)
                return self.setcookie(request,datas["nationalcode"])
        messages.warning(request, f"Please enter correct nationalcode or email and password or Please register in Ada company site first before login", "warning")
        return self.get(request)
    
    @staticmethod
    def setcookie(request,name):
        hashed_name = hashlib.sha256(name.encode()).hexdigest()
        url=reverse("home:home")
        html = HttpResponseRedirect(url)
        if request.COOKIES.get(hashed_name):
            value = int(request.COOKIES.get(hashed_name))
            html.set_cookie(hashed_name, value + 1, max_age=84600)
            messages.success(request, f"welcome back to Ada company {name}", "success")
        else:
            value = 1
            html.set_cookie(hashed_name, value,max_age=84600)
            messages.success(request, f"welcome to Ada company {name} for first time", "success")
        return html

class UserLogoutView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        messages.success(request, "you log out successfully ", "success")
        return redirect("home:home")

