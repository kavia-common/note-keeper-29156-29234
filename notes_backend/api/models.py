from django.db import models


class Note(models.Model):
    """
    Note model representing a user note with title, content, archive state,
    and timestamps for creation and updates.
    """
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Provide a readable representation of the note
        return f"{self.title}"

    class Meta:
        # Order by most recently updated first
        ordering = ['-updated_at']
