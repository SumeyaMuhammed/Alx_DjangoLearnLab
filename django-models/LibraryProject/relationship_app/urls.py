from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('libraries/<int:pk>/', views.libraryDetailView.as_view(), name='library-detail'),
]