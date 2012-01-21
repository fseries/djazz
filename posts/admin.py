from django.contrib import admin
from djazz.posts.models import Post,PostVar,Type,TypeVar


class PostVarInline(admin.TabularInline):
    model = PostVar
    extra = 0

class TypeVarInline(admin.TabularInline):
    model = TypeVar
    extra = 0

class AdminPost(admin.ModelAdmin):
    fieldsets    = (
        (None,{
               'fields': ('title','parent','uid','type','content','status'),
        }),
        ("Advanced options",{
              'classes': ('collapse',),
              'fields': ('author','last_editor',)
        }),
    )
    inlines = [PostVarInline]
    list_filter = ['type']

class AdminType(admin.ModelAdmin):
    inlines = [TypeVarInline]

admin.site.register(Post,AdminPost)
admin.site.register(Type,AdminType)
