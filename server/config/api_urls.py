from django.urls import path, include

from apps.news.urls import news_router, comment_router

urlpatterns = [
    path('auth/', include('apps.users.urls.auth')),
    path('users/', include('apps.users.urls.user')),
    path('news/', include(news_router.urls)),
    path('comments/', include(comment_router.urls)),
]
