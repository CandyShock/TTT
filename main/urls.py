from django.urls import path

from main.apps import MainConfig
from rest_framework.routers import DefaultRouter

from main.views import KursViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'Kurs', KursViewSet, basename='Kurs')

urlpatterns = [
                  path('lesson/create', LessonCreateAPIView.as_view(), name='create'),
                  path('lesson/', LessonListAPIView.as_view(), name='list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='detail'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete')

              ] + router.urls
