import django.contrib.auth
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Main page
    path('login/', views.login, name='login'),  # Main page
    path('logout/', views.logout_user, name='logout'),  # Main page
    path('registration/', views.registration, name='registration'),  # Registration page


    path('testCreation/', views.test_creation, name='test_creation'),  # Registration page
]
