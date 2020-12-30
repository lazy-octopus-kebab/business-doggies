from io import StringIO

from django.test import TestCase
from django.core.management import call_command
from django.contrib.auth.models import Group


class CreategroupsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.out = StringIO()
        call_command('creategroups', verbosity=3, stdout=cls.out)

    def test_verbosity(self):
        out = StringIO()
        call_command('creategroups', verbosity=0, stdout=out)

        self.assertEqual('', out.getvalue())

    def test_groups(self):
        self.assertTrue(Group.objects.filter(name='Clients').exists())
        self.assertTrue(Group.objects.filter(name='Sitters').exists())

    def test_clients_permissions(self):
        group = Group.objects.get(name='Clients')

        self.assertTrue(group.permissions.filter(codename='add_offer', content_type__app_label='offers', content_type__model='offer').exists())
        self.assertTrue(group.permissions.filter(codename='view_offer', content_type__app_label='offers', content_type__model='offer').exists())
        self.assertTrue(group.permissions.filter(codename='add_pet', content_type__app_label='pets', content_type__model='pet').exists())
        self.assertTrue(group.permissions.filter(codename='view_pet', content_type__app_label='pets', content_type__model='pet').exists())
        self.assertTrue(group.permissions.filter(codename='view_review', content_type__app_label='reviews', content_type__model='review').exists())
        self.assertTrue(group.permissions.filter(codename='add_reviewrating', content_type__app_label='reviews', content_type__model='reviewrating').exists())

    def test_sitters_permissions(self):
        group = Group.objects.get(name='Sitters')

        self.assertTrue(group.permissions.filter(codename='change_offer', content_type__app_label='offers', content_type__model='offer').exists())
        self.assertTrue(group.permissions.filter(codename='view_offer', content_type__app_label='offers', content_type__model='offer').exists())
        self.assertTrue(group.permissions.filter(codename='view_pet', content_type__app_label='pets', content_type__model='pet').exists())
        self.assertTrue(group.permissions.filter(codename='add_review', content_type__app_label='reviews', content_type__model='review').exists())
        self.assertTrue(group.permissions.filter(codename='view_reviewrating', content_type__app_label='reviews', content_type__model='reviewrating').exists())
    
    def test_output(self):
        self.assertIn('Adding permission', self.out.getvalue())
        self.assertIn('pet', self.out.getvalue())
        self.assertIn('offer', self.out.getvalue())
        self.assertIn('review', self.out.getvalue())
        self.assertIn('to group', self.out.getvalue())
        self.assertIn('Clients', self.out.getvalue())
        self.assertIn('Sitters', self.out.getvalue())