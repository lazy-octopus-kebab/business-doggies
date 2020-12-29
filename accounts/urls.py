from django.urls import path

from allauth.account.views import LogoutView

from .views import (
    ClientSignUpView,
    SitterSignUpView,
    UserLoginView,
    UserProfileView,
)


app_name = 'accounts'
urlpatterns = [
    # ex: /accounts/login/
    path('login/', UserLoginView.as_view(), name='login'),

    # ex: /accounts/logout/
    path('logout/', LogoutView.as_view(), name='logout'),

    # ex: /accounts/client_signup/
    path('client_signup/', ClientSignUpView.as_view(), name='client_signup'),

    # ex: /accounts/sitter_signup/
    path('sitter_signup/', SitterSignUpView.as_view(), name='sitter_signup'),

    # ex: /accounts/profile/
    path('profile/', UserProfileView.as_view(), name='profile'),

    # ex: /accounts/profile/1/
    path('profile/<int:id>/', UserProfileView.as_view(), name='profile'),
]
