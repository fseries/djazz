from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db.models.signals import post_save
from django.dispatch import receiver
from djazz.core.db import ModelTree


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
    attributes  = models.TextField(null=True, blank=True)
    description = models.CharField(max_length=255,null=True, blank=True)
    
    def __unicode__(self):
        return self.title

class MenuItem(models.Model):
    label       = models.CharField(max_length=60)
    url         = models.TextField(null=True,blank=True)
    menu        = models.ForeignKey('Menu',related_name='menuitem_menu')
    parent      = models.ForeignKey('self',null=True,blank=True,
                    related_name='menuitem_parent')
    prev        = models.ForeignKey('self',null=True,blank=True,related_name='menuitem_prev')
    next        = models.ForeignKey('self',null=True,blank=True,related_name='menuitem_next')
    attributes  = models.TextField(null=True,blank=True)
    
    def __unicode__(self):
        return self.label
    
    def before(self,item):
        if self.prev:
                self.prev.next = self.next
                self.prev.save()
                if self.prev.id == item.id:
                    item = self.prev
        if self.next:
            self.next.prev = self.prev
            self.next.save()
        
        self.next = item
        self.prev = item.prev
        self.parent = item.parent
        self.save()
        if item.prev:
            item.prev.next = self
            item.prev.save()
        item.prev = self
        item.save()
    
#    def after(self,item):
#    def childof(self,item):
#    def left(self)
#    def right(self)
#    def up(self)
#    def down(self)
