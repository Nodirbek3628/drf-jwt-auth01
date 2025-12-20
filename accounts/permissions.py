from rest_framework.permissions import BasePermission
from rest_framework import status

class IsAdmin(BasePermission):
    message = 'Siz admin emasz'
    def has_permission(self, request, view):
        return request.user and request.user.is_admin
    
    
class IsUser(BasePermission):
    message = 'Siz User emasz'
    
    def has_permission(self, request, view):
        return request.user and request.user.is_user
    
class IsManager(BasePermission):
    message = 'Siz Manager emasz'
    
    def has_permission(self, request, view):
        return request.user and request.user.is_manager