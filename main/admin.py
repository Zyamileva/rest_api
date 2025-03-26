from django.contrib import admin


from main.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author","genre","publication_year","created_at")
    list_filter = ("title", "author")

