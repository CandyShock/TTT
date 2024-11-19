import requests
import stripe
from django.conf import settings
from rest_framework import status

stripe.api_key = f"{settings.STRIPE_API_KEY}"


def convert_currencies(rub_price):
    usd_price = 0
    response = requests.get(
        f'{settings.CUR_API_URL}/v3/latest?apikey={settings.CUR_API_KEY}'
    )
    if response.status_code == status.HTTP_200_OK:
        usd_rate = response.json()['data']['RUB']['value']
        usd_price = rub_price * usd_rate
    return usd_price


def create_product_course(name, description):
    '''Создание продукта в страйпе и присвоение id'''
    course = stripe.Product.create(
        name=name,
        description=description,
    )
    return course.get('id')


def create_price(amount, product):
    """создание платежа"""
    price = stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        nickname="Покупка",
        product=product,
    )
    return price


def create_session(price):
    """Создание сессии"""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/success",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
