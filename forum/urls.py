from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('',

   # index
   url(r'^$', 'djazz.forum.views.index'),
   
   # liste d'un forum
   url(r'^forum/(\d+)/$', 'djazz.forum.views.index'),
   
   # creation d'un sujet
   url(r'^topic/create/(?P<forum>\d+)/$', 'djazz.forum.views.create'),
   
   # reponse a un sujet
   url(r'^topic/(?P<topic>\d+)/reply/$', 'djazz.forum.views.create'),
   
   # visualisation d'un sujet
   url(r'^topic/(\d+)/$', 'djazz.forum.views.topic'),
   
)
