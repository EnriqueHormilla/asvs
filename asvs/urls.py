
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('home.urls')),
    path('home/', include('home.urls')),
    path('levels/', include('levels.urls')),
    path('help/', include('help.urls')),
    path('auth/', include('accountauth.urls')),
    path('projects/', include('projects.urls')),
    re_path(r'^api/', include('accountauth.urls')),

]
