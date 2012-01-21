from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('',
#   url(r'^post/test/$', 'djazz.forum.views.test'),

   url(r'^$', 'djazz.forum.views.index'),
   url(r'^topic/new/$', 'djazz.forum.views.new'),
   url(r'^topic/([\w-]+)/$', 'djazz.forum.views.topic'),
   url(r'^topic/([\w-]+)/add/$', 'djazz.forum.views.new'),
   
)
