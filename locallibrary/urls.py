from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('catalog/', include('catalog.urls')),
    path('admin/', admin.site.urls)
]