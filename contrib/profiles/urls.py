from django.conf.urls.defaults import patterns,url
from django.core.urlresolvers import reverse

def urlpatterns():
	return patterns('',
	   # index
	   url(r'^$', 'djazz.contrib.profiles.views.index'),
       
       url(r'^edit/$', 'djazz.contrib.profiles.views.edit'),
       
       url(r'^edit/password/change/$',
            'django.contrib.auth.views.password_change',
            { 'template_name':'djazz/profiles/password_change.html',
              'post_change_redirect': '/profile/'}),
       url(r'^edit/password/save/$', 'django.contrib.auth.views.password_change_done'),
       url(r'^edit/password/reset/$', 'django.contrib.auth.views.password_reset'),
	)
