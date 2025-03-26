from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Book
from .serializers import BookSerializer
import django_filters

class BookFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(lookup_expr='icontains')  # Фільтрація по автору
    publication_year = django_filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['author', 'publication_year']