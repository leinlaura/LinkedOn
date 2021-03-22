from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'LinkedOn/index.html')
    
def signin(request):
    return render(request, 'LinkedOn/signin.html')
    
def signup(request):
    return render(request, 'LinkedOn/signup.html')
    
def aboutus(request):
    return render(request, 'LinkedOn/aboutus.html')
    
def categories(request):
    return render(request, 'LinkedOn/categories.html')
    
def joblisting(request):
    return render(request, 'LinkedOn/joblisting.html')
    
def profile(request):
    return render(request, 'LinkedOn/profile.html')
    

    