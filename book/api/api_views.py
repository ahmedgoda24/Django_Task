from ..models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from book.api.pagination import DefaultPagination
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultPagination