from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('profile/<int:user_id>', views.ProfileUpdateView.as_view(), name='ProfileUpdate'),
    path('profile/<str:title>', views.CategoryDetailView.as_view(), name='categorydetail'),
    path('profile', views.StaffPdetailView.as_view(), name='staffpdetail'),
]