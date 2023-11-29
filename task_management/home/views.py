from django.shortcuts import render,redirect
from django.views import View
from .models import Category,Staff
from account.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import StaffForm
from account.models import CustomUser
from django.urls import reverse
from django.views.generic import TemplateView

# Create your views here.
class HomeView(View):
    def get(self, request):
        # allcategory=Category.objects.values_list('title', flat=True).distinct()
        allcategory = Category.objects.all()
        return render(request, 'home/home.html', {"allcategory": allcategory})

    def post(self, request):
        return render(request, 'home/home.html')
    
class StaffPdetailView(View):
    staff_form=StaffForm
    template_name="home/staffpdetail.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_id=request.user.id
            return self.get(request,user_id)
        return super().dispatch(request, *args, **kwargs)

    
    def get(self, request, user_id):
        if user_id:
            user= CustomUser.objects.get(id=user_id)
            staff = Staff.objects.get(user_id=user_id)
            context = {
             'user': user,
             'staff': staff,
            }
            return render(request,self.template_name,context)
        messages.warning(request,"your not access to staff of Ada company profile","warning")

        
        
    # def get(self, request, user_id):
    #     if request.user.is_authenticated:
    #         if request.user.has_category_permission(user_id):
    #             user= CustomUser.objects.get(id=user_id)
    #             staff = Staff.objects.get(user_id=user_id)
    #             context = {
    #              'user': user,
    #              'staff': staff,
    #             }
    #             return render(request,"home/staffdetail.html",context)
    #         staff=Staff.objects.get(user_id=user_id)
    #         form=StaffForm(instance=staff)
    #         return render(request,self.template_name,{'form':form})


class CategoryDetailView(View):
    
    def get(self, request,title):
        category = Category.objects.get(title=title)
        staffs = Staff.objects.filter(categories=category)
        context = {
            'category_name': category.title,
            'staffs': staffs,
            'user': request.user
        }
        return render(request, 'home/categorydetail.html', context)
    

class ProfileUpdateView(View):
    staff_form=StaffForm
    template_name="home/profileupdate.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_id=request.user.id
            return self.get(request,user_id)
        return super().dispatch(request, *args, **kwargs)
    

    def get(self, request, user_id):
        staff=Staff.objects.get(user_id=user_id)
        form=StaffForm(instance=staff)
        return render(request,self.template_name,{'form':form})
    
    def post(self, request,user_id):
        staff=Staff.objects.get(user_id=user_id)
        staff_form = self.staff_form(request.POST,instance=staff)
        if staff_form.is_valid():
            staff_form.save()
            messages.success(request, f"update successfully", "success")
            return redirect("home:home")
        else:
            messages.warning(request,"check your input data","warning")

            
class StaffDeleteView(View):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_id=request.user.id
            return self.get(request, user_id)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, user_id):
        staff=Staff.objects.get(user_id=user_id)
        print(1)
        title=staff.categories.title
        staff.delete() 
        print(1)
        url=reverse("home:categorydetail",args=[title])
        return redirect(url)
    

class AboutUsView(TemplateView):
    template_name = 'about_us.html'

class ContactUsView(TemplateView):
    template_name = 'contact_us.html'