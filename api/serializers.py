from rest_framework import serializers
from . models import (
    Profile,
    SocialMediaPost,
    Happy
)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1


class SocialMediaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaPost
        fields = '__all__'
        depth = 1


class HappySerializer(serializers.ModelSerializer):
    class Meta:
        model = Happy
        fields = '__all__'
        depth = 1