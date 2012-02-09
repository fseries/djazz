from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db.models.signals import pre_delete,post_save
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
    attributes  = models.TextField(null=True, blank=True)
    description = models.CharField(max_length=255,null=True, blank=True)
    
    def __unicode__(self):
        return self.title

class MenuItemManager(models.Manager):
    def get_first(self):
        return self.get(parent=None,prev=None)
    
    def get_last(self):
        return self.get(parent=None,next=None)

class MenuItem(models.Model):
    label       = models.CharField(max_length=60)
    url         = models.TextField(null=True,blank=True)
    menu        = models.ForeignKey('Menu',related_name='menuitem_menu')
    parent      = models.ForeignKey('self',null=True,blank=True,
                    related_name='menuitem_parent')
    prev        = models.ForeignKey('self',null=True,blank=True,related_name='menuitem_prev',on_delete=models.DO_NOTHING)
    next        = models.ForeignKey('self',null=True,blank=True,related_name='menuitem_next',on_delete=models.DO_NOTHING)
    attributes  = models.TextField(null=True,blank=True)
    
    objects = MenuItemManager()
    
    def __unicode__(self):
        return self.label
    
    def after(self,item):
        if self.next:
            self.next.prev = self.prev
            self.next.save()
            if self.next.id == item.id:
                item = self.next
        if self.prev:
            self.prev.next = self.next
            self.prev.save()
        
        self.prev = item
        self.next = item.next
        self.parent = item.parent
        self.save()
        if item.next:
            item.next.prev = self
            item.next.save()
        item.next = self
        item.save()
    
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
    
    def childof(self,item):
        if self.prev:
            self.prev.next = self.next
            self.prev.save()
        if self.next:
            self.next.prev = self.prev
            self.next.save()
        try:
            lastchild = item.menuitem_parent.get(next=None)
            lastchild.next = self
            lastchild.save()
            self.prev = lastchild
        
        except self.DoesNotExist:
            self.prev = None
        
        self.next = None
        self.parent = item
        self.save()
    
    def left(self):
        if self.parent:
            self.after(self.parent)
    def right(self):
        if self.prev:
            self.childof(self.prev)
    def up(self):
        if self.prev:
            self.before(self.prev)
    def down(self):
        if self.next:
            self.after(self.next)


@receiver(pre_delete, sender=MenuItem)
def on_menuitem_delete(sender,**kwargs):
    item = kwargs['instance']
    try:
        if item.prev:
            item.prev.next = item.next
            item.prev.save()
        if item.next:
            item.next.prev = item.prev
            item.next.save()
    except MenuItem.DoesNotExist:
        pass