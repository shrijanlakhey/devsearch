from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def projects(request):
    page = 'projects'
    return render(request, 'projects/projects.html', {'page':page})
    # message is the key and msg is the value

def project(request, pk):
    return render(request, 'projects/single-project.html')
