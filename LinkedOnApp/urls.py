from django.urls import path
from LinkedOnApp import views

app_name = 'LinkedOn'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('categories/', views.categories, name='categories'),
    path('categories/joblisting/', views.joblisting, name='joblistings'),
    path('categories/profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),

]