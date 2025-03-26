from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .swagger import schema_view
from .views import BookViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]

urlpatterns += [
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger_docs"),
]
