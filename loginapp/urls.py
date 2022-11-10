from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('', views.profile_view, name='logged_in'),
    path('register/', views.register, name='register'),
    ]

# need to insert name of the URL
