from django.conf import settings
from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Subscription(models.Model):
    """подписка привязана к владельцу, отображается как и уроки списком в листе курсов под меткой sub_stat"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    sub_name = models.CharField(max_length=25, verbose_name='Название подписки', **NULLABLE)
    sub_status = models.BooleanField(default=True, verbose_name='Признак подписки')

    def __str__(self):
        return f"{self.sub_name} {self.sub_status}"

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class Kurs(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                              verbose_name='Владелец')
    name = models.CharField(max_length=30, verbose_name='Название')
    text = models.TextField(max_length=100, verbose_name='Описание')
    image = models.ImageField(upload_to='kurs/', verbose_name='Картинка', **NULLABLE)
    sub = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='sub', **NULLABLE)
    amount = models.IntegerField(default=1000, verbose_name='цена')
    product_id = models.CharField(max_length=200, verbose_name='ID курса', **NULLABLE)

    def __str__(self):
        return f"{self.name} {self.text}"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                              verbose_name='Владелец')
    name = models.CharField(max_length=30, verbose_name='Название')
    text = models.TextField(max_length=100, verbose_name='Описание')
    image = models.ImageField(upload_to='lesson/', verbose_name='Картинка', **NULLABLE)
    url = models.URLField(max_length=50, verbose_name='Ссылка на видео')
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE, related_name='lesson', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payment(models.Model):
    payment_method = [
        ('cash', 'наличные'),
        ('translation', 'перевод')
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                              verbose_name='Владелец')
    datetime = models.DateTimeField(default=timezone.now, verbose_name='Дата и время оплаты')
    kurse = models.ForeignKey(Kurs, on_delete=models.CASCADE, related_name="kurs", **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lesson",
                               **NULLABLE)
    pay_method = models.CharField(verbose_name='Способ оплаты', choices=payment_method, max_length=15)
    pay_sum = models.IntegerField(verbose_name='Сумма оплаты')
    payment_session = models.CharField(max_length=200, verbose_name='Сессия платежа', **NULLABLE)
    payment_url = models.URLField(max_length=400, verbose_name='Ссылка для оплаты', **NULLABLE)

    def __str__(self):
        return f'{self.owner}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
