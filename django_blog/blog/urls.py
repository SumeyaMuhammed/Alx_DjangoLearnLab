from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic import TemplateView
from .views import SignUpView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import SignUpView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # Custom login page using built-in LoginView
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Logout page using built-in LogoutView
    path('logout/', LogoutView.as_view(), name='logout'),

    # User registration page using the SignUpView
    path("register/", SignUpView.as_view(), name="register"),

    # Simple template view for profile page after login
    path('profile/', TemplateView.as_view(template_name='blog/accounts/profile.html')),

    # Shos a list of all blog posts
    path('posts/', PostListView.as_view(), name='post-list'),

    # Display the full details of a single post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Allow authenticated users to create a new post
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    # Let the author edit an existing post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    # Let the author delete an existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]