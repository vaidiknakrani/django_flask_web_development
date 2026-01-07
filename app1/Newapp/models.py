from django.db import models

# Create your models here.
class Image(models.Model):
    # ...existing code...
    category = models.CharField(max_length=50, blank=True, null=True)  # e.g., 'nature', 'animals'

    def __str__(self):
        return self.title