from django.core.exceptions import ObjectDoesNotExist

from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions

from rest_framework_simplejwt.tokens import AccessToken

from .models import User


class SimpleTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, token):
        try:
            token = AccessToken(token)
        except Exception as e:
            raise exceptions.AuthenticationFailed(str(e))

        try:
            user = User.objects.get(id=token['user_id'])
        except ObjectDoesNotExist:
            raise exceptions.AuthenticationFailed('Dose not exist user.')

        if not user.token:
            raise exceptions.AuthenticationFailed('User logged out.')

        return (user, str(token))
