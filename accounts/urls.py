from django.urls import path

from .views import (
    ClientSingUpView,
    SitterSingUpView,
    UserLoginView,
    UserProfileView,
)


app_name = 'accounts'
urlpatterns = [
    # ex: /accounts/login
    path('login/', UserLoginView.as_view(), name='login'),

    # ex: /accounts/client_singup
    path('client_singup/', ClientSingUpView.as_view(), name='client_singup'),

    # ex: /accounts/sitter_singup
    path('sitter_singup/', SitterSingUpView.as_view(), name='sitter_singup'),

    # ex: /accounts/profile
    path('profile/', UserProfileView.as_view(), name='profile'),

    # ex: /accounts/profile/1
    path('profile/<int:id>/', UserProfileView.as_view(), name='profile'),
]
