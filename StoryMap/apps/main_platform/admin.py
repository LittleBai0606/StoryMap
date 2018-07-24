from django.contrib import admin
from .models import Story


# Register your models here.

class StoryAdmin(admin.ModelAdmin):

    fields = ['title', 'content', 'user_belong', 'longitude', 'latitude']

    list_display = ['title', 'content', 'created_time', 'modified_time', 'user_belong']


admin.site.register(Story, StoryAdmin)