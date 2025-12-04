from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# View for user registration
class SignUpView(CreateView):
    form_class = UserCreationForm  # Form used for creating a new user
    success_url = reverse_lazy('login')  # Redirect URL after successful signup
    template_name = 'registration/signup.html'  # Template for the signup page


