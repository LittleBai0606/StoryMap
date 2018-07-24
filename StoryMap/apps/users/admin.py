from django.contrib import admin
from .models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):

    fields = ['username', 'password', 'email', 'nickname', 'gender', 'birthday', 'avatar', ]

    list_display = ['username', 'email', 'nickname']


admin.site.register(UserProfile, UserProfileAdmin)
