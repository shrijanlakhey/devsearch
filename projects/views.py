from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

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


# a decorator that lets user access this age only if they are logged in and send them to the login page if they are not logged in
@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        # request.FILES is getting those files/images sent
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form, }
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    # instead of rendering a form, we are gonna take an instance, it is gonna pre-fill all the form fields of that projects data
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        # letting django know which project is being updated
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form, }
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)
