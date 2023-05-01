from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from . models import Profile
# Create your views here.


def loginPage(request):
    if request.method == "POST":
        # print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print("Username does not exist")

        # takes in the username and password and makes sure that the password matches username and return back either user instance or none
        user = authenticate(request, username=username, password=password)

        # if user exists
        if user is not None:
            # this method will create a session for the user in the db and also add that into the browsers cookies
            login(request, user)
            return redirect('profiles')
        else:
            print("Username or password was incorrect")
    return render(request, 'users/login_register.html')


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
