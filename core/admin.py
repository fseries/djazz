from django.contrib import admin
from djazz.core.models import Config

class DjazzConfig(admin.ModelAdmin):
    list_display    = ['site','section', 'key', 'value']
    list_filter     = ['site','section','key']
admin.site.register(Config,DjazzConfig)
