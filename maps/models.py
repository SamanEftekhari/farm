from django.db import models

# Create your models here.
from django.db import models

from farms.models import Farm

class Field(models.Model):

    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        related_name="fields"
    )

    name = models.CharField(max_length=100)

    geojson = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name