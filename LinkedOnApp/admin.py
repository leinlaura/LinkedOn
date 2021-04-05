from django.contrib import admin
from LinkedOnApp.models import Category, UserProfile, JobListing


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)
admin.site.register(JobListing)
