import pytest
from datetime import datetime, timezone
from cachemanager.models import AnalysisCacheEntry


@pytest.mark.django_db
class TestAnalysisCacheEntry:
    test_single_record = {
            'id': 'v1|AROA_111|test123456',
            'partition_id': 'AROA_111',
            'data': ['read-config'],
            'valid_until': int(datetime.now(timezone.utc).timestamp()) + 3600
        }

    def test_create_cache_entry(self):
        entry = AnalysisCacheEntry.objects.create(**self.test_single_record)

        assert entry.id == self.test_single_record['id']
        assert entry.partition_id == self.test_single_record['partition_id']
        assert entry.data == self.test_single_record['data']
        assert entry.valid_until == self.test_single_record['valid_until']

    def test_get_cache_entry_by_id(self):
        AnalysisCacheEntry.objects.create(**self.test_single_record)

        saved_entry = AnalysisCacheEntry.objects.get(id=self.test_single_record['id'])

        assert saved_entry.id == self.test_single_record['id']
        assert saved_entry.partition_id == self.test_single_record['partition_id']
        assert saved_entry.data == self.test_single_record['data']
        assert saved_entry.valid_until == self.test_single_record['valid_until']

    def test_get_single_entry_by_partition_id_if_until_valid(self):
        now = int(datetime.now(timezone.utc).timestamp())
        test_data = [
            {
                'id': 'v1|AROA_333|test1234567890',
                'partition_id': 'AROA_333',
                'data': ['read-config'],
                'valid_until': now + 7200  # valid
            },
            {
                'id': 'v1|AROA_333|test12345678900',
                'partition_id': 'AROA_333',
                'data': ['read-config', 'write-config'],
                'valid_until': now - 7200  # not valid
            },
        ]

        AnalysisCacheEntry.objects.create(**test_data[0])
        AnalysisCacheEntry.objects.create(**test_data[1])

        partition_id = test_data[0]['partition_id']
        saved_entries_count = AnalysisCacheEntry.load_by_partition(partition_id=partition_id).count()
        # only valid entry should be returned
        assert saved_entries_count == 1

        entry_valid = AnalysisCacheEntry.load_by_partition(partition_id=partition_id).first()
        # check if the first entry, the one valid is returned
        assert entry_valid.id == test_data[0]['id']

    def test_get_multiple_entries_by_partition_id_if_until_valid(self):
        now = int(datetime.now(timezone.utc).timestamp())
        test_data = [
            {
                'id': 'v1|AROA_333|test123',
                'partition_id': 'AROA_333',
                'data': ['read-config'],
                'valid_until': now + 7200  # valid
            },
            {
                'id': 'v1|AROA_333|test456',
                'partition_id': 'AROA_333',
                'data': ['read-config', 'write-config'],
                'valid_until': now - 7200  # not valid
            },
            {
                'id': 'v1|AROA_333|test789',
                'partition_id': 'AROA_333',
                'data': ['read-config', 'write-config'],
                'valid_until': now + 3600  # valid
            },
            {
                'id': 'v1|AROA_444|test000',
                'partition_id': 'AROA_444',
                'data': ['read-config', 'write-config'],
                'valid_until': now + 5600  # not valid, another partition
            },
            {
                'id': 'v1|AROA_333|test101010',
                'partition_id': 'AROA_333',
                'data': ['read-config', 'write-config'],
                'valid_until': now + 5600  # valid
            },
        ]

        entries_to_save = [AnalysisCacheEntry(**test_entry) for test_entry in test_data]
        AnalysisCacheEntry.objects.bulk_create(entries_to_save)

        partition_id = 'AROA_333'
        returned_entries = AnalysisCacheEntry.load_by_partition(partition_id=partition_id)
        # 3 valid entries should be returned
        assert len(returned_entries) == 3
        
        # Verify that the correct entries ids are returned
        expected_ids = {'v1|AROA_333|test123', 'v1|AROA_333|test789', 'v1|AROA_333|test101010'}
        returned_ids = {entry.id for entry in returned_entries}

        assert returned_ids == expected_ids
