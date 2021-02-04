from django.urls import include, path

from rest_framework import routers

from allauth.account.views import LogoutView

from .api.viewsets import UserViewSet

from .views import (
    ClientSignUpView,
    SitterSignUpView,
    UserLoginView,
    UserProfileView,
)


app_name = 'accounts'

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # ex: /accounts/login/
    path(r'login/', UserLoginView.as_view(), name='login'),

    # ex: /accounts/logout/
    path(r'logout/', LogoutView.as_view(), name='logout'),

    # ex: /accounts/client_signup/
    path(r'client_signup/', ClientSignUpView.as_view(), name='client_signup'),

    # ex: /accounts/sitter_signup/
    path(r'sitter_signup/', SitterSignUpView.as_view(), name='sitter_signup'),

    # ex: /accounts/profile/
    path(r'profile/', UserProfileView.as_view(), name='profile'),

    # ex: /accounts/profile/1/
    path(r'profile/<int:pk>/', UserProfileView.as_view(), name='profile'),

    # API
    path(r'api/', include((router.urls)))
]
