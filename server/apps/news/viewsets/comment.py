from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import QuerySet

from ..models import Comment, News
from ..serializers import CommentCreateSerializer, CommentSerializer
from ..permissions import IsAdminOrAuthor


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAdminOrAuthor)

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update',):
            return CommentCreateSerializer
        return super().get_serializer_class()

    def get_queryset(self) -> QuerySet:
        if self.action == 'create':
            News.objects.all()
        return Comment.objects.all()
