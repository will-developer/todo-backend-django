from django.db import models

class Task(models.Model):
    """Model representing a task in the todo list."""
    title = models.CharField(max_length=200, verbose_name='Title')
    completed = models.BooleanField(default=False, verbose_name='Completed')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    class Meta:
        ordering = ['-created_at']  # Newest tasks first

    def __str__(self):
        return self.title