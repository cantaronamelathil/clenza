# from rest_framework.permissions import permissions
# from useracount.models import Accounts
# class Is_vendor(permissions.BasePermission):
#     def has_permission(self,request,view):
#      def has_permission(self, request, view):
#         # Allow read-only access for all users.
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         # Only allow write access for vendor users.
#         return request.user and request.user.role == Accounts.Roles.VENDOR