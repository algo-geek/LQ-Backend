from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    return Response({"message":"hello"})