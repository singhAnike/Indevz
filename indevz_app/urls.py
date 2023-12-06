from django.urls import path
from .views import SignupAPIView, SigninAPIView, UsersApi

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='api-signup'),
    path('signin/', SigninAPIView.as_view(), name='api-signin'),
    path('users/',  UsersApi.as_view(), name='api-users'),
]
