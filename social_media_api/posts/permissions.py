from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Read for anyone; write only for the object owner.
    Works for Post (author) and Comment (author).
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # obj.author exists for both Post and Comment
        return getattr(obj, "author_id", None) == getattr(request.user, "id", None)
