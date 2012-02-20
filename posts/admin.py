from django.contrib import admin
from djazz.posts.models import Post,PostVar,Type,TypeVar


class PostVarInline(admin.TabularInline):
    model = PostVar
    extra = 0

class TypeVarInline(admin.TabularInline):
    model = TypeVar
    extra = 0

class AdminPost(admin.ModelAdmin):
    inlines = [PostVarInline]
    list_filter = ['type']
    exclude = ('author','last_editor',)
    
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.author = request.user
        obj.last_editor = request.user
        super(AdminPost,self).save_model(request,obj,form,change)

class AdminType(admin.ModelAdmin):
    inlines = [TypeVarInline]

admin.site.register(Post,AdminPost)
admin.site.register(Type,AdminType)
