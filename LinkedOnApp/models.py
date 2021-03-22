from django.db import models
from django.contrib.auth.models import User
    
class UserProfile(models.Model):
    ABOUT_MAX_LENGTH = 1000
    SEARCHING_MAX_LENGTH = 1000
    WEBSITE_MAX_LENGTH = 128
    
    #user includes username, password, email, firstname, lastname.
    #Could have users input their email as the 'username'
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    #category : still figuring this out. will get back to it
    website = models.CharField(max_length=WEBSITE_MAX_LENGTH, blank=True)
    about = models.CharField(max_length=ABOUT_MAX_LENGTH, blank=True)
    searchingInfo = models.CharField(max_length=SEARCHING_MAX_LENGTH, blank=True)
    profileImage = models.ImageField(blank=True)
    isEmployer = models.BooleanField()
    
    def __str__(self):
        return self.user.username
    
class JobListing(models.Model):
    ID_MAX_LENGTH = 128
    DESCRIPTION_MAX_LENGTH = 1000
    
    job_id = models.CharField(max_length=ID_MAX_LENGTH, unique=True)
    employer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)
    
    def __str__(self):
        return self.job_id
        
class Category(models.Model):
    NAME_MAX_LENGTH = 128
    
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    
    def __str__(self):
        return self.name
    
