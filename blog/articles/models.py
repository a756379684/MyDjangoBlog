from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
from django.utils import timezone

class Article(models.Model):
    #标题
    title = models.CharField(max_length=100)
    #正文
    text = models.TextField()
    #创建日期
    create = models.DateTimeField(default = timezone.now)
    #标签
    tags = TaggableManager(blank=True)
    #访问量
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class Mydynamic(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.text