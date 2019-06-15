from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('idol/', include('api.idol.urls')),
    path('skill/', include('api.skill.urls')),
    path('idol_name/', include('api.idol_name.urls')),
    path('cartoon/', include('api.cartoon.urls')),
]
