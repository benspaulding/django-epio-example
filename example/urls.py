from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    url(r'^things/', include('example.apps.things.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls')),

    url(r'^$',
        'django.views.generic.simple.direct_to_template',
        { 'template': 'homepage.html' },
        name='home'),

    # Including this makes flatpage URLs reversable, though more verbose to use
    # in templates and code. I may or may not keep this.
    url(r'^(?P<url>.*)$',
        'django.contrib.flatpages.views.flatpage',
        name='flatpage'),
)
