from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Urls_App.urls')),
]
urlpatterns += [
    # path('obtain-auth-token/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    # path('accounts/profile/', lambda request: HttpResponse("Profile page")),
]