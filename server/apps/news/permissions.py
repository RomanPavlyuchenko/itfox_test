from rest_framework import permissions


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAdminOrAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            obj.author == request.user or
            request.user.is_admin
        )
