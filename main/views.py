from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from main.models import Kurs, Lesson, Payment
from main.serialaizers import KursSerialaizer, LessonSerializer, PaymentSerializer


class KursViewSet(viewsets.ModelViewSet):
    serializer_class = KursSerialaizer
    queryset = Kurs.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('pay_method', 'kurse', 'lesson')
    ordering_fields = 'datetime'
