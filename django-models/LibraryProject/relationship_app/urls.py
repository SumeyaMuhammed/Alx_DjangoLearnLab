from django.urls import path, include
from .views import list_books, LibraryDetailView, SignUpView
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('login/', LoginView.as_view(template_name = 'relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'relationship_app/logout.html'), name='logout'),
]
