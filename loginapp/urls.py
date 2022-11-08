from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home_view, name='home'),
    ]

# need to insert name of the URL
