from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from main.models import Book


class BookAPITestCase(APITestCase):
    """
    Набір тестів для API книги.

    Тестує створення, отримання, оновлення та видалення книг.
    """

    def setUp(self):
        """Налаштування тестових даних"""
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        # Генеруємо токен для користувача
        self.token = Token.objects.create(user=self.user)
        token = Token.objects.get(user=self.user)
        print(token.key)

        # Створюємо API-клієнт
        self.client = APIClient()

        # Примусово автентифікуємо користувача через токен
        self.client.force_authenticate(user=self.user)
        # self.client.credentials(HTTP_AUTHORIZATION="token")

        # Створюємо тестову книгу
        self.book = Book.objects.create(
            title="Test Book", author="John Doe", genre="Fiction", publication_year=2022
        )
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"
        self.book_url = f"/api/books/{self.book.id}/"

    def test_create_book(self):
        """Перевірка створення книги"""
        data = {
            "title": "New Book",
            "author": "Author_1",
            "genre": "Non-fiction",
            "publication_year": 2023,
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_books_list(self):
        """Перевірка отримання списку книг"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_book_detail(self):
        """Перевірка отримання деталей книги"""
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_update_book(self):
        """Перевірка оновлення книги"""
        data = {"title": "Updated Title"}
        response = self.client.patch(self.book_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_delete_book(self):
        """Перевірка видалення книги"""
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
