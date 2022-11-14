from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


# these are the urls that redirect to the function that actually runs the application
router = DefaultRouter()
router.register('users', views.user_view_set)

urlpatterns = [
    path('', include(router.urls)),  # include the registred viwe
    # request a token for a username and password
    path('request_token/', obtain_auth_token),

]
