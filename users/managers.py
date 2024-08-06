from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("email is requred")
        if not password:
            raise ValueError("password is requred")

        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fields):
        if not email:
            raise ValueError("email is requred")
        if not password:
            raise ValueError("password is requred")

        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user




