from rest_framework import serializers

from main.models import Kurs, Lesson, Payment, Subscription
from main.servives import convert_currencies
from main.validators import url_validator


class SubscripeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    url = serializers.URLField(validators=[url_validator])

    class Meta:
        model = Lesson
        fields = '__all__'


class KursSerialaizer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=True, read_only=True)
    # kurs = PaymentSerializer(many=True)
    lesson_count = serializers.SerializerMethodField()
    sub = SubscripeSerializer(read_only=True)
    usd_price = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lesson.count()

    def get_usd_price(self, obj):
        return convert_currencies(obj.amount)

    class Meta:
        model = Kurs
        fields = '__all__'
