from django.db import models
from django.utils import timezone

class Pdf(models.Model):
    """
    Create an abstract model for new files
    """
    name = models.CharField(max_length="50", null=False)
    path = models.CharField(max_length="250", null=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.name