from django.urls import path
from View_App.views import AccountListView, AccountEditView
urlpatterns = [
    path('', AccountListView),
    path('<int:pk>/', AccountEditView),
]
