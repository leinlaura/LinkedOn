from django.shortcuts import render
from django.http import HttpResponse
from LinkedOnApp.forms import UserForm, UserProfileForm

def index(request):
    return render(request, 'LinkedOn/index.html')
    
def signin(request):
    return render(request, 'LinkedOn/signin.html')
    
def signup(request):
    registered = False; #set registered to false
    
    #if it is a HTTP POST, we're interesting in processing form data
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            #hash the password 
            user.set_password(user.password)
            user.save()
            
            #until we're ready to avoid integrity problems
            profile = profile_form.save(commit=False)
            profile.user = user
            
            #if user provided a picture we need to get it from the input form
            #and put it in the UserProfile model
            if 'profileImage' in request.FILES:
                profile.picture = request.FILES['profileImage']
                
            profile.save()
            
            registered = True
            
        else:
            #invalid form or forms - print problems to the terminal
            print(user_form.errors, profile_form.errors)
            
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    context_dic = {'user_form': user_form, 'profile_form': profile_form, 'registered' : registered}
    return render(request, 'LinkedOn/signup.html', context_dic)
    
def aboutus(request):
    return render(request, 'LinkedOn/aboutus.html')
    
def categories(request):
    return render(request, 'LinkedOn/categories.html')
    
def joblisting(request):
    return render(request, 'LinkedOn/joblisting.html')
    
def profile(request):
    return render(request, 'LinkedOn/profile.html')
    

    