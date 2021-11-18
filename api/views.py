from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from . models import (
    Profile, 
    SocialMediaPost
)
from . serializers import (
    ProfileSerializer,
    SocialMediaPostSerializer
)

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

# socila media views end here

    