from django.db import models

# Create your models here.


class Story(models.Model):
    """
    旅行故事
    """
    title = models.CharField()


