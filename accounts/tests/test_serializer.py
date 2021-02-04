from django.test import TestCase

from accounts.serializers import UserSerializer
from .factories import UserClientFactory, UserSitterFactory


class UserSerializerTest(TestCase):

    def test_client_fields(self):
        user = UserClientFactory()
        serializer = UserSerializer(user)

        for field in [
            'id',
            'email',
            'phone_number',
            'first_name',
            'last_name',
        ]:
            self.assertEqual(
                serializer.data[field],
                getattr(user, field)
            )

        for field in [
        ]:
            self.assertEqual(
                serializer.data['client'][field],
                getattr(user.client, field)
            )

    def test_sitter_fields(self):
        user = UserSitterFactory()
        serializer = UserSerializer(user)

        for field in [
            'id',
            'email',
            'phone_number',
            'first_name',
            'last_name',
        ]:
            self.assertEqual(
                serializer.data[field],
                getattr(user, field)
            )

        for field in [
            'description'
        ]:
            self.assertEqual(
                serializer.data['sitter'][field],
                getattr(user.sitter, field)
            )
            
