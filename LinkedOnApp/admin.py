from django.contrib import admin
from LinkedOnApp.models import UserProfile, JobListing, Category ##add userprofile

#admin.ste.register(User)
admin.site.register(UserProfile)
admin.site.register(JobListing)
admin.site.register(Category)
