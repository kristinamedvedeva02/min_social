from rest_framework.permissions import BasePermission


class IsMainHR(BasePermission):
    """
    Allows access only to staff of in certain office company.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


