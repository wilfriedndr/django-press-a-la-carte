from django.db import models
from django.utils import timezone

class Pdf(models.Model):
    """
    Create a model for new files
    """
    name = models.CharField(max_length=150, null=False)
    path = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name