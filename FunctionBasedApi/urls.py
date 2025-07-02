from django.urls import path
from . import views

urlpatterns = [
    path('note/', views.ApiFunctionView),
    path('note/<int:pk>/', views.ApiFunctionEdit),
]