from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views
from .views import list_books, LibraryDetailView, admin_dashboard, member_dashboard, librarian_dashboard, add_book, change_book, delete_book

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path("signup/", views.register, name="signup"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/',  admin_dashboard, name="member-dashboard"),
    path('member/',  librarian_dashboard, name="member-dashboard"),
    path('member/', member_dashboard, name='member-dashboard'),
    path('add_book/',add_book, name='add-book' ),
    path('edit_book/<int:book_id>/',change_book, name='change-book' ),
    path('delete_book/<int:book_id>/',delete_book, name='delete-book' ),
]
