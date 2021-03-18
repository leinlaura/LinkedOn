from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = render(request, 'LinkedOn/index.html')
    return response
    
def signin(request):
    return render(request, 'LinkedOn/signin.html')
    
def signup(request):
    return render(request, 'LinkedOn/signup.html')

    