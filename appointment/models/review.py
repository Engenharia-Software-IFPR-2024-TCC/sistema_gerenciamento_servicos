from django.db import models
from core.models.mixins import TimeStampedModel

class Review(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    comment = models.TextField()
