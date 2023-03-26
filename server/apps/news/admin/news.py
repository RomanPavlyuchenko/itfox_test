from django.contrib import admin

from ..models import News, Comment, Like


class CommentsInstanceInline(admin.TabularInline):
    model = Comment


class LikesInstanceInline(admin.TabularInline):
    model = Like


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'title')

    inlines = [CommentsInstanceInline, LikesInstanceInline]
