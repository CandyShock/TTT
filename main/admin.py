from django.contrib import admin

from main.models import Kurs


@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = ('sub', 'id')
