from django.contrib import admin
from . models import (
    Profile,
    SocialMediaPost
)

# Register your models here.
admin.site.register(Profile)
admin.site.register(SocialMediaPost)