from django.db import models


class Book(models.Model):
    """
    Represents a book.

    Stores information about a book, including title, author, genre, publication year, and creation timestamp.
    """

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
