from LinkedOnApp.models import Category
from django.shortcuts import render
from LinkedOnApp.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
import math


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
        print(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            plain_text_password = user.password
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            print(request.POST, request.POST.get('button', ['off']), request.POST.get('button', ['off']) == ['on'])
            # profile.isEmployer = request.POST.get('employer', ['off']) == ['on']

            if 'profileImage' in request.FILES:
                profile.profileImage = request.FILES['profileImage']
            profile.save()

            if attempt_login(request, user.username, plain_text_password):
                return redirect(reverse('LinkedOn:index'))
            else:
                return redirect(reverse('LinkedOn:signin'))

    context_dic = {"categories": Category.objects.all()}
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

    # returns
    return render(request, 'LinkedOn/categories.html', context_dic)


@login_required
def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None

    return render(request, 'LinkedOn/show_category.html')


@login_required
def joblistings(request):
    return render(request, 'LinkedOn/joblisting.html')


@login_required
def profiles(request):
    return render(request, 'LinkedOn/profile.html')


def attempt_login(request, username, password):
    user_auth = authenticate(username=username, password=password)
    if user_auth and user_auth.is_active:
        login(request, user_auth)
        return True

    return False
