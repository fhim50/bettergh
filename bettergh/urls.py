from django.conf.urls import patterns, include, url
from search_lap.views import search , home
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bettergh.views.home', name='home'),
    # url(r'^bettergh/', include('bettergh.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'search_lap.views.home'),
	url(r'^search_lap/search/(?P<term>.*?)$', 'search_lap.views.search'),
)
