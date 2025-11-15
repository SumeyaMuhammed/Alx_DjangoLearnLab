from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Author, Book, Library, Librarian, CustomUser

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

class userAdmin(admin.ModelAdmin):
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