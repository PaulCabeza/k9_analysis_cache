from django.contrib import admin

# Register your models here.

from cachemanager.models import AnalysisCacheEntry


@admin.register(AnalysisCacheEntry)
class AnalysisCacheEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'partition_id', 'valid_until')