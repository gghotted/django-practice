from django.core.exceptions import ObjectDoesNotExist

from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions

from rest_framework_simplejwt.tokens import AccessToken

from .models import User


class SimpleTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, token):
        try:
            token = AccessToken(token)
            user = User.objects.get(id=token['user_id'])
        except Exception as e:
            raise exceptions.AuthenticationFailed(str(e))

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return (user, str(token))
