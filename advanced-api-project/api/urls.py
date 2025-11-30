from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('books/create/', BookCreateView.as_view()),
    path('books/update/', BookUpdateView.as_view()),
    path('books/delete/', BookDeleteView.as_view()),
]
