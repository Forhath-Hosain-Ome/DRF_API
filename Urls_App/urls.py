from django.urls import path
from View_App.views import AccountListView, AccountEditView, CourseListView, CourseEditView, DepertmentListView, DepertmentEditView


urlpatterns = [
    path('', AccountListView),
    path('<int:pk>/', AccountEditView),

    path('class/', CourseListView.as_view()),
    path('class/<int:pk>/', CourseEditView.as_view()),
    
    path('dep/', DepertmentListView.as_view()),
    path('dep/<int:pk>/', DepertmentEditView.as_view()),
]

