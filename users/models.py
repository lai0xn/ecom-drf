from datetime import datetime, timezone
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.forms.fields import uuid
from django.utils.timezone import timedelta
import jwt
from .managers import UserManager
# Create your models here.


class User(AbstractUser,PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    objects = UserManager()
    is_admin = models.BooleanField(default=False)
    username = None
    full_name = models.CharField(max_length=50,null=False)
    email = models.EmailField(unique=True,null=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
   

    def generate_jwt(self):
        claims = {
            'id':str(self.id),
            'email':self.email, 
            'full_name':self.full_name,
            'exp':datetime.now(tz=timezone.utc) + timedelta(days=7)
        }
        token = jwt.encode(claims,settings.JWT_SECRET,algorithm="HS256")
        return token

