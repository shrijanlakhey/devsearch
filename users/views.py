from django.shortcuts import render
from . models import Profile
# Create your views here.


def profiles(request):
    profiles = Profile.objects.all()  # getting all the profiles from the db
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    # get method gets back a single object
    profile = Profile.objects.get(id=pk)
    # if skill does not have any description or is blank, it will be excluded
    topSkills = profile.skill_set.exclude(description__exact="")
    # if skill has an empty string or blank as a description, it will be selected
    othrtSkills = profile.skill_set.filter(description="")
    context = {'profile': profile,
               'topSkills': topSkills,
               'otherSkills': othrtSkills,
               }
    return render(request, 'users/user-profile.html', context)
