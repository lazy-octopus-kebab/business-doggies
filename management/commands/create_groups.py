from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

from offers.models import Offer

GROUPS = {
    'Clients': {
        Offer: ['add', 'view'],
    },
    'Sitters': {
        Offer: ['change', 'view'],
    },
}

class Command(BaseCommand):
    help = "Create default groups with permissions"

    def handle(self, *args, **kwargs):
        for group_name in GROUPS:
            group, created = Group.objects.get_or_create(name=group_name)

            for model in GROUPS[group_name]:
                for perm in GROUPS[group_name][model]:
                    codename = perm + '_' + model._meta.model_name

                    try:
                        perm = Permission.objects.get(codename=codename)
                        group.permissions.add(perm)
                        print("Adding permission " + codename + " to group " + group)
                    except Permission.DoesNotExist:
                        print("Permission " + codename + " not found")