from rest_framework import permissions


class IsUserorReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # READ permissions are allowed to any request;
        # we'll always allow GET, HEAD, or OPTION requests.
        if request.method in permissions.SAFE_METHODS:
            return True

#        Write permissions are allowed only to user that created Activity
        return obj.user == request.user


class IsReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False
