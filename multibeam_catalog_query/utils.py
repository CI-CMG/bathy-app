import logging
import os
from datetime import datetime
import requests
logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))
MAPSERVICE_URL = 'https://gis.ngdc.noaa.gov/arcgis/rest/services/multibeam_files/MapServer/0/query'

# convert the value in the CLOUD_PATH field to an S3 object key for the corresponding FBT file
def translate_cloud_path_to_fbt_objkey(cloud_path):
    parts = cloud_path.split('/')
    parts.insert(-1,'generated')
    parts[-1] = parts[-1] + '.fbt'
    # just the object key w/o prefix and bucket name
    return '/'.join(parts[3:])


# convert the value in the DATA_FILE field to an S3 object key for the corresponding FBT file
def convert_data_file_to_fbt_objkey(data_file):
    # e.g. 'ocean/ships/henry_b._bigelow/HB2203/multibeam/data/version1/MB/em2040/0132_20220527_054325_HenryBigelow.all.gz'
    # to  'mb/ships/henry_b._bigelow/HB2203/multibeam/data/version1/MB/em2040/generated/0132_20220527_054325_HenryBigelow.all.fbt'
    parts = data_file.split('/')
    # substitute 'mb' for 'ocean' in leading part of prefix
    parts[0] = 'mb'

    # FBT files use different prefix
    parts.insert(-1, 'generated')

    # replace extension with 'fbt'
    name_parts = parts[-1].split('.')
    name_parts[-1] = 'fbt'
    parts[-1] = '.'.join(name_parts)
    return '/'.join(parts)
    # return f"s3://noaa-dcdb-bathymetry-pds/{'/'.join(parts)}"

def query_mapservice(bbox, query_params):
    sql = payload_to_sql(query_params)
    logger.info(sql)

    params = {
        "where": sql,
        "outFields": "DATA_FILE",
        "returnGeometry": "false",
        "geometryType": "esriGeometryEnvelope",
        "spatialRel": "esriSpatialRelIntersects",
        "f": "json"
    }
    if bbox is not None:
        # expects coords in minx,miny,maxx,maxy order
        bbox_str = ','.join([str(i) for i in bbox])
        params["geometry"] = bbox_str

    try:
        # TODO mapservice limits 2000 records per page, need to iterate over all available pages
        r = requests.get(MAPSERVICE_URL, params=params, timeout=10)
        if r.status_code != 200:
            logger.error('invalid response code: ' + str(r.status_code))
        payload = r.json()
        fbt_files = [convert_data_file_to_fbt_objkey(x['attributes']['DATA_FILE']) for x in payload['features'] if
                 x['attributes']['DATA_FILE'] is not None]

        # logger.info(f'{len(fbt_files)} multibeam files match request')
        return fbt_files
    except Exception as e:
        logger.error(e)
        raise e

def iso8601_to_utc_timestamp(datestring, end_of_day=False):
    if not end_of_day:
        # ignore anything in datestring beyond YYYY-MM-DD
        dt = datetime.fromisoformat(datestring[0:10]+'T00:00:00Z')
    else:
        dt = datetime.fromisoformat(datestring[0:10]+'T23:59:59Z')
    return int(dt.timestamp())


# prepare strings for SQL by single quoting names and escaping single quotes w/in name
def sql_quote_and_escape(name):
    return "'" + name.replace("'", "''") + "'"


# dates are inclusive. either start, end, or both may be specified
def format_collection_date_clause(period):
    start = None
    end = None

    # use the ISO8601 date and construct timestamp in the query or pre-calculate?
    if 'start' in period:
        start = iso8601_to_utc_timestamp(period['start'])
    if 'end' in period:
        end = iso8601_to_utc_timestamp(period['end'], end_of_day=True)
    if start and end:
        # return f"(SURVEY_START_TIME >= timestamp '{start}' and SURVEY_END_TIME <= timestamp '{end}')"
        return f"(SURVEY_START_TIME >= {start} and SURVEY_END_TIME <= {end})"
    elif start:
        return f"SURVEY_START_TIME >= {start}"
    elif end:
        return f"SURVEY_END_TIME <= {end}"
    else:
        return None


def format_archive_date_clause(period):
    # logger.info(period)
    start = None
    end = None

    # use the ISO8601 date and construct timestamp in the query or pre-calculate?
    if 'start' in period:
        start = iso8601_to_utc_timestamp(period['start'])
    if 'end' in period:
        end = iso8601_to_utc_timestamp(period['end'], end_of_day=True)

    if 'start' in period and 'end' in period:
        return f"PUBLISH_DATE between {start} and {end}"
    elif 'start' in period:
        return f"PUBLISH_DATE >= {start}"
    elif 'end' in period:
        return f"PUBLISH_DATE <= {end}"
    else:
        return None

# JSON schema parameter == feature service field
# platforms == PLATFORM_NAME
# providers == SOURCE
# collection_date == SURVEY_START_TIME, SURVEY_END_TIME
# archive_date == PUBLISH_DATE
# surveys, exclude_surveys == SURVEY_NAME
# processing_level == DATA_TYPE

def payload_to_sql(query_params):
    where_clauses = []

    if 'platforms' in query_params:
        # create a list of SQL-friendly platform names from incoming SQS message
        platforms = [sql_quote_and_escape(i) for i in query_params['platforms']]
        where_clauses.append(f'PLATFORM_NAME in ({",".join(platforms)})')

    if 'providers' in query_params:
        providers = [sql_quote_and_escape(i) for i in query_params['providers']]
        where_clauses.append(f'SOURCE in ({",".join(providers)})')

    # dates are inclusive. either start, end, or both may be specified
    if 'collection_date' in query_params:
        where_clauses.append(format_collection_date_clause(query_params['collection_date']))

    # archive date is in UTC and represented as UNIX timestamp
    if 'archive_date' in query_params:
        where_clauses.append(format_archive_date_clause(query_params['archive_date']))

    if 'exclude_surveys' in query_params:
        exclude_surveys = [sql_quote_and_escape(i) for i in query_params['exclude_surveys']]
        where_clauses.append(f'SURVEY_NAME not in ({",".join(exclude_surveys)})')

    if 'surveys' in query_params:
        surveys = [sql_quote_and_escape(i) for i in query_params['surveys']]
        # "surveys" parameter supersedes all other MB parameters except "processing_level"
        where_clauses = [f'SURVEY_NAME in ({",".join(surveys)})']

    if 'processing_level' in query_params:
        processing_level = 'MB RAW' if query_params["processing_level"] == 'raw' else 'MB PROCESSED'
        where_clauses.append(f"""DATA_TYPE = '{processing_level}'""")

    return ' and '.join(where_clauses)
