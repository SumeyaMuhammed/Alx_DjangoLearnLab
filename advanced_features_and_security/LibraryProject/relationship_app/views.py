from django.shortcuts import render, redirect
from .models import Book, CustomUser
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .admin_view import is_admin
from .member_view import is_member
from .librarian_view import is_librarian

def list_books(request):
  books = {'books': Book.objects.all()}
  return render(request, 'relationship_app/list_books.html', books)

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context
  
#  User Authentication Views
def register(request):
    if request.method == "POST":
        form = UserCreationForm(CustomUser(request.POST))
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("member-dashboard")
    else:
        form = UserCreationForm(CustomUser)

    return render(request, "relationship_app/register.html", {"form": form})

@user_passes_test(is_admin)
def admin_dashboard(request):
  return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_dashboard(request):
  return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_dashboard(request):
  return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
  book = Book(title = '1984', author = 'George Orwell', published_date = 1949)
  book.save()
  return redirect('book-list')



@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request, book_id):
  book = Book.objects.get(id=book_id)
  book.title = 'The Art of Being Alone'
  book.save()
  return redirect('book-list')

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
  book = Book.objects.get(id=book_id)
  book.delete()
  return redirect('book-list')
