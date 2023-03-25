from rest_framework.routers import DefaultRouter

from ..viewsets import CommentViewSet

comment_router = DefaultRouter()

comment_router.register(
    prefix='comments',
    viewset=CommentViewSet,
    basename='comments'
)
