from django.urls import path
from .views import SearchView, CostarView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('search/', SearchView.as_view()),
    path('costar/<str:name>', CostarView.as_view()),
]
