from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from .models import Book
from .serializers import BookSerializer


class CustomPagination(PageNumberPagination):
    """
    Custom pagination class.

    Sets the page size, page size query parameter, and maximum page size.
    """

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.

    Provides API endpoints for listing, retrieving, creating, updating, and deleting books.
    """

    queryset = Book.objects.all().order_by("-created_at")
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["author", "genre", "publication_year"]
    search_fields = ["title"]

    def get_permissions(self):
        """
        Gets the permissions for the current action.

        Allows any user to destroy a book.
        """
        if self.action == "destroy":
            return [permissions.AllowAny()]
        return super().get_permissions()
