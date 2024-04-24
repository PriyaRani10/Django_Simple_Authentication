from django.contrib import admin
from django.urls import path,include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from .views import RegisterView, LoginView, LogoutView, UserView
urlpatterns = [
    path('register', RegisterView.as_view()),  #for register the user 1st time
    path('login', LoginView.as_view()),     # for log in purpose
    path('logout', LogoutView.as_view()), # for logout purpose
    path('userList', UserView.as_view()), # to view all the register users
]