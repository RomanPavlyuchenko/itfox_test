from django.urls import path, include

urlpatterns = [
    path('auth/', include('apps.users.urls.auth')),
    path('users/', include('apps.users.urls.user')),
    path('news/', include('apps.news.urls'))
]
