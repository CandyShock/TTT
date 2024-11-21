from dateutil.relativedelta import relativedelta
from django.utils import timezone

from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand

from main.models import Kurs
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        now = timezone.now()
        month_ago = now - relativedelta(months=1)
        user = User.objects.filter(last_login__lte=month_ago)
        print(user)
        for i in user:
            print(i.is_active)
            i.is_active = False
            i.save()