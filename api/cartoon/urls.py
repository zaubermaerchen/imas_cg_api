from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^search$', 'api.cartoon.views.search'),
    url(r'^search/$', 'api.cartoon.views.search'),
)
