import pytest
from format_point_query.utils import sql_quote_and_escape
from format_point_query.utils import filters_to_where_clause
import logging
import os
logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))


class TestCsbBuildQuery:
    @pytest.fixture()
    def test_data(self):
        return [
            {
                "name": "test case 0",
                "expected": "platform_name in ('Ramform Vanguard','Anonymous') "
                            "and provider in ('PGS','MacGregor') "
                            "and time >= date('2023-01-01') and entry_date >= date('2023-01-01')",
                "payload": {
                    'bbox': [5, 60, 6, 61],
                    'order_id': 'bc22b3a3-0ce7-4169-8754-a7cd68375985',
                    'dataset': {
                        'label': 'csb',
                        'providers': ['PGS', 'MacGregor'],
                        'platforms': ['Ramform Vanguard', 'Anonymous'],
                        'collection_date': {'start': '2023-01-01'},
                        'archive_date': {'start': '2023-01-01'}
                    }
                }
            }
        ]

    def test_sql_quote_and_escape(self):
        platforms = ["Hi'ialakai", "Surveyor"]
        expected = ["'Hi''ialakai'", "'Surveyor'"]

        assert sql_quote_and_escape(platforms[0]) == expected[0]
        assert sql_quote_and_escape(platforms[1]) == expected[1]

    def test_filters_to_where_clause(self, test_data):
        for case in test_data:
            payload = case['payload']
            expected = case['expected']
            name = case['name']
            logger.info(f'running test case {name}')
            where_clauses = filters_to_where_clause(payload['dataset'])
            assert ' and '.join(where_clauses) == expected
