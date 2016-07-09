from django.conf.urls import url
from api.cartoon import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^search$', views.search),
    url(r'^search/$', views.search),
]
