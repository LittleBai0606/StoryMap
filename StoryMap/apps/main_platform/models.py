from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import UserProfile


# Create your models here.


class Story(models.Model):
    """
    旅行故事
    """
    title = RichTextUploadingField(max_length=1000, null=False, verbose_name=u'标题')
    content = RichTextUploadingField(max_length=1000, default='', verbose_name=u'内容')
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'创建时间')
    modified_time = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'最后修改时间')

    user_belong = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'所属用户')
    #经度
    longitude = models.FloatField(default=116.397428, verbose_name=u'景点经度')
    latitude = models.FloatField(default=39.90923, verbose_name=u'景点纬度')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    class Meta:
        verbose_name = u'旅行故事'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Gallery(models.Model):
    """
    旅行照片墙
    """
    photo_name = models.CharField(max_length=100, verbose_name=u'照片名字')
    photo_url = models.CharField(max_length=100, verbose_name=u'照片路径')
    user_belong = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'所属用户')

    class Meta:
        verbose_name = u'旅行照片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.photo_name


class Comment(models.Model):
    """
    评论
    """

    content = models.TextField(max_length=500, verbose_name=u'评论内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u'评论时间')
    story_belong = models.ForeignKey(Story, on_delete=models.CASCADE, verbose_name=u'所属故事')
    user_belong = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'所属用户')


    class Meta:
        verbose_name = '博客评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:10]









