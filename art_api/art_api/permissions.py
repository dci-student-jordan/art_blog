from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class IsStaffUser(BasePermission):
    """
    Custom permission to only allow staff users to access a view.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff

def get_or_create_token_for_user(username):

    user, created = User.objects.get_or_create(username=username)
    refresh = RefreshToken.for_user(user)

    # Access the access token (used for authentication) and refresh token (used for token refreshing)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    # Print or use the tokens as needed
    return (access_token, refresh_token)