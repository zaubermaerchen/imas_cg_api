from django.conf.urls import url
from api.idol import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^(?P<idol_id>\d{7})$', views.get),
    url(r'^list$', views.get_list),
    url(r'^list/$', views.get_list),
]