from rest_framework import permissions
from useracount.models import Accounts
class Is_Worker(permissions.BasePermission):
    def has_permission(self,request,view):
    #  def has_permission(self, request, view):
        # Allow read-only access for all users.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only allow write access for vendor users.
        return request.user and request.user.role == Accounts.Roles.WORKER