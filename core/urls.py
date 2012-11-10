from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
    url(r'^$', 'landing', name='landing_page'),
    url(r'^(?P<slug>[a-zA-Z0-9\-]+)/$', 'visualization', 
        name='visualization'),
)
