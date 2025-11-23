from django.shortcuts import render
import rest_framework.generics
import rest_framework.viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAdminUser

class BookList (rest_framework.generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class BookViewSet(rest_framework.viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  
  # Only admins can create/update/delete, but everyone authenticated can read
  permission_classes = [IsAdminUser]
