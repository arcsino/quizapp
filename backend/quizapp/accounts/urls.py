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
    path("registration/", UserRegistrationAPIView.as_view(), name="registration"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("detail/", UserDetailAPIView.as_view(), name="detail"),
    path("update/", UserUpdateAPIView.as_view(), name="update"),
    path("password_change/", PasswordChangeAPIView.as_view(), name="password_change"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
]
