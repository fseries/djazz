from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title       = models.CharField(max_length=100)
    uid            = models.CharField(max_length=100,unique=True,blank=True)
    parent      = models.ForeignKey('self',null=True,blank=True)
    author      = models.ForeignKey(User,related_name="author_posts",null=True,blank=True)
    content     = models.TextField(null=True,blank=True)
    type        = models.ForeignKey('Type',null=True,blank=True)
    status      = models.CharField(max_length=15,null=True,blank=True)
    date        = models.DateTimeField(auto_now_add=True)
    last_editor = models.ForeignKey(User,related_name="last_editor_posts",null=True,blank=True)
    last_date   = models.DateTimeField(auto_now=True, auto_now_add=True)
    def __unicode__(self):
        return self.uid


class PostVar(models.Model):
    post    = models.ForeignKey('Post',related_name="postvars")
    key     = models.CharField(max_length=60)
    value   = models.TextField(null=True,blank=True)
    def __unicode__(self):
        return self.key + " - " + self.post.unix_title


class Type(models.Model):
    name    = models.CharField(max_length=20)
    description = models.CharField(max_length=255,blank=True,null=True)

    
class TypeVar(models.Model):
    type    = models.ForeignKey('Type',related_name="typevars")
    key     = models.CharField(max_length=60)
    value   = models.TextField(null=True,blank=True)
    def __unicode__(self):
        return self.key + " - " + self.type.name
