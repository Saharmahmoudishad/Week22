from django.urls import path
from . import views

app_name = 'activity'
urlpatterns = [
    path('project/<int:project_id>', views.ProjectUpdateView.as_view(), name='project_update'),
path('project/add', views.ProjectUpdateView.as_view(), name='project_add'),
    path('project/', views.CategoryProjectView.as_view(), name='all_project'),

]
