from rest_framework import viewsets, pagination
from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated

from ..models import News
from ..serializers import NewsSerializer, NewsCreateSerializer
from ..permissions import IsAdminOrAuthor


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, IsAdminOrAuthor)
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 10

    def get_queryset(self) -> QuerySet:
        queryset = News.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update',):
            return NewsCreateSerializer
        return super().get_serializer_class()
