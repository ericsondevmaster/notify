from django.contrib import admin
from . import models


@admin.register(models.Webhook)
class WebhookAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_type', 'event',)
    list_filter = ('event_type',)
