from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """
    Изменять чужие записи может только автор.
    И аутентифицированный пользователь может воспользоваться методами из:
    SAFE_METHODS
    """
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class UserIsAuthenticated(permissions.IsAuthenticated):
    ...


class UserIsAuthenticatedOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    ...
