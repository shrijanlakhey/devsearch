from django.shortcuts import render
from . models import Profile
# Create your views here.


def profiles(request):
    profiles = Profile.objects.all() # getting all the profiles from the db
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)