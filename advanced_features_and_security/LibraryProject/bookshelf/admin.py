from django.contrib import admin
from .models import Book
from django.utils.translation import gettext_lazy as _
from .models import Book, CustomUser
from django.contrib.auth.models import Group, Permission

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
  
def setup_groups():
    perms = Permission.objects.filter(codename__in=[
        "can_view", "can_create", "can_edit", "can_delete"
    ])

    editors = Group.objects.create(name="Editors")
    editors.permissions.set(perms.filter(codename__in=["can_view", "can_edit", "can_create"]))

    viewers = Group.objects.create(name="Viewers")
    viewers.permissions.set(perms.filter(codename="can_view"))

    admins = Group.objects.create(name="Admins")
    admins.permissions.set(perms)


admin.site.register(CustomUser, CustomUserAdmin)