from django.db import models
from django.contrib.auth.models import User
from djazz.posts.signals import types_choice


def posttype_choices():
    types = []
    types_choice.send(sender=None,types_list=types)
    return types


## Models
class Category(models.Model):
    name = models.CharField(max_length=30,unique=True)
    parent = models.ForeignKey('self',null=True,blank=True,
            related_name='category_parent')

class Post(models.Model):
    title       = models.CharField(max_length=100)
    uid         = models.CharField(max_length=100)
    parent      = models.ForeignKey('self',null=True,blank=True)
    author      = models.ForeignKey(User,related_name="post_author",
							null=True,blank=True)
    content     = models.TextField(null=True,blank=True)
    type        = models.CharField(max_length=20,choices=posttype_choices())
    category	= models.ManyToManyField('Post',null=True,blank=True,
            related_name='category_blog')
    status      = models.CharField(max_length=15,null=True,blank=True)
    date        = models.DateTimeField(auto_now_add=True)
    last_editor = models.ForeignKey(User,related_name="post_lasteditor",
							null=True,blank=True)
    last_date   = models.DateTimeField(auto_now=True, auto_now_add=True)
    def __unicode__(self):
        return self.uid
        
    def save(self, *args, **kwargs):
        import random,re
        if not self.uid and not self.id:
            self.uid = re.sub('[\W]','-',self.title).lower()
            if Post.objects.filter(uid=self.uid).exists():
                suffixe = '_' + str(random.randint(1,1000000000))
                while Post.objects.filter(uid=self.uid + suffixe).exists():
                    suffixe = '_' + str(random.randint(1,1000000000))
                self.uid += suffixe
        super(Post, self).save(*args, **kwargs)

class PostVar(models.Model):
    post    = models.ForeignKey('Post',related_name="postvar_post")
    key     = models.CharField(max_length=60)
    value   = models.TextField(null=True,blank=True)
    def __unicode__(self):
        return self.key + " - " + self.post.uid

