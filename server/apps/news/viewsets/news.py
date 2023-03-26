from rest_framework import viewsets, pagination
from django.db.models import QuerySet, Count, Prefetch, Subquery, OuterRef
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from ..models import News, Like, Comment
from ..serializers import NewsSerializer, NewsCreateSerializer, CommentListSerializer
from ..permissions import IsAdminOrAuthor


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, IsAdminOrAuthor)
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 10
    comments_limit = 10

    def get_queryset(self) -> QuerySet:
        queryset = News.objects.all()
        if self.action in ('retrieve', 'list', 'set_news_like'):
            subquery = Subquery(Comment.objects.filter(
                news_id=OuterRef('news_id')
            ).values_list('id')[:self.comments_limit])
            queryset = queryset.prefetch_related(
                Prefetch(
                    'comments',
                    queryset=Comment.objects.filter(id__in=subquery)
                ),
                'likes'
            ).annotate(
                comments_count=Count('comments', distinct=True),
                likes_count=Count('likes', distinct=True)
            )
        elif self.action == 'get_news_comments':
            queryset = queryset.prefetch_related('comments')
        return queryset

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update',):
            return NewsCreateSerializer
        elif self.action == 'get_news_comments':
            return CommentListSerializer
        return super().get_serializer_class()

    @action(methods=('GET',), detail=False, url_path='(?P<pk>[^/.]+)/comments',)
    def get_news_comments(self, request: Request, pk=None) -> Response:
        news_comments = self.get_object().comments.all()
        page = self.paginate_queryset(news_comments)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(news_comments, many=True)
        return Response(serializer.data)

    @action(methods=('GET',), detail=False, url_path='(?P<pk>[^/.]+)/(un)?like',)
    def set_news_like(self, request: Request, pk=None) -> Response:
        url_like = request.get_full_path().split('/')[-2]
        obj = self.get_object()
        like = obj.likes.filter(user=request.user)

        if url_like == 'like' and not like:
            Like.objects.create(user=request.user, news=obj)

        if url_like == 'unlike' and like:
            like.delete()

        return super().retrieve(request, pk)
