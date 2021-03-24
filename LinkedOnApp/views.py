from LinkedOnApp.models import Category
from django.shortcuts import render
from django.http import HttpResponse
from LinkedOnApp.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect

def index(request):
    return render(request, 'LinkedOn/index.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('LinkedOn:index'))

            else:
                return HttpResponse("Your LinkedOn account is disabled.")

        else:
            print(f"Invalid login details:{username}, {password}")
            return HttpResponse("Invalid login details supplied.")

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
            
    context_dic = {}
    context_dic["categories"] = Category.objects.all()
    return render(request, 'LinkedOn/signup.html', context_dic)

def user_logout(request):
    logout(request)
    return redirect(reverse('LinkedOn:index'))

def aboutus(request):
    return render(request, 'LinkedOn/aboutus.html')


def categories(request):
    return render(request, 'LinkedOn/categories.html')


@login_required
def joblisting(request):
    return render(request, 'LinkedOn/joblisting.html')

@login_required
def profile(request):
    return render(request, 'LinkedOn/profile.html')
    
    
    
