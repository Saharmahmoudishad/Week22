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
    
class StaffProfileView(View):
    staff_form=StaffForm
    template_name="home/staffprofile.html"
    
    def get(self, request, user_id):
        staff=Staff.objects.get(user_id=user_id)
        form=StaffForm(instance=staff)
        return render(request,self.template_name,{'form':form})

    def post(self, request,user_id):
        staff=Staff.objects.get(user_id=user_id)
        staff_form = self.staff_form(request.POST,instance=staff)
        if staff_form.is_valid():
            print(1)
            staff_form.save()
            print(1)
            messages.success(request, f"update successfully", "success")
            return redirect("home:home")
        else:
            messages.warning(request,"check your input data","warning")


            

