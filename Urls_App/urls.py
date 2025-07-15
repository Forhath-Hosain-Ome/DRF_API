from django.urls import path
from View_App.views import AccountListView, AccountEditView, CourseListView, CourseEditView
urlpatterns = [
    path('', AccountListView),
    path('<int:pk>/', AccountEditView),

    path('class/', CourseListView.as_view()),
    path('class/<int:pk>/', CourseEditView.as_view()),
]
