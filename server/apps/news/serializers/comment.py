from django.utils import timezone
from rest_framework import serializers

from ..models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'author', 'create_date', 'text', 'news')


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'create_date', 'text')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('title', 'news', 'id')

    def create(self, validated_data: dict) -> Comment:
        validated_data['author'] = self.context['request'].user
        validated_data['create_date'] = timezone.now()
        return super().create(validated_data)
