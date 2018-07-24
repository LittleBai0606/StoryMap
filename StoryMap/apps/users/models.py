from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.


class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ('register', u'注册'),
        ('forget', u'找回密码')
    )

    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=SEND_CHOICES, max_length=10, verbose_name=u'邮件目的')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name


class UserProfile(AbstractUser):

    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女'),
        ('secret', '保密'),
    )
    # 邮箱
    email = models.EmailField(unique=True, max_length=50, verbose_name=u'邮箱')
    # 昵称
    nickname = models.CharField(max_length=30, default=u'佚名大侠', verbose_name=u'昵称')
    # 性别
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male', verbose_name=u'姓名')
    # 生日
    birthday = models.DateField(null=True, blank=True, verbose_name=u'生日')
    # 头像
    avatar = models.ImageField(upload_to='image/%Y/%m', default=u'img/user.jpg')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


