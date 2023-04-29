from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission): # делаем ограничение прав доступа на уровне всего запроса
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: # если пришедший запрос безопасный - т.е. принадлежит
            # коллекции  SAFE_METHODS (запросы только на чтение данных)
            return True # то предоставляем права доступа для всех
        # иначе, проверяем, что пользователь вошел как администратор
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user # если user из БД равен пользователю request.user, который пришел с запросом,
                                        # тогда даем доступ