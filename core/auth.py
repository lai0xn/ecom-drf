from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from django.conf import settings
import jwt


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if auth_header:
            parts = auth_header.split(" ")
            if len(parts) != 2:
                return None
            token = parts[1]
            try:
                payload = jwt.decode(token,settings.JWT_SECRET,algorithms=["HS256"])
                user = get_user_model().objects.get(id=payload["id"])
                return (user,None)
            except:
                return None
        return None
