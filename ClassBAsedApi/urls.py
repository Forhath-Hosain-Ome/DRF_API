from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter

# router.register(r'student',viewset=views.student_edit_view,basename='student')

urlpatterns = [
    path('student/', views.StudentView.as_view()),
    path('student/<int:pk>/', views.StudentEdit.as_view()),
]