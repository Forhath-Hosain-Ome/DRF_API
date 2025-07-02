from django.urls import path
from . import views

urlpatterns = [
    path('teacher/',views.TeacherView.as_view()),
    path('teacher/<int:pk>',views.TeacherEdit.as_view()),
]