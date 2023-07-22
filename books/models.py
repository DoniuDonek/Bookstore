import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser


FORMATS_CHOICES = [
    ('PB', 'Paperback'),
    ('HC', 'Hardcover'),
    ('EB', 'Ebook'),
    ('AB', 'Audiobook'),
]


class Book(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    title = models.CharField(max_length = 155)
    author = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    cover = models.ImageField(upload_to = 'covers/', blank = True)
    publication_date = models.DateField(null=True, blank = True)
    rating = models.FloatField(null=True, blank = True)
    stock = models.IntegerField(null=True, blank = True)
    formats = models.CharField(max_length=4, choices=FORMATS_CHOICES, default='PB', blank=True)
    summary = models.TextField(null=True, blank = True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='books')

    class Meta: 
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args = [str(self.id)])
    

class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete = models.CASCADE,
        related_name = 'reviews',
    )
    review = models.CharField(max_length = 255)  
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        related_name = 'reviews',
    )
    def __str__(self):
        return self.review
