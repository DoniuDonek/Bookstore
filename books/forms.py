from django import forms
from .models import Book

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'cover', 'publication_date', 'rating', 'stock', 'formats', 'summary']
        exclude = ['posted_by']