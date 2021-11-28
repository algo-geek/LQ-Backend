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


class Comment(models.Model):
    post = models.ForeignKey(SocialMediaPost, on_delete=models.CASCADE)
    body = models.TextField()
    origin = models.ForeignKey(Profile, on_delete= models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Comment of :" + str(self.post.body) + " from : " + str(self.origin.user.username)





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


class Content(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return "title : " + str(self.title) + "description : " + str(self.description) 


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_des = models.TextField()
    content = models.ManyToManyField(Content, related_name="content")

    def __str__(self):
        return " category_name : " + str(self.category_name) + " category_description : " + str(self.category_des) 
         



# job portal stats here

class JobCategory(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    
    def __str__(self):
        return self.name








class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=100)
    isOpen = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    min_experience = models.IntegerField(default=0)
    max_experience = models.IntegerField(default=10)
    category = models.ManyToManyField(JobCategory, related_name='job_category')
    salary_ctc = models.IntegerField()
    age_limit = models.IntegerField(default=40)
    isRemote = models.BooleanField(default=False)
    hirer = models.ForeignKey(Profile, on_delete= models.CASCADE)

    def __str__(self):
        return self.title





# job portal ends here






