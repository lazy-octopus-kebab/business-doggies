from io import StringIO

from django.test import TestCase
from django.core.management import call_command

from accounts.models import (
    UserManager,
    User,
    Client,
    Sitter
)


class UserManagerTest(TestCase):
    def test_create_client_user(self):
        user = User.objects.create_user(
            email='email@mail.com',
            phone_number='+1 215-818-1895',
            password='password',
            is_client=True,
        )

        self.assertEqual(user.email, 'email@mail.com')
        self.assertEqual(user.phone_number, '+1 215-818-1895')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_client)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.groups.filter(name='Clients').exists())
        self.assertEqual(Client.objects.get(user_id=user.id).user, user)

    def test_create_sitter_user(self):
        user = User.objects.create_user(
            email='email@mail.com',
            phone_number='+1 215-818-1895',
            password='password',
            is_sitter=True,
        )

        self.assertEqual(user.email, 'email@mail.com')
        self.assertEqual(user.phone_number, '+1 215-818-1895')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_sitter)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.groups.filter(name='Sitters').exists())
        self.assertEqual(Sitter.objects.get(user_id=user.id).user, user)

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email='email@mail.com',
            phone_number='+1 215-818-1895',
            password='password',
        )

        self.assertEqual(user.email, 'email@mail.com')
        self.assertEqual(user.phone_number, '+1 215-818-1895')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            email='email@mail.com',
            phone_number='+1 215-818-1895',
            password='password',
        )

    def test_get_absolute_url(self):
        user = User.objects.get(id=2)
        self.assertEqual(user.get_absolute_url(), '/accounts/profile/2/')

    def test_str(self):
        user = User.objects.get(id=2)
        self.assertEqual(str(user), 'email@mail.com')


class ClientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            email='email@mail.com',
            phone_number='+1 215-818-1895',
            password='password',
        )
        
    def test_create(self):
        Client.objects.create(user=User.objects.get(id=2))
        self.assertEqual(Client.objects.get(user_id=2).user, User.objects.get(id=2))


class SitterModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            email='email@mail.com',
            phone_number='+1 215-818-1895',
            password='password',
        )
        
    def test_create(self):
        Sitter.objects.create(user=User.objects.get(id=2))
        self.assertEqual(Sitter.objects.get(user_id=2).user, User.objects.get(id=2))

    def test_description(self):
        Sitter.objects.create(user=User.objects.get(id=2), description='Some text')
        self.assertEqual(Sitter.objects.get(user_id=2).description, 'Some text')
