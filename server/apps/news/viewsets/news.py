from rest_framework import viewsets, pagination
from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from ..models import News
from ..serializers import NewsSerializer, NewsCreateSerializer, CommentListSerializer
from ..permissions import IsAdminOrAuthor


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, IsAdminOrAuthor)
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 10

    def get_queryset(self) -> QuerySet:
        queryset = News.objects.all().prefetch_related('comments')
        return queryset

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update',):
            return NewsCreateSerializer
        elif self.action == 'get_news_comments':
            return CommentListSerializer
        return super().get_serializer_class()

    @action(methods=('GET',), detail=False, url_path='(?P<pk>[^/.]+)/comments',)
    def get_news_comments(self, request: Request, pk=None) -> Response:
        queryset = self.get_object().comments.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
