from django.urls import path   
from .views import BookListView, BookDetailView, SearchResultsListView, AddBookView

urlpatterns = [
    path('', BookListView.as_view(), name = 'book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name = 'book_detail'),
    path('search', SearchResultsListView.as_view(), name = 'search_results'),
    path('add-book', AddBookView.as_view(), name = 'add_book')
]