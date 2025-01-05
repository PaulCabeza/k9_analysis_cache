from django.contrib import admin
from datetime import datetime
# Register your models here.

from cachemanager.models import AnalysisCacheEntry


@admin.register(AnalysisCacheEntry)
class AnalysisCacheEntryAdmin(admin.ModelAdmin):
    list_display = ('partition_id', 'truncated_id', 'data', 'formatted_valid_until')

    # limits characters shown on display view
    def truncated_id(self, obj):
        max_length = 60
        return (obj.id[:max_length] + '...') if len(obj.id) > max_length else obj.id
    
    truncated_id.short_description = 'ID'

    # Converts valid until int to human readable version
    def formatted_valid_until(self, obj):
        return datetime.fromtimestamp(int(obj.valid_until)).strftime('%Y-%m-%d %H:%M:%S')

    formatted_valid_until.short_description = 'Valid Until'