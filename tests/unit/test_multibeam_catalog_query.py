import pytest
from multibeam_catalog_query.utils import sql_quote_and_escape
from multibeam_catalog_query.utils import payload_to_sql
import logging
import os
logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))


class TestMultibeamCatalogQuery:
    @pytest.fixture()
    def test_data(self):
        return [
            {
                "name": "test case 0",
                "expected": "PLATFORM in ('Hi''ialakai','Surveyor') and SOURCE in ('University of New Hampshire, Center for Coastal and Ocean Mapping (UNH/CCOM)') and (START_DATE >= '2013/10/26' and END_DATE <= '2013/10/30') and DATASET_TYPE_NAME = 'MB PROCESSED'",
                "payload": {
                    "label": "multibeam",
                    "providers": [
                        "University of New Hampshire, Center for Coastal and Ocean Mapping (UNH/CCOM)"
                    ],
                    "platforms": [
                        "Hi\'ialakai",
                        "Surveyor"
                    ],
                    "collection_date": {
                        "start": "2013-10-26",
                        "end": "2013-10-30"
                    },
                    "processing_level":
                        "processed"
                }
            },
            {
                "name": "test case 1",
                "expected": "SURVEY_NAME in ('KM1319') and DATASET_TYPE_NAME = 'MB PROCESSED'",
                "payload": {
                    "label": "multibeam",
                    "providers": [
                        "University of New Hampshire, Center for Coastal and Ocean Mapping (UNH/CCOM)"
                    ],
                    "surveys": ["KM1319"],
                    "processing_level":
                        "processed"
                }
            }

        ]

    def test_sql_quote_and_escape(self):
        platforms = ["Hi'ialakai", "Surveyor"]
        expected = ["'Hi''ialakai'", "'Surveyor'"]

        assert sql_quote_and_escape(platforms[0]) == expected[0]
        assert sql_quote_and_escape(platforms[1]) == expected[1]

    def test_payload_to_sql(self, test_data):
        for case in test_data:
            payload = case['payload']
            expected = case['expected']
            name = case['name']
            logger.info(f'running test case {name}')
            assert payload_to_sql(payload) == expected
