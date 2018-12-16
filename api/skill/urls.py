from django.urls import path
from .views import ListView
from api.skill import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('list/', views.get_list),
    path('list2/', ListView.as_view()),
]
