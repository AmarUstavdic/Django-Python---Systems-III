from django.urls import path
from . import views

urlpatterns = [
    path('', views.createUserView, name='register'),
    ]

# need to insert name of the URL
