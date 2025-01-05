from django.db import models
from datetime import datetime, timezone

# Create your models here.

class AnalysisCacheEntry(models.Model):
    id = models.CharField(max_length=127, unique=True, primary_key=True)
    partition_id = models.CharField(max_length=30)
    data = models.JSONField(null=True, blank=True)
    valid_until = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'analysis_cache'
        managed = False
        indexes = [
            models.Index(fields=['partition_id'], name='analysis_cache_partition_idx')
        ]

    @classmethod
    def load_by_partition(cls, partition_id):
        now = int(datetime.now(timezone.utc).timestamp())
        return cls.objects.filter(
            partition_id=partition_id,
            valid_until__gt=now
        )
