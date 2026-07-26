from django.db import models

# Create your models here.
from django.db import models

class Farm(models.Model):

    name = models.CharField(max_length=200)

    owner = models.CharField(max_length=100)

    city = models.CharField(max_length=100)

    area = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name