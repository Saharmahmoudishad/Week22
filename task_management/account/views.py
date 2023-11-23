from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


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
            User.objects.create_user(datas["username"], datas["password"], datas["email"])
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
            user = authenticate(request, username=datas["username"], password=datas["password"])
            if user is not None:
                login(request, user)
                messages.success(request, f"welcome to Ada company {datas['username']}", "success")
                return redirect('home:home')
            messages.warning(request, f"Please register in Ada company sit", "warning")
        return self.get(request)


class UserLogoutView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        messages.success(request, "you log out successfully ", "success")
        return redirect("home:home")
