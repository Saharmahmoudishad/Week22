from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('profile/<int:user_id>', views.StaffProfileView.as_view(), name='staffprofile'),
]