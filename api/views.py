from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from . models import (
    Profile, 
    SocialMediaPost,
    Happy
)
from . serializers import (
    ProfileSerializer,
    SocialMediaPostSerializer,
    HappySerializer,
    UserSerializer
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



# social media views start here

@api_view(['GET'])
def all_posts(request):
    posts = SocialMediaPost.objects.all()
    serializer = SocialMediaPostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def all_happies(request):
    happies = Happy.objects.all()
    serializer = HappySerializer(happies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def register_user(request):
    data = request.data

    serializer = UserSerializer(data=data)
    # print(data)

    user = User.objects.filter(username = data['username'])

    if user:
        return Response({"message":"Username already exists !!"})

    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        user_obj = get_object_or_404(User, id = serializer.data['id'])
        profile = get_object_or_404(Profile, user=user_obj)
        profile.pride_community = json.loads(data['pride_community'])
        profile.save()
        print(profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# socila media views end here

    