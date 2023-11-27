from django.shortcuts import render,redirect
from django.views import View
from .models import Category,Staff
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import StaffForm


# Create your views here.
class HomeView(View):
    def get(self, request):
        # allcategory=Category.objects.values_list('title', flat=True).distinct()
        allcategory = Category.objects.all()
        return render(request, 'home/home.html', {"allcategory": allcategory})

    def post(self, request):
        return render(request, 'home/home.html')
    
class StaffProfileView(LoginRequiredMixin,View):
    staff_form=StaffForm
    def get(self, request, user_id):
        staff=Staff.objects.get(id=user_id)
        form=StaffForm(instance=staff)
        return render(request,"home:staffprofile",{'form':form})

    def post(self, request,user_id):
        staff_form = self.staff_form(request.POST)
        if staff_form.is_valid():
            staff_form.save()
            messages.success(request, f"update successfully", "success")
            return redirect("home:home")
        else:
            messages.warning(request,"check your input data","warning")


            

