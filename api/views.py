from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from . models import (
    News,
    Profile, 
    SocialMediaPost,
    Happy,
    Laws,
    Category,
    Sub_Category,
    Comment,
    Job,
    JobCategory
)
from . serializers import (
    ProfileSerializer,
    SocialMediaPostSerializer,
    HappySerializer,
    UserSerializer,
    NewsSerializer,
    LawsSerializer,
    CategorySerializer,
    Sub_CategorySerializer,
    CommentSerializer,
    JobSerializer,
    JobCategorySerializer
)
from django.contrib.auth.models import User
import json

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    return Response({"message":"hello"})

@api_view(['GET'])
def profiles(request):
    profs = Profile.objects.all()
    serializer = ProfileSerializer(profs,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def register_user(request):
    data = request.data

    serializer = UserSerializer(data=data)
    print(data)

    user = User.objects.filter(username = data['username'])

    if user:
        return Response({"message":"Username already exists !!"})

    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        user_obj = get_object_or_404(User, id = serializer.data['id'])
        profile = get_object_or_404(Profile, user=user_obj)
        profile.pride_community =data['pride_community']
        profile.save()
        print(profile)
        token = get_object_or_404(Token, user = user_obj)
        print(token)

        return Response({"serializer_data":serializer.data, "token":token.key}, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# social media views start here

@api_view(['GET'])
def all_posts(request):
    posts = SocialMediaPost.objects.all()
    serializer = SocialMediaPostSerializer(posts, many=True)
    for post in serializer.data:
        print(post)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_post(request):
    # print("hello")
    user_obj = request.user
    prof_obj = user_obj.profile
    data = request.data
    # print(data)
    data_dict = data
    data_dict['profile'] = prof_obj.id
    # print(data_dict)
    serializer = SocialMediaPostSerializer(data=data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def modify_post(request, id):
    user_obj = request.user
    prof_obj = user_obj.profile
    post = get_object_or_404(SocialMediaPost, id=id)


    if request.method == "GET":
        serializer = SocialMediaPostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    if request.method == "PUT":
        if request.user.profile == post.profile:

            data = request.data
            data['profile']= request.user.profile.id

            serializer = SocialMediaPostSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"You do not have permission to modify"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if request.method == "DELETE":
        if request.user.profile == post.profile:
            post.delete()
            return Response({"message":"Deleted successfully"}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message":"You do not have permission to modify"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_happies(request):
    happies = Happy.objects.all()
    serializer = HappySerializer(happies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_happy(request):

    user_obj = request.user
    prof_obj = user_obj.profile
    print("hello :")
    print(user_obj)
    data = request.data
    print(data)
    data['origin']= prof_obj.id
    post = get_object_or_404(SocialMediaPost, id = data['post'])
    happy_obj = Happy.objects.filter(post=post, origin = prof_obj)
    if happy_obj:
        happy_obj.delete()
        return Response({"message": "already liked"}, status=status.HTTP_202_ACCEPTED)

    serializer = HappySerializer(data = data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def comments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request):
    data = request.data
    user_obj = request.user
    prof_obj = user_obj.profile
    data['origin']= prof_obj.id
    serializer = CommentSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


# socila media views end here


@api_view(['GET'])
def news(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def laws(request):
    laws = Laws.objects.all()
    serializer = LawsSerializer(laws, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)    


@api_view(['GET'])
def unaware(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 


@api_view(['GET'])
def sub_category(request):
    sub_category = Sub_Category.objects.all()
    serializer = Sub_CategorySerializer(sub_category, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 




@api_view(['GET'])
def all_jobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def filtered_jobs(request,category):
    category_obj = get_object_or_404(JobCategory, name=category)
    jobs = Job.objects.filter(category=category_obj)
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def job(request, id):
    job = get_object_or_404(Job, id=id)
    serializer = JobSerializer(job)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def job_categories(request):
    categories = JobCategory.objects.all()
    serializer = JobCategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)









    