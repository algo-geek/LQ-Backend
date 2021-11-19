from rest_framework import serializers

from . models import (
    Profile,
    SocialMediaPost,
    Happy,
    News,
    Laws,
    Category,
    Sub_Category
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


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        # depth = 1

class LawsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laws
        fields = '__all__'
        # depth = 1       


class Sub_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Category
        fields = '__all__'
        # depth = 1 
        


class CategorySerializer(serializers.ModelSerializer):
    sub_category = Sub_CategorySerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'
        # depth = 1 


