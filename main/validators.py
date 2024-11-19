from rest_framework import serializers

acess_list = ['http://youtube.com']


def url_validator(value):
    if value.lower() not in acess_list:
        raise serializers.ValidationError('Недопустимая ссылка')