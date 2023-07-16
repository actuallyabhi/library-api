from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    publication_date = models.DateField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return self.title
