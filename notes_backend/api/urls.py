from django.urls import path
from .views import (
    health,
    NoteListCreateAPIView,
    NoteRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('health/', health, name='Health'),
    path('notes/', NoteListCreateAPIView.as_view(), name='notes-list-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyAPIView.as_view(), name='notes-detail'),
]
