from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
class RegisterView(View):
    def get(self, request):
        form= UserRegisterForm()
        return render(request, 'account/register.html',{'form':form})

    def post(self, request):
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            datas=form.cleaned_data
            User.objects.create_user(datas["username"],datas["password"],datas["email"])
            messages.success(request,"your registered successfully","success")
            return redirect('home/home.html')
        return render(request, 'account/register.html')
