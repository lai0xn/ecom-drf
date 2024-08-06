from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request,view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            if request.user.is_admin:
                return True
        return False



class IsAuthenticated(BasePermission):
    def has_permission(self, request,view):
        if request.user.is_authenticated:
            return True
        return False



class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user == obj.user:
                return True
        return False
   

class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.is_admin:
                return True
            if request.user == obj.user:
                return True
        return False
