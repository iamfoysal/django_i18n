from django.contrib import admin
from .models import User
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'name', 'created_at',)
    search_fields = ('username',)
    list_display_links = ('username', 'password')
    ordering = ('-created_at',)
    list_filter = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('username', 'name','password',)
        }),
    )


