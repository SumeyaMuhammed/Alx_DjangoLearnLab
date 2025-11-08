from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

urlpatterns = [
    path('books/', views.list_books, name='book-list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    path("signup/", views.register, name="signup"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
