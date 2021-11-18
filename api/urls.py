from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints, name="endpoints"),
    path('profiles/', views.profiles, name="profiles")
]