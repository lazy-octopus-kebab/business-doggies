import logging

from django.apps import AppConfig
from django.db.models.signals import post_migrate


logger = logging.getLogger(__name__)


def create_groups(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission

    from offers.models import Offer
    from pets.models import Pet
    from reviews.models import Review, ReviewRating


    GROUPS = {
        'Clients': {
            Offer: ['add', 'view'],
            Pet: ['add', 'view'],
            Review: ['view'],
            ReviewRating: ['add'],
        },
        'Sitters': {
            Offer: ['change', 'view'],
            Pet: ['view'],
            Review: ['add'],
            ReviewRating: ['view'],
        },
    }

    for group_name in GROUPS:
        group, created = Group.objects.get_or_create(name=group_name)

        for model in GROUPS[group_name]:
            for perm in GROUPS[group_name][model]:
                codename = perm + '_' + model._meta.model_name

                try:
                    perm = Permission.objects.get(codename=codename)
                    group.permissions.add(perm)
                    logger.info("Adding permission " + codename + " to group " + group.__str__())
                except Permission.DoesNotExist:
                    logger.error("Permission " + codename + " not found")


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        post_migrate.connect(create_groups, sender=self)
