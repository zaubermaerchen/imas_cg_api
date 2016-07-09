from django.conf.urls import url
from api.skill import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^list$', views.get_list),
    url(r'^list/$', views.get_list),
]
