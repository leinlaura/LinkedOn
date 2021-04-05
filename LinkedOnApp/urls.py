from django.urls import path
from LinkedOnApp import views

app_name = 'LinkedOn'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signup/checkusername', views.check_username, name="check_username"),
    path('signin/', views.signin, name='signin'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('categories/', views.categories, name='categories'),
    path('categories/joblistings/createjoblisting/', views.create_joblisting, name='create_joblisting'),
    path('categories/joblistings/', views.joblistings, name='joblistings'),
    path('categories/profiles/', views.profiles, name='profiles'),
    path('categories/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('categories/profiles/<user_id>/', views.show_profile, name='show_profile'),
    path('categories/joblistings/<job_id>/', views.show_joblisting, name='show_joblisting'),
    path('logout/', views.user_logout, name='logout'),
    path('editprofile/', views.edit_profile, name='edit_profile'),
    path('settings/', views.settings, name='settings'),
    path('settings/change_password/', views.PasswordsChangeView.as_view(template_name='LinkedOn/change_password.html'), name='change_password'),
    path('settings/delete_acc/', views.delete_acc, name='delete_acc'),

]
