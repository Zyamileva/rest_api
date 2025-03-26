from django.contrib import admin


from main.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Book model.

    Customizes the list display and filter options for the Book model in the admin interface.
    """

    list_display = ("title", "author", "genre", "publication_year", "created_at")
    list_filter = ("title", "author")
