import kwargs
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    summary = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    # publish_date = models.DateField()

    def __str__(self):
        return self.title
