from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import PostForm, CommentForm
from .models import Post, Comment
from taggit.models import Tag

# View for user registration
def signup(request):
    if request.method == "POST":       
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()                
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "blog/register.html", {"form": form})

# List View
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

#Detail View
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['comment_form'] = CommentForm()
        return ctx

#Create View
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        tags_input = form.cleaned_data.get("tags", "")
        tag_names = [t.strip() for t in tags_input.split(",") if t.strip()]

        self.object.tags.clear()
        for name in tag_names:
            tag_obj, created = Tag.objects.get_or_create(name=name)
        self.object.tags.add(tag_obj)

        return response

# Update View
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
    def form_valid(self, form):
        response = super().form_valid(form)
        tags_input = form.cleaned_data.get("tags", "")
        tag_names = [t.strip() for t in tags_input.split(",") if t.strip()]

        self.object.tags.clear()
        for name in tag_names:
            tag_obj, created = Tag.objects.get_or_create(name=name)
        self.object.tags.add(tag_obj)

        return response


# Delete View
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    # attach comment to correct post
    def dispatch(self, request, *args, **kwargs):
        self.post = get_object_or_404(Post, pk=kwargs.get('post_pk'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.post
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['post'] = self.post
        return ctx

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.get_object().post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.get_object().post.pk})

def search_view(request):
    query = request.GET.get("q")
    results = []

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

    return render(request, 'blog/search_results.html', {'query': query, 'results': results})

def posts_by_tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    posts = Post.objects.filter(tags__in=[tag])
    return render(request, 'blog/tag_posts.html', {'tag': tag, 'posts': posts})

class PostByTagView(ListView):
    model = Post
    template_name = "blog/posts_by_tag.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs['tag_name'])
