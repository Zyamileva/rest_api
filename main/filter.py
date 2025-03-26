from .models import Book
import django_filters


class BookFilter(django_filters.FilterSet):
    """
    FilterSet for filtering Book objects.

    Allows filtering by author (case-insensitive contains) and publication year.
    """

    author = django_filters.CharFilter(lookup_expr="icontains")  # Фільтрація по автору
    publication_year = django_filters.NumberFilter()

    class Meta:
        """Meta options for the BookFilter."""

        model = Book
        fields = ["author", "publication_year"]
