from rest_framework.routers import DefaultRouter

from ..viewsets import NewsViewSet

news_router = DefaultRouter()

news_router.register(
    prefix='news',
    viewset=NewsViewSet,
    basename='news'
)
