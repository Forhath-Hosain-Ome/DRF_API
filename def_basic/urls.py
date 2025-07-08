from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('def/', include('FunctionBasedApi.urls')),
    path('cls/', include('ClassBasedApi.urls')),
    path('gen/', include('GenericsBasedApi.urls')),
]
