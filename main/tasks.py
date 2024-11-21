from datetime import datetime

import pytz
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from requests import Response

from main.models import Kurs, Subscription


@shared_task
def send_massage_about_update(course_id):
    """отправка письма при обновлении курса"""
    course = Kurs.objects.filter(id=course_id)
    for i in course:
        if i.sub != None:
            send_mail(
                subject='Обновление',
                message='Ваш курс был обновлен',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[f'{i.sub.owner}'],
                fail_silently=False
            )
