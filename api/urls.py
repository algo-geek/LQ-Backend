from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints, name="endpoints"),
    path('profiles/', views.profiles, name="profiles"),


    # social media urls start here

    path('socialmedia/all-posts/', views.all_posts, name="all_posts"),
    path('socialmedia/all-happies/', views.all_happies, name="all_happies")

    # social medial urls end here
]