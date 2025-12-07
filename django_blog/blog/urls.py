from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from .views import signup, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentDeleteView, CommentUpdateView, PostByTagView

urlpatterns = [
    # Custom login page using built-in LoginView
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Logout page using built-in LogoutView
    path('logout/', LogoutView.as_view(), name='logout'),

    # User registration page using the signup function
    path("register/", signup, name="register"),

    # Simple template view for profile page after login
    path('profile/', TemplateView.as_view(template_name='blog/accounts/profile.html')),

    # Shos a list of all blog posts
    path('', PostListView.as_view(), name='home'),

    # Display the full details of a single post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Allow authenticated users to create a new post
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    # Let the author edit an existing post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    # Let the author delete an existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    path("search/", views.search_view, name="search"),
    path("tags/<slug:tag_slug>/", views.posts_by_tag, name="posts_by_tag"),
    path('tags/<str:tag_name>/', PostByTagView.as_view(), name='posts-by-tag'),

]