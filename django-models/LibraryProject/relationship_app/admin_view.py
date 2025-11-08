from django.shortcuts import render

def is_admin(user):
  return user.userprofile.role == 'Admin'
