from django.conf.urls.defaults import patterns,url


def urlpatterns():
	return patterns('',
	   # index
	   url(r'^$', 'djazz.contrib.blog.views.index', name="index"),
	   url(r'^article/(\d+)/$', 'djazz.contrib.blog.views.article', name="article"),
	   
	), 'blog', 'blog'
