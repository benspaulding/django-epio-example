from django.conf.urls.defaults import *

# Thing views.
urlpatterns = patterns('example.apps.things.views',

    url(r'^$',
        'thing_index',
        name='things-thing-index'),

    url(r'^(?P<slug>[-\w]+)/$',
        'thing_detail',
        name='things-thing-detail'),
)
