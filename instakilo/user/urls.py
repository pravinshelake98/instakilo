from django.contrib import admin
from django.urls import path

from user.views import Login , RegistrationView

urlpatterns = [
    path("login/",Login.as_view() ) ,
    path("register/",RegistrationView.as_view())

]