from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

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

