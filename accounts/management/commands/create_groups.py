from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

from offers.models import Offer
from pets.models import Pet
from reviews.models import Review, ReviewRating

GROUPS = {
    'Clients': {
        Offer: ['add', 'view'],
        Pet: ['add', 'view'],
        ReviewRating: ['add'],
    },
    'Sitters': {
        Offer: ['change', 'view'],
        Pet: ['view'],
        Review: ['add'],
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
                        self.stdout.write("Adding permission " + codename + " to group " + group.__str__())
                    except Permission.DoesNotExist:
                        self.stderr.write("Permission " + codename + " not found")