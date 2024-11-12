from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Kurs(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    text = models.TextField(max_length=100, verbose_name='Описание')
    image = models.ImageField(upload_to='kurs/', verbose_name='Картинка', **NULLABLE)

    def __str__(self):
        return f"{self.name} {self.text}"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    text = models.TextField(max_length=100, verbose_name='Описание')
    image = models.ImageField(upload_to='lesson/', verbose_name='Картинка', **NULLABLE)
    url = models.URLField(max_length=50, verbose_name='Ссылка на видео')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
