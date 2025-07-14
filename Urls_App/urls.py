from django.urls import path
from View_App.views import AccountView
urlpatterns = [
    path('', AccountView),
]
