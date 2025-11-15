from django.contrib import admin
from .models import Book
from django.utils.translation import gettext_lazy as _
from .models import Book, CustomUser
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

class CustomUserAdmin(admin.ModelAdmin):
  model = CustomUser
  list_display = ("email", "date_of_birth", "profile_photo", "is_staff", "is_superuser", "is_active")
  list_filter = ("is_staff", "is_superuser")
  fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("date_of_birth", "profile_photo")}),
        (_("Permissions"), {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
        }),
    )

  add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "date_of_birth", "profile_photo", "password1", "password2"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)"