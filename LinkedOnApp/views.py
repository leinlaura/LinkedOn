from django.shortcuts import render
from LinkedOnApp.forms import UserForm, UserProfileForm


def index(request):
    return render(request, 'LinkedOn/index.html')


def signin(request):
    return render(request, 'LinkedOn/signin.html')


def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.user_name = user.email
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profileImage' in request.FILES:
                profile.profileImage = request.FILES['profileImage']

            profile.save()

    return render(request, 'LinkedOn/signup.html')


def aboutus(request):
    return render(request, 'LinkedOn/aboutus.html')


def categories(request):
    return render(request, 'LinkedOn/categories.html')


def joblisting(request):
    return render(request, 'LinkedOn/joblisting.html')


def profile(request):
    return render(request, 'LinkedOn/profile.html')
