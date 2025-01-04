from django.db import models

# Create your models here.

class AnalysisCacheEntry(models.Model):
    id = models.CharField(max_length=127, unique=True, primary_key=True)
    partition_id = models.CharField(max_length=30)
    data = models.JSONField(null=True, blank=True)
    valid_until = models.BigIntegerField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['partition_id'])
        ]
