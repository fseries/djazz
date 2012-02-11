from django.conf.urls.defaults import patterns,url


def urlpatterns():
	return patterns('',
	   # index
	   url(r'^$', 'djazz.blog.views.index', name="index"),
	   url(r'^article/(\d+)/$', 'djazz.blog.views.article', name="article"),
	   
	), 'blog', 'blog'
