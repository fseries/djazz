from djazz.core import widgets

class Categories(widgets.Widget):
    name = "Categories Widget"
    version = "0.1"
    
    def pre_render(self):
        from djazz.contrib.posts.models import PostVar
        cats = PostVar.objects.filter(key="category")
        self.add_var('categories', cats)