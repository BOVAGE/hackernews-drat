from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAPICREATEDORREADONLY(BasePermission):
    """Object-level permission to only allow is_api_created items to be deleted and updated
    Assumes the model instance has an `is_api_created` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.is_api_created is True
