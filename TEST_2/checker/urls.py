from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

app_name = 'checker'

urlpatterns = [
    #path('dust_checker', include('dust_checker.urls'),name='dust'),
    path('dust_checker', include('dust_checker.urls')),
    #path('covid_checker', include('covid_checker.urls'),name='covid'),
    path('covid_checker', include('covid_checker.urls')),
    path('',include('common.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)