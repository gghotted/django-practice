from django.urls import path
from .views import *


urlpatterns = [
    path('login/kakao', KakaoLoginView.as_view()),
    path('', Index.as_view()),
]
