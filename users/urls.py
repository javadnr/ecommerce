from django.urls import path
from .views import home
from django.contrib.auth import views

urlpatterns = [
    path('',home.as_view(),name='home'),
]
