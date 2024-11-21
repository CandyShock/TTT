from django.utils import timezone
from celery import shared_task
from dateutil.relativedelta import relativedelta

from users.models import User


@shared_task
def check_user_login():
    now = timezone.now()
    month_ago = now - relativedelta(months=1)
    user = User.objects.filter(last_login__lte=month_ago)
    for i in user:
        i.is_active = False
        i.save()
