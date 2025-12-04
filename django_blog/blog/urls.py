from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic import TemplateView
from .views import SignUpView

urlpatterns = [
    # Custom login page using built-in LoginView
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Logout page using built-in LogoutView
    path('logout/', LogoutView.as_view(), name='logout'),

    # User registration page using the SignUpView
    path("register/", SignUpView.as_view(), name="registration/register"),

    # Simple template view for profile page after login
    path('profile/', TemplateView.as_view(template_name='accounts/profile.html')),
]