from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookSearchForm, ExampleForm

def search_books(request):
    form = BookSearchForm(request.GET or None)
    books = None
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_search.html', {'form': form, 'books': books})

def example_form_view(request):
    form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form": form})



def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

def books(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "bookshelf/book_detail.html", {"book": book})


@permission_required('advanced_features_and_security.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})

@permission_required('advanced_features_and_security.can_create', raise_exception=True)
def create_article(request):
    # creation logic
    return render(request, 'articles/create.html')

@permission_required('advanced_features_and_security.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # editing logic
    return render(request, 'articles/edit.html', {'article': article})

@permission_required('advanced_features_and_security.can_delete', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')

