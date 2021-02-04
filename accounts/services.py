from django.contrib.auth.models import Group

from .models import User, ClientMore, SitterMore


def set_user_type(
    user: User,
    is_client: bool = False,
    is_sitter: bool = False,
    commit: bool = True
) -> None:
    """
    Service for setting up User type and adding him to the
    appropriate Groups (Clients or Sitters)
    """

    user.is_client = is_client
    user.is_sitter = is_sitter

    if commit:
        user.save()

    if is_client:
        group = Group.objects.get(name='Clients')
        user.groups.add(group)
        client = ClientMore.objects.create(user=user)
        client.save()

    if is_sitter:
        group = Group.objects.get(name='Sitters')
        user.groups.add(group)
        sitter = SitterMore.objects.create(user=user)
        sitter.save()
