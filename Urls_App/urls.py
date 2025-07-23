from django.urls import path
from View_App.views import AccountListView, AccountEditView, CourseListView, CourseEditView, DepertmentListView, DepertmentEditView, SubjectEditView, SubjectListView, SubjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Subject', SubjectViewSet, basename='subject')

urlpatterns = [
    path('', AccountListView),
    path('<int:pk>/', AccountEditView),

    path('class/', CourseListView.as_view()),
    path('class/<int:pk>/', CourseEditView.as_view()),
    
    path('dep/', DepertmentListView.as_view()),
    path('dep/<int:pk>/', DepertmentEditView.as_view()),

    path('sub/', SubjectListView.as_view()),
    path('sub/<int:pk>/', SubjectEditView.as_view()),

]

urlpatterns += router.urls