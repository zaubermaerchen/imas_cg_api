from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^api/', include('api.foo.urls')),
    url(r'^imas_cg/api/idol/', include('api.idol.urls')),
    url(r'^imas_cg/api/skill/', include('api.skill.urls')),
    url(r'^imas_cg/api/idol_name/', include('api.idol_name.urls')),
    url(r'^imas_cg/api/cartoon/', include('api.cartoon.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^imas_cg/api/admin/', include(admin.site.urls)),
]
