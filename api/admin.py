from django.contrib import admin
from . models import (
    Profile,
    SocialMediaPost,
    Happy
)

# Register your models here.
admin.site.register(Profile)
admin.site.register(SocialMediaPost)
admin.site.register(Happy)