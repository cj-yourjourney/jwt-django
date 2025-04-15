from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_details(request):
    """
    A protected function-based view that returns user details
    """
    user = request.user

    # Basic user information
    user_data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "is_active": user.is_active,
        "date_joined": user.date_joined,
        "last_login": user.last_login,
    }

    return Response(
        {
            "user": user_data,
            "message": f"Hello, {user.username}! This is your user profile.",
        }
    )
