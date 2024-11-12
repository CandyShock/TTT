# Generated by Django 5.1.3 on 2024-11-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='аватар'),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='страна'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='телефон'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='почта'),
        ),
    ]
