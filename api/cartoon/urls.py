from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^list$', 'api.cartoon.views.get_list'),
    url(r'^list/$', 'api.cartoon.views.get_list'),
)
