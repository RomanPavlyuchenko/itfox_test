from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Comment
from ..serializers import CommentCreateSerializer, CommentSerializer
from ..permissions import IsAdminOrAuthor


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAdminOrAuthor)

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update',):
            return CommentCreateSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        return Comment.objects.all()
