from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author')

admin.site.register(Book, BookAdmin)


