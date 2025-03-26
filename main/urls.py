from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import BookViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Library API",
        default_version='v1',
        description="Документация для API библиотеки",
        contact=openapi.Contact(email="support@library.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('api/docs/', include_docs_urls(title='Library API', permission_classes=[AllowAny])),
]

urlpatterns += [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_docs'),
]