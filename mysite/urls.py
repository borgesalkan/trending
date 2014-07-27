from django.conf.urls import patterns, include, url

from twitter.views import get_sample_tweets, post_minutes

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sample_tweets/$', get_sample_tweets, name='top_retweets'),
    url(r'^sample_tweets/(?P<minutes>[^/]+)/$', get_sample_tweets, name='top_retweets_minutes'),
    url(r'^input/$', post_minutes, name='input_minutes'),
)

