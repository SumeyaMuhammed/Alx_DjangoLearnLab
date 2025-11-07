from django.urls import path
from .views import list_books, libraryDetailView

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('libraries/<int:pk>/', libraryDetailView.as_view(), name='library-detail'),
]