from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin2@sky.pro',
            first_name='Admin',
            last_name='SkyPro',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('1')
        user.save()
