from django.shortcuts import render
from django.views import View
from .models import Category


# Create your views here.
class HomeView(View):
    def get(self, request):
        # allcategory=Category.objects.values_list('title', flat=True).distinct()
        allcategory = Category.objects.all()
        return render(request, 'home/home.html', {"allcategory": allcategory})

    def post(self, request):
        return render(request, 'home/home.html')
