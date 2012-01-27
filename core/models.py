from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User)

@receiver(post_save, sender=User)
def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.get_or_create(user=kwargs['instance'])

class Config(models.Model):
    site    = models.ForeignKey(Site,null=True,blank=True)
    section = models.CharField(max_length=15,null=True,blank=True)
    key     = models.CharField(max_length=60)
    value   = models.TextField(null=True,blank=True)
    
    def __unicode__(self):
        return "["+self.section+"] "+self.key
    
    class Meta:
        ordering    = ['section','key']
        unique_together = ('site', 'section', 'key')


class Menu(models.Model):
    title       = models.CharField(max_length=60)
    attributes  = models.TextField()
    description = models.CharField(max_length=255)
    
class MenuItem(models.Model):
    label   = models.CharField(max_length=60)
    url     = models.TextField()
    menu    = models.ForeignKey('Menu',related_name='menuitem_menu')
    attributes  = models.TextField()
    