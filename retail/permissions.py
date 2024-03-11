from rest_framework.permissions import BasePermission

class IsActive(BasePermission):
    message = 'Ваша учетная запись не активна'

    def has_permission(self, request, view):
        if request.user.is_active == True:
            return True
