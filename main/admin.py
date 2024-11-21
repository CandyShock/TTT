from django.contrib import admin

from main.models import Kurs, Subscription


@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = ('sub', 'id')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('owner', 'id', 'sub_status', 'sub_name')
