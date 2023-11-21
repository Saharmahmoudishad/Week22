from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
class RegisterView(View):
    form_user=UserRegisterForm
    def get(self, request):
        form= self.form_user()
        return render(request, 'account/register.html',{'form':form})

    def post(self, request):
        form=self.form_user(request.POST)
        if form.is_valid():
            datas=form.cleaned_data
            print(datas)
            User.objects.create_user(datas["username"], datas["password"], datas["email"])
            messages.success(request,"your registered successfully","success")
            return redirect('home:home')
        return render(request, 'account/register.html',{'form':form})
