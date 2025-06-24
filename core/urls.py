from django.urls import path
from .views import Notes_List, Note_Edit

# urlpatterns = [
#     path('hello/', notes_create, name='hello'),
#     path('hello/<int:pk>/', notes_create_details, name='hello'),
# ]
urlpatterns = [
    path('hello/', Notes_List.as_view(), name='hello'),
    path('hello/<int:pk>/', Note_Edit.as_view(), name='hello'),
]

