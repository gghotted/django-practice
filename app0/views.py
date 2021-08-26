from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

from .authentication import SimpleTokenAuthentication
from .serializers import UserListSerializer
from .models import User


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username='gypark')
        refresh_token = RefreshToken.for_user(user)
        user.token = str(refresh_token)
        user.save()
        return Response({
            'access_token': str(refresh_token.access_token),
            'refresh_token': str(refresh_token)
        })


class UserListView(APIView):
    authentication_classes = (SimpleTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserListSerializer(queryset, many=True)

        return Response(serializer.data)
