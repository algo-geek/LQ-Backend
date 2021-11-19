from django.db import models


from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pride_community = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



# social media part starts here


class SocialMediaPost(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to = 'sm_posts/')
    # others --->

    def __str__(self):
        return "post from :" + str(self.profile.user.username) + " body : " + str(self.body) 


class Happy(models.Model):
    post = models.ForeignKey(SocialMediaPost, on_delete=models.CASCADE)
    origin = models.ForeignKey(Profile, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "like of : " + str(self.post.body) + " from : " + str(self.origin.user.username)



# social media part ends here

class News(models.Model):
    headline = models.CharField(max_length=300)
    content = models.TextField()

    def __str__(self):
        return "headline : " + str(self.headline) + " content : " + str(self.content) 


class Laws(models.Model):
    law = models.CharField(max_length=300)
    des = models.TextField()

    def __str__(self):
        return "law : " + str(self.law) + " des : " + str(self.des)        


class Sub_Category(models.Model):
    sub_category = models.CharField(max_length=100)
    sub_category_des = models.TextField()

    def __str__(self):
        return " sub_category : " + str(self.sub_category) + " sub_category_description : " + str(self.sub_category_des) 


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_des = models.TextField()
    sub_category = models.ManyToManyField(Sub_Category, related_name="subcategory")

    def __str__(self):
        return " category_name : " + str(self.category_name) + " category_description : " + str(self.category_des) 
         









