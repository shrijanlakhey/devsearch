from django.shortcuts import render
from . models import Profile
# Create your views here.


def profiles(request):
    profiles = Profile.objects.all() # getting all the profiles from the db
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request,pk):
    profile = Profile.objects.get(id=pk) # get method gets back a single object
    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context)