from django.contrib import admin

# Register your models here.

from cachemanager.models import AnalysisCacheEntry

admin.site.register(AnalysisCacheEntry)