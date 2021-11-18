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






