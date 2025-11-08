from django.shortcuts import render

def is_member(user):
  return user.userprofile.role == 'Member'

