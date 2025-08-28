from django.urls import path
from .views import (
    UserRegistrationAPIView,
    LoginAPIView,
    UserDetailAPIView,
    UserUpdateAPIView,
    PasswordChangeAPIView,
    LogoutAPIView,
)


urlpatterns = [
    path(route="registration/", view=UserRegistrationAPIView.as_view()),
    path(route="login/", view=LoginAPIView.as_view()),
    path(route="detail/", view=UserDetailAPIView.as_view()),
    path(route="update/", view=UserUpdateAPIView.as_view()),
    path(route="password_change/", view=PasswordChangeAPIView.as_view()),
    path(route="logout/", view=LogoutAPIView.as_view()),
]
