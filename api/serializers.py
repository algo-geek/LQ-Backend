from rest_framework import serializers
from rest_framework.authtoken.models import Token

from . models import (
    Profile,
    SocialMediaPost,
    Happy,
    News,
    Laws,
    Category,
    Sub_Category,
    Comment,
    Job,
    JobCategory
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


class CommentSerializer(serializers.ModelSerializer):
    prof_username = serializers.SerializerMethodField("get_username")
    def get_username(self,obj):
        prof =  obj.origin
        return prof.user.username
    class Meta:
        model = Comment
        fields = '__all__'



class SocialMediaPostSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()
    prof_username = serializers.SerializerMethodField("get_username")
    happies_count = serializers.SerializerMethodField("get_happies_count")
    happy_profs = serializers.SerializerMethodField("get_happy_profs")
    comments = serializers.SerializerMethodField("get_comments")
    comments_count = serializers.SerializerMethodField("get_comments_count")

    def get_happies_count(self,obj):
        happies_count = len(obj.happy_set.all())
        return happies_count
    
    def get_comments_count(self,obj):
        comments_count = len(obj.comment_set.all())
        return comments_count

    def get_username(self,obj):
        prof =  obj.profile
        return prof.user.username
    
    def get_happy_profs(self, obj):
        li =[]
        for i in obj.happy_set.all():
            token = Token.objects.get(user =i.origin.user)
            li.append(token.key)
        return li
    def get_comments(self, obj):
        all_comments = obj.comment_set.all().order_by('-timestamp')
        serializer = CommentSerializer(all_comments, many=True)
        return serializer.data

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




class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField("get_category")

    def get_category(self,obj):
        cats = obj.category.all()
        serializer = JobCategorySerializer(cats, many=True)
        return serializer.data


    class Meta:
        model = Job
        fields = '__all__'


    





