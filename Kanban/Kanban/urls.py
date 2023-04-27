from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Main.urls')),
    path('registration', include('Main.urls')),
    path('register', include('Main.urls')),
    path('main', include('Main.urls')),
]
