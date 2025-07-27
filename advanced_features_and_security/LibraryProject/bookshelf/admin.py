from django.contrib import admin
from .models import Book ,CustomUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'published_date')
    list_filter = ('published_date', )
    search_fields = ('title','author')


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)