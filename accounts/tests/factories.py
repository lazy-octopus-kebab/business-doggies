import factory

from django.core.files.base import ContentFile
from django.contrib.auth.models import Group

from accounts.models import User, Client, Sitter


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    phone_number = factory.Faker('phone_number')
    password = factory.PostGenerationMethodCall(
        'set_password',
        factory.faker.faker.Faker().password()
    )

    class Meta:
        model = User


class ClientFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Client


class SitterFactory(factory.django.DjangoModelFactory):
    description = factory.Faker('sentence')

    class Meta:
        model = Sitter


class UserClientFactory(UserFactory):
    is_client = True
    client = factory.RelatedFactory(
        ClientFactory,
        factory_related_name='user'
    )

    @factory.post_generation
    def set_group(obj, create, extracted, **kwargs):
        if not create:
            return
        group = Group.objects.get(name='Clients')
        obj.groups.add(group)
        return
        

class UserSitterFactory(UserFactory):
    is_sitter = True
    sitter = factory.RelatedFactory(
        SitterFactory,
        factory_related_name='user'
    )

    @factory.post_generation
    def set_group(obj, create, extracted, **kwargs):
        if not create:
            return
        group = Group.objects.get(name='Sitters')
        obj.groups.add(group)
        return
