from django.db import models


# Create your models here.

class Image(models.Model):
    url = models.URLField()
    name = models.CharField(max_length = 80)

    def __str__(self):
        return f'Name: {self.name}, url: {self.url}'
    