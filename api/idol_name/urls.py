from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^list$', 'api.idol_name.views.get_list'),
    url(r'^list/$', 'api.idol_name.views.get_list'),
)
