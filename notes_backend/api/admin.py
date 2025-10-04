from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Admin configuration for Note model."""
    list_display = ('id', 'title', 'is_archived', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('is_archived',)
    ordering = ('-updated_at',)
