from django.contrib.auth.backends import BaseBackend, get_user_model
from users.models import User
class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None,password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            if not user:
                return None
            if user.check_password(password):
                return user
        except:
            return None
        return None 

    def get_user(self, user_id):
        model = get_user_model()
        try:
            return model.objects.get(pk=user_id)
        except:
            return None
