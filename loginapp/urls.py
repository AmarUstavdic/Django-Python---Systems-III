from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('loggedin/', login_required(views.profile_view), name='logged_in'),
    path('register/', views.register, name='register'),
    ]

# need to insert name of the URL
