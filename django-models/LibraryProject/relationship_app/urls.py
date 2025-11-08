from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views
from .views import list_books, LibraryDetailView
from .admin_view import admin_dashboard
from .member_view import member_dashboard
from librarian_view import librarian_dashboard

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path("signup/", views.register, name="signup"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/',  admin_dashboard, name="member-dashboard"),
    path('member/',  librarian_dashboard, name="member-dashboard"),
    path('member/', member_dashboard, name='member-dashboard'),
]
