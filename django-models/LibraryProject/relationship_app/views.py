from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import DetailView

def book_list(request):
  books = {'books': Book.objects.all()}
  return render(request, 'relationship_app/list_books.html', books)

class libraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context
  