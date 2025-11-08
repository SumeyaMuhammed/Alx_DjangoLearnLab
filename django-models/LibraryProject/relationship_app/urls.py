from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
import views

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path("signup/", views.register.as_view(), name="signup"),
    path('login/', LoginView.as_view(template_name = 'relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'relationship_app/logout.html'), name='logout'),
]
