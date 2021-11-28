from django.contrib import admin
from . models import (
    Profile,
    SocialMediaPost,
    Happy,
    News,
    Laws,
    Category,
    Content,
    Comment,
    Job,
    JobCategory
)

# Register your models here.
admin.site.register(Profile)
admin.site.register(SocialMediaPost)
admin.site.register(Happy)
admin.site.register(News)
admin.site.register(Laws)
admin.site.register(Category)
admin.site.register(Content)
admin.site.register(Comment)
admin.site.register(Job)
admin.site.register(JobCategory)