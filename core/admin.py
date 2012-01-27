from django.contrib import admin
from djazz.core.models import Config,Menu,MenuItem

class DjazzConfig(admin.ModelAdmin):
    list_display    = ['site','section', 'key', 'value']
    list_filter     = ['site','section','key']
admin.site.register(Config,DjazzConfig)


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]

admin.site.register(Menu,MenuAdmin)