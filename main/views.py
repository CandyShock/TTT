from django.shortcuts import render
import stripe
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from main.models import Kurs, Lesson, Payment
from main.paginator import MyPagePagination
from main.permissions import IsOwnerorStaff
from main.serialaizers import KursSerialaizer, LessonSerializer, PaymentSerializer, SubscripeSerializer
from main.servives import create_product_course, create_price, create_session
from main.tasks import send_massage_about_update


class KursViewSet(viewsets.ModelViewSet):
    serializer_class = KursSerialaizer
    queryset = Kurs.objects.all()
    pagination_class = MyPagePagination

    def perform_create(self, serializer):
        course = serializer.save()
        product = create_product_course(course.name, course.text)
        course.product_id = product
        course.save()

    def perform_update(self, serializer):
        course = serializer.save()
        send_massage_about_update.delay(course_id=course.id)
        course.save()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        """Привязка владельца"""
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = MyPagePagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerorStaff]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerorStaff]

    def post(self, request):
        send_massage_about_update.delay()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('pay_method', 'kurse', 'lesson')
    ordering_fields = 'datetime'

    def perform_create(self, serializer):
        new_payment = serializer.save()
        if new_payment.kurse:
            product = new_payment.kurse.product_id
        price = create_price(new_payment.pay_sum, product)
        session, payment_url = create_session(price)
        new_payment.payment_session = session
        new_payment.payment_url = payment_url
        new_payment.save()


class SubscripeViewSet(viewsets.ModelViewSet):
    serializer_class = SubscripeSerializer
    queryset = Kurs.objects.all()
