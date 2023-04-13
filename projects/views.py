from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.

projectList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'This was a project where I built out my portfolio'
    },
    
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open source project I am still working on it'
    },
]

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
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project': projectObj, 'tags': tags})
