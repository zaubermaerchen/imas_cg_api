from django.urls import path
from .views import GetView, SearchView
from api.idol import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('<int:pk>/', GetView.as_view()),
    path('search/', SearchView.as_view()),
    path('list/', views.get_list),
]