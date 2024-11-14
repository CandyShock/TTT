from rest_framework import serializers

from main.models import Kurs, Lesson, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class KursSerialaizer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=True, read_only=True)
    # kurs = PaymentSerializer(many=True)
    lesson_count = serializers.SerializerMethodField()

    #
    def get_lesson_count(self, obj):
        return obj.lesson.count()

    class Meta:
        model = Kurs
        fields = '__all__'



