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
            if request.user.is_admin:
                return True
            if request.user == obj.user:
                return True
        return False
  

class OwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow read-only access to all users
        if request.method in SAFE_METHODS:
            return True

        # Allow write access only to authenticated users
        if request.user and request.user.is_authenticated:
            # Allow the owner of the review to modify or delete it
            if request.user.is_admin:
                return True
            return obj.user == request.user
        
        return False

    def has_permission(self, request, view):
        # Allow authenticated users to create reviews
        if request.method == 'POST':
            return request.user and request.user.is_authenticated
        
        return super().has_permission(request, view)


class IsAdminOrOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        else:
            return False
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.is_admin:
                return True
            if request.user == obj.user:
                return True
        return False
