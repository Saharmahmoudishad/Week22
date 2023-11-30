from django.shortcuts import render
from django.views import View
from .models import Project
from .forms import ProjectForm
from home.models import Category, Staff
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
class CategoryProjectView(View):
    template_name = 'activity/all_project.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_id = request.user.id
            return self.get(request, user_id)
        return super().dispatch(request, user_id=None, *args, **kwargs)

    def get(self, request, user_id):
        all_project = Project.objects.all()
        categories = Category.objects.all()
        context = {
            'all_project': all_project,
            'categories': categories,
        }
        if user_id:
            log_staff = get_object_or_404(Staff, user_id=user_id)
            context['log_staff_category'] = log_staff.categories
        return render(request, self.template_name, context)

    class ProjectUpdateView(View):
        template_name = "activity/project-update.html"
        project_form = ProjectForm

        def get(self, request, project_id):
            project = Project.objects.get(project_id=project_id)
            form = self.project_form(instance=project)
            return render(request, self.template_name, {'form': form})

        def post(self, request, project_id):
            project = Project.objects.get(project_id=project_id)
            form = self.project_form(request.POST, instance=project)
            if form.is_valid():
                form.save()
                messages.success(request, f"update successfully", "success")
                # return redirect("home:home")
                return HttpResponseRedirect(reverse('activity:all_project'))
            else:
                messages.warning(request, "check your input data", "warning")
            return render(request, self.template_name, {'form': form})


class ProjectUpdateView(View):
    template_name = "activity/project_update.html"
    project_form = ProjectForm

    def get(self, request, project_id=None):
        if project_id:
            project = Project.objects.get(id=project_id)
            form = self.project_form(instance=project)
        else:
            form = self.project_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, project_id=None):
        if project_id:
            project = Project.objects.get(id=project_id)
            form = self.project_form(request.POST, instance=project)
        else:
            form = self.project_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"update successfully", "success")
            # return redirect("home:home")
            return HttpResponseRedirect(reverse('activity:all_project'))
        else:
            messages.warning(request, "check your input data", "warning")
        return render(request, self.template_name, {'form': form})
