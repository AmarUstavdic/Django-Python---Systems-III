from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    ]

# need to insert name of the URL
