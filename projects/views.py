from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def projects(request):
    msg = 'Hello, you are on the projects page'
    return render(request, 'projects/projects.html', {'message':msg})
    # message is the key and msg is the value

def project(request, pk):
    return render(request, 'projects/single-project.html')
