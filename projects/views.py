from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
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
    projectObj = Project.objects.get(id = pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})

def createProject(request):
    context = {}
    return render(request, 'projects/project_form.html')
