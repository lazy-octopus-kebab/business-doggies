from allauth.account.auth_backends import AuthenticationBackend

from .models import User


class AuthBackend(AuthenticationBackend):
    """Authentication class to login with phone number."""

    def authenticate(self, request, **credentials):
        ret = self._authenticate_by_email(**credentials)
        if not ret:
            ret = self._authenticate_by_phone_number(**credentials)
        return ret
        

    def _authenticate_by_phone_number(self, **credentials):
        phone_number = credentials.get('phone_number')
        password = credentials.get('password')

        user = User

        if phone_number is None or password is None:
            return

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
        else:
            if self._check_password(user, password):
                return user