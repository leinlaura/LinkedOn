from LinkedOnApp.models import Category, UserProfile, JobListing, User
from LinkedOnApp.forms import UserForm, UserProfileForm, UserUpdateForm, UserProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from LinkedOnApp.search_bing import run_query
import math
import uuid


def index(request):
    return render(request, 'LinkedOn/index.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if attempt_login(request, username, password):

            return redirect(reverse('LinkedOn:index'))
        else:
            print(f"Invalid login details:{username}, {password}")
            render(request, 'LinkedOn/signin.html', {"error": "Wrong email or password"})

    return render(request, 'LinkedOn/signin.html')


def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            plain_text_password = user.password
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.isEmployer = request.POST.get('isEmployer', '[\'off\']') == 'on'

            try:
                category = Category.objects.get(name=request.POST.get('category'))
                profile.category = category
            except ObjectDoesNotExist:
                pass

            if 'profileImage' in request.FILES:
                profile.profileImage = request.FILES['profileImage']
            profile.save()

            if attempt_login(request, user.username, plain_text_password):
                return redirect(reverse('LinkedOn:index'))
            else:
                return redirect(reverse('LinkedOn:signin'))
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dic = {"categories": Category.objects.all(),
                   "COMPANY_MAX_LENGTH": UserProfile.COMPANY_MAX_LENGTH,
                   "WEBSITE_MAX_LENGTH": UserProfile.WEBSITE_MAX_LENGTH,
                   "ABOUT_MAX_LENGTH": UserProfile.ABOUT_MAX_LENGTH,
                   "SEARCHING_MAX_LENGTH": UserProfile.SEARCHING_MAX_LENGTH,
                   "user_form": user_form,
                   "profile_form": profile_form,
                   }

    return render(request, 'LinkedOn/signup.html', context_dic)


def user_logout(request):
    logout(request)
    return redirect(reverse('LinkedOn:index'))


def aboutus(request):
    return render(request, 'LinkedOn/aboutus.html')


def categories(request):
    context_dic = {}
    categories = Category.objects.all()  # get all categories
    categories_length = Category.objects.all().count()  # get length of categories

    # there will be three columns and hence they are divided by 3
    length_of_col = math.floor(categories_length / 3)

    # three colummns
    context_dic["first_col"] = categories[:length_of_col]
    context_dic["second_col"] = categories[length_of_col:2 * length_of_col]
    context_dic["third_col"] = categories[2 * length_of_col:]
    
    if request.method == "POST":
        query_name = request.POST.get('name', None).strip()
        if query_name:
            categories = Category.objects.filter(name__contains=query_name)
            joblistings = JobListing.objects.filter(description__contains=query_name)
           # profiles = UserProfile.objects.filter(user.first_name ==query_name).union(UserProfile.objects.filter(user.last_name==query_name))
            context_dic["categories"] = categories
            context_dic["joblistings"] = joblistings
            context_dic["profiles"] = profiles
            context_dic["boolean"] = True
         
    
    # returns
    return render(request, 'LinkedOn/categories.html', context_dic)


@login_required
def show_category(request, category_name_slug):
    context_dic = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dic['category'] = category
        # get profiles where the category matches and they are not employers
        profiles = UserProfile.objects.filter(category=category, isEmployer=False)
        context_dic["profiles"] = profiles

    except Category.DoesNotExist:
        context_dic['category'] = None
        context_dic["profiles"] = None

    return render(request, 'LinkedOn/show_category.html', context_dic)


@login_required
def joblistings(request):
    context_dic = {}
    try:
        joblistings = JobListing.objects.all()
        context_dic["joblistings"] = joblistings
        currentUser = UserProfile.objects.get(user=request.user)
        context_dic["currentUser"] = currentUser  # get current user to check if they are an employer

    except UserProfile.DoesNotExist:
        context_dic["currentUser"] = None

    return render(request, 'LinkedOn/joblistings.html', context_dic)


@login_required
def profiles(request):
    profiles = UserProfile.objects.filter(isEmployer=False)  # filter profiles to jobseekers and active users
    context_dic = {}
    context_dic["profiles"] = profiles
    return render(request, 'LinkedOn/profiles.html', context_dic)


@login_required
def show_profile(request, profile_id):
    context_dict = {}
    try:
        profile = UserProfile.objects.get(id=profile_id)
        context_dict["profile"] = profile

    except UserProfile.DoesNotExist:
        context_dict["profile"] = None

    return render(request, 'LinkedOn/show_profile.html', context_dict)


@login_required
def show_joblisting(request, job_id):
    context_dic = {}
    try:
        job = JobListing.objects.get(id=job_id)
        context_dic["job"] = job

    except JobListing.DoesNotExist:
        context_dic["job"] = None

    return render(request, 'LinkedOn/show_joblisting.html', context_dic)


@login_required
def create_joblisting(request):
    currentUser = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        description = request.POST['description']
        category = Category.objects.get(name=request.POST.get('category'))
        employer = currentUser
        joblisting = JobListing(job_id=uuid.uuid4(), description=description, 
                                category=category, employer=employer)
        joblisting.save()

    return render(request, 'LinkedOn/create_joblisting.html', {"categories": Category.objects.all()})


def check_username(request):
    return JsonResponse({"unique": not User.objects.filter(username=request.GET.get('username', '')).exists()})


def attempt_login(request, username, password):
    user_auth = authenticate(username=username, password=password)
    if user_auth and user_auth.is_active:
        login(request, user_auth)
        return True

    return False


@login_required
def edit_profile(request):
    currentUser = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        profile_form = UserProfileUpdateForm(request.POST)
        if profile_form.is_valid():
            currentUser.user.first_name = request.POST['first_name']
            currentUser.user.last_name = request.POST['last_name']
            currentUser.user.save()

            currentUser.website = request.POST['website']
            if currentUser.isEmployer == True:
                currentUser.company = request.POST['company']
            else:
                currentUser.about = request.POST['about']
                currentUser.searchingInfo = request.POST['searchingInfo']

            try:
                category = Category.objects.get(name=request.POST.get('category'))
                currentUser.category = category
            except ObjectDoesNotExist:
                pass

            if 'profileImage' in request.FILES:
                currentUser.profileImage = request.FILES['profileImage']
            currentUser.save()

            return redirect('/')

    context_dic = {"categories": Category.objects.all(),
                   "COMPANY_MAX_LENGTH": UserProfile.COMPANY_MAX_LENGTH,
                   "WEBSITE_MAX_LENGTH": UserProfile.WEBSITE_MAX_LENGTH,
                   "ABOUT_MAX_LENGTH": UserProfile.ABOUT_MAX_LENGTH,
                   "SEARCHING_MAX_LENGTH": UserProfile.SEARCHING_MAX_LENGTH,
                   "currentUser": currentUser,
                   }
    return render(request, 'LinkedOn/edit_profile.html', context_dic)

@login_required
def settings(request):
    return render(request, 'LinkedOn/settings.html')

@login_required
def delete_acc(request):
    user = request.user
    user.delete()
    user.save()
    
    return render(request, 'LinkedOn/delete_acc.html')
    
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('index')
    

    


