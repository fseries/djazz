from django.db import models

class Forum(models.Model):
    name    = models.CharField(max_length=50)
    parent  = models.ForeignKey('self',null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    
    def __unicode__(self):
        if self.parent:
            return self.parent.name +" -> "+ self.name
        return self.name
    class Meta:
        unique_together = (('name','parent'),)

