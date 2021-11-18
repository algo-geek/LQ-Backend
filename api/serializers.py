from rest_framework import serializers

from . models import (
    Profile,
    SocialMediaPost,
    Happy
)

from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password','id']

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user





class SocialMediaPostSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()
    class Meta:
        model = SocialMediaPost
        fields = '__all__'
        # depth = 1


class HappySerializer(serializers.ModelSerializer):
    class Meta:
        model = Happy
        fields = '__all__'
        # depth = 1