from django.urls import path
from api.idol_name import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('list', views.get_list),
    path('list/', views.get_list),
]
