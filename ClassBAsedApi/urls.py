from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StudentView.as_view()),
    path('student/<int:pk>/', views.StudentEdit.as_view()),
]