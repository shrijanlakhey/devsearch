from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
# Create your views here.

# we access a dictonary's value in template by its key


def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'projects/projects.html', context)
    # message is the key and msg is the value


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form, }
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    # instead of rendering a form, we are gonna take an instance, it is gonna pre-fill all the form fields of that projects data
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project) # letting django know which project is being updated
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form, }
    return render(request, 'projects/project_form.html', context)
