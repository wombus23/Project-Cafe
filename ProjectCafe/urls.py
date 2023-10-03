from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),  # This maps to the /admin/ URL
    path('',include('base.url'))
]
