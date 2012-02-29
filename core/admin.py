from django.contrib import admin
from djazz.core.models import Block,BlockVar,\
	Config,Menu,MenuItem,Widget,WidgetVar


class BlockVarInline(admin.TabularInline):
    model = BlockVar
    extra = 0
class BlockAdmin(admin.ModelAdmin):
    inlines = [BlockVarInline]

class ConfigAdmin(admin.ModelAdmin):
    list_display    = ['site','section', 'key', 'value']
    list_filter     = ['site','section','key']

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]

class WidgetVarInline(admin.TabularInline):
    model = WidgetVar
    extra = 0
class WidgetAdmin(admin.ModelAdmin):
    inlines = [WidgetVarInline]

admin.site.register(Block,BlockAdmin)
admin.site.register(Config,ConfigAdmin)
admin.site.register(Menu,MenuAdmin)
admin.site.register(Widget,WidgetAdmin)
