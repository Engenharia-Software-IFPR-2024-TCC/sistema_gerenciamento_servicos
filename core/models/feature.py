from django.db import models
from core.models.mixins import TimeStampedModel

class Feature(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
