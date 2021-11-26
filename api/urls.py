from django.urls import path
from . import views

urlpatterns = [
    path('auth/register-user/', views.register_user, name="register_user"),


    path('', views.endpoints, name="endpoints"),
    path('profiles/', views.profiles, name="profiles"),


    # social media urls start here

    path('socialmedia/all-posts/', views.all_posts, name="all_posts"),
    path('socialmedia/all-happies/', views.all_happies, name="all_happies"),
    path('socialmedia/add-post/', views.add_post, name="add_post"),
    path('socialmedia/add-happy/', views.add_happy, name="add_happy"),
    path('socialmedia/modify-post/<int:id>/',views.modify_post, name="modify_post"),
    path('socialmedia/comments/', views.comments, name="comments"),
    path('socialmedia/add-comment/', views.add_comment, name="add_comment"),

    # social medial urls end here


    # learning portal urls start here 
    
    path('news/', views.news, name="news"),
    path('laws/', views.laws, name="laws"),
    path('unaware/', views.unaware, name="unaware"),
    path('sub_category/', views.sub_category, name="sub_category"),

    # learning portal urls end here 



    # job portal starts here
    path('job-portal/all-jobs/', views.all_jobs, name="all_jobs"),
    path('job-portal/filtered-jobs/<str:category>/', views.filtered_jobs, name="filtered_jobs"),
    path("job-portal/job/<int:id>/", views.job, name="job"),
    path('job-portal/job-categories/', views.job_categories, name="job_categories"),

    # job portal ends here
]