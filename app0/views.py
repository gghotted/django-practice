from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from django.views.generic import TemplateView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class KakaoLoginView(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)


class Index(TemplateView):
    template_name = 'app0/login.html'


