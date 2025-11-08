from django.shortcuts import render

def is_librarian(user):
  return user.userprofile.role == 'Librarian'
