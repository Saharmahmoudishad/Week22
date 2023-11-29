from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about_us/', views.AboutUsView.as_view(), name='about_us'),
     path('contact_us/', views.ContactUsView.as_view(), name='contact_us'),
    path('profile/<int:user_id>', views.ProfileUpdateView.as_view(), name='ProfileUpdate'),
    path('profile/<str:title>', views.CategoryDetailView.as_view(), name='categorydetail'),
    path('profile', views.StaffPdetailView.as_view(), name='staffpdetail'),
    path('delete/<int:user_id>', views.StaffDeleteView.as_view(), name='staffdelete'),
]