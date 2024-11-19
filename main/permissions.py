from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsOwnerorStaff(BasePermission):
    message = "Вы не имеете прав"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODER:
            return True

        return request.user == view.get_object().owner
