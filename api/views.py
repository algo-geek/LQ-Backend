from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from . models import (
    Profile
)
from . serializers import (
    ProfileSerializer
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
    