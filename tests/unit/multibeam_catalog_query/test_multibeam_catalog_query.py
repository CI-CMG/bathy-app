import pytest
from multibeam_catalog_query.utils import sql_quote_and_escape
from multibeam_catalog_query.utils import iso8601_to_utc_timestamp
from multibeam_catalog_query.utils import format_collection_date_clause
from multibeam_catalog_query.utils import format_archive_date_clause
from multibeam_catalog_query.utils import payload_to_sql
from multibeam_catalog_query.utils import query_mapservice
from multibeam_catalog_query.utils import convert_data_file_to_fbt_objkey
import logging
import os
logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))
import boto3
import botocore.exceptions

s3_client = boto3.client('s3')


class TestMultibeamCatalogQuery:
    @pytest.fixture()
    def test_data(self):
        return [
            {
                "name": "platform, source, date_range, data_type",
                "expected": "PLATFORM_NAME in ('Hi''ialakai','Surveyor') and SOURCE in ('University of New Hampshire, Center for Coastal and Ocean Mapping (UNH/CCOM)') and (SURVEY_START_TIME >= 1382745600 and SURVEY_END_TIME <= 1383177599) and DATA_TYPE = 'MB PROCESSED'",
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
                "name": "survey and data_type",
                "expected": "SURVEY_NAME in ('KM1319') and DATA_TYPE = 'MB PROCESSED'",
                "payload": {
                    "label": "multibeam",
                    "providers": [
                        "University of New Hampshire, Center for Coastal and Ocean Mapping (UNH/CCOM)"
                    ],
                    "surveys": ["KM1319"],
                    "processing_level":
                        "processed"
                }
            },
            {
                "name": "surveys parameter overrides all others except processing_level",
                "expected": "SURVEY_NAME in ('HB2203') and DATA_TYPE = 'MB RAW'",
                "payload": {
                    "label": "multibeam",
                    "providers": [ "National Marine Fisheries Service (NMFS)" ],
                    "surveys": ["HB2203"],
                    "processing_level": "raw",
                    "platforms": [
                        "NOAA Ship HENRY B. BIGELOW (R225)"
                    ]
                }
            },
            {
                "name": "single survey",
                "expected": "SURVEY_NAME in ('HNRO17RR') and DATA_TYPE = 'MB RAW'",
                "payload": {
                    "label": "multibeam",
                    "processing_level": "raw",
                    "surveys": ["HNRO17RR"]
                }
            }

        ]

    def test_sql_quote_and_escape(self):
        platforms = ["Hi'ialakai", "Surveyor"]
        expected = ["'Hi''ialakai'", "'Surveyor'"]

        assert sql_quote_and_escape(platforms[0]) == expected[0]
        assert sql_quote_and_escape(platforms[1]) == expected[1]

    def test_iso8601_to_timestamp(self):
        assert 1776988800 == iso8601_to_utc_timestamp('2026-04-24')
        assert 1777075199 == iso8601_to_utc_timestamp('2026-04-24', end_of_day=True)


    def test_format_collection_date_clause(self):
        input_periods = [
            {"start":"2022-04-06"},
            {"start":"2022-04-06", "end":"2022-04-06"},
            {"start":"2022-04-06", "end": "2022-04-07"},
            {"end":"2022-04-06"}
        ]
        expected = [
            "SURVEY_START_TIME >= 1649203200",
            "(SURVEY_START_TIME >= 1649203200 and SURVEY_END_TIME <= 1649289599)",
            "(SURVEY_START_TIME >= 1649203200 and SURVEY_END_TIME <= 1649375999)",
            "SURVEY_END_TIME <= 1649289599"
        ]

        for case in zip(input_periods, expected):
            assert format_collection_date_clause(case[0]) == case[1]

    def test_payload_to_sql(self, test_data):
        for case in test_data:
            payload = case['payload']
            expected = case['expected']
            name = case['name']
            logger.info(f'running test case {name}')
            logger.info(payload_to_sql(payload))
            assert payload_to_sql(payload) == expected

    # def test_payload_to_sql2(self, test_data):
    #     for case in test_data[3:]:
    #         payload = case['payload']
    #         expected = case['expected']
    #         name = case['name']
    #         # logger.info(f'running test case {name}')
    #         # logger.info(payload_to_sql2(payload))
    #         # logger.info(f'{expected}')
    #         assert payload_to_sql2(payload) == expected

    def test_multibeam_catalog_query(self, test_data):
        fbt_obj_keys = query_mapservice(None, test_data[2]['payload'])
        print('FBT files: ', fbt_obj_keys)
        assert len(fbt_obj_keys)
        bucket_name = 'noaa-dcdb-bathymetry-pds'

        for object_key in fbt_obj_keys:
            try:
                # logger.info(f"checking for object key: '{object_key}'")
                response = s3_client.head_object(Bucket=bucket_name, Key=object_key)
                assert response['ResponseMetadata']['HTTPStatusCode'] == 200
                assert response['ContentLength'] > 0
            except botocore.exceptions.ClientError as e:
                if e.response['Error']['Code'] == "404":
                    logger.warning(f"Object '{object_key}' not found in bucket '{bucket_name}'.")
                    # raise e
                else:
                    # Re-raise the exception for other errors (e.g., 403 Forbidden, 500 Internal Error)
                    raise e

    def test_multibeam_catalog_query2(self, test_data):
        fbt_obj_keys = query_mapservice(None, test_data[3]['payload'])
        assert len(fbt_obj_keys)
        bucket_name = 'noaa-dcdb-bathymetry-pds'

        for object_key in fbt_obj_keys:
            try:
                # logger.info(f"checking for object key: '{object_key}'")
                response = s3_client.head_object(Bucket=bucket_name, Key=object_key)
                assert response['ResponseMetadata']['HTTPStatusCode'] == 200
                assert response['ContentLength'] > 0
            except botocore.exceptions.ClientError as e:
                if e.response['Error']['Code'] == "404":
                    logger.warning(f"Object '{object_key}' not found in bucket '{bucket_name}'.")
                    # raise e
                else:
                    # Re-raise the exception for other errors (e.g., 403 Forbidden, 500 Internal Error)
                    raise e

    def test_data_file_to_fbt(self, test_data):
        file_name = 'ocean/ships/henry_b._bigelow/HB2203/multibeam/data/version1/MB/em2040/0132_20220527_054325_HenryBigelow.all.gz'
        expected = 'mb/ships/henry_b._bigelow/HB2203/multibeam/data/version1/MB/em2040/generated/0132_20220527_054325_HenryBigelow.all.fbt'

        assert convert_data_file_to_fbt_objkey(file_name) == expected