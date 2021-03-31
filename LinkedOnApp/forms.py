from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from LinkedOnApp.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'company', 'profileImage', 'about', 'searchingInfo', 'isEmployer',)
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password')


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'company', 'profileImage', 'about', 'searchingInfo',)
        

