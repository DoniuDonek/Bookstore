from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.db.models import Q

from .models import Book
from .forms import AddBookForm

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = "books.special_status"
    queryset = Book.objects.all().prefetch_related('reviews__author',)


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(summary__icontains=query)
        )


class AboutPageView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/about.html'
    context_object_name = 'recent_books'
    queryset = Book.objects.order_by('-publication_date')[:5] 
    login_url = 'account_login'


class AddBookView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = AddBookForm
    template_name = 'books/add_book.html'
    success_url = '/books/' 

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
    
