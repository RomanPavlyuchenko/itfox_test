from django.utils import timezone
from rest_framework import serializers

from ..models import News
from .comment import CommentListSerializer


class NewsSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(many=True)
    comments_count = serializers.IntegerField()
    likes_count = serializers.IntegerField()

    class Meta:
        model = News
        fields = (
            'id', 'author', 'create_date', 'title',
            'text', 'comments_count', 'likes_count', 'comments'
        )


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'text')

    def create(self, validated_data: dict) -> News:
        validated_data['author'] = self.context['request'].user
        validated_data['create_date'] = timezone.now()
        return super().create(validated_data)
