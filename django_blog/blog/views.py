from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Post

# View for user registration
def signup(request):
    if request.method == "POST":       
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()                
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


class ListView:
   model = Post
   template_name = 'blog/post_list.html'


class DetailView:
    model = Post
    template_name = 'blog/post_detail.html'

class CreateView:
    model = Post
    template_name = 'blog/post_form.html'

class UpdateView:
    model = Post
    template_name = 'blog/post_form.html'

class DeleteView:
    model = Post
    template_name = 'blog/post_confirm_delete.html'