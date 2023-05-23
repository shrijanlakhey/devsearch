from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from .forms import CustomUserCreationForm
# Create your views here.


def loginUser(request):
    page = 'login'
    # redirects the user to profile page if he is logged in and he cannot access login page
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == "POST":
        # print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        # takes in the username and password and makes sure that the password matches username and return back either user instance or none
        user = authenticate(request, username=username, password=password)

        # if user exists
        if user is not None:
            # this method will create a session for the user in the db and also add that into the browsers cookies
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or password was incorrect")
    context = {
        'page': page,
    }
    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    logout(request)  # delete the session
    messages.error(request, "User was logged out")
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        # passing the data retrieved from the form
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # creating an instance of the user or the CustomUserCreationForm()
            # 'commit = False' will not save the form right away, it will hold a temporarily instance of it so that we can further make changes to the data retrieved like below then only save it io the db
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()  # finally saving the data to the db

            messages.success(request, 'User account was created!')

            # this method will create a session for the user in the db and also add that into the browsers cookies
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'An error has occurred during registration!')
    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'users/login_register.html', context)


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
