from django.db import models
from django.contrib.sites.models import Site


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
