import logging
import os
from datetime import datetime
import requests
logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))
MAPSERVICE_URL = 'https://gis.ngdc.noaa.gov/arcgis/rest/services/multibeam_files/MapServer/0/query'

# expect FBT files to be in direct descendant directory "generated" with extension ".fbt"
def translate_mb_objkey_to_fbt_objkey(objkey):
    parts = objkey.split('/')
    parts.insert(-1,'generated')
    parts[-1] = parts[-1] + '.fbt'
    # just the object key w/o prefix and bucket name
    return '/'.join(parts[3:])


# convert the value in the DATA_FILE field to an S3 url for the corresponding FBT file
def convert_data_file_to_fbt_objkey(data_file):
    # e.g. 'ocean/ships/henry_b._bigelow/HB2203/multibeam/data/version1/MB/em2040/0132_20220527_054325_HenryBigelow.all.gz'
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
    sql = payload_to_sql2(query_params)
    logger.info(sql)

    params = {
        "where": sql,
        "outFields": "CLOUD_PATH",
        # "geometry": bbox,
        "returnGeometry": "false",
        "geometryType": "esriGeometryEnvelope",
        "spatialRel": "esriSpatialRelIntersects",
        "f": "json"
    }
    if bbox is not None:
        # expects coords in minx,miny,maxx,maxy order
        bbox_str = ','.join([str(i) for i in bbox])
        params["bbox"] = bbox_str

    try:
        r = requests.get(MAPSERVICE_URL, params=params, timeout=10)
        if r.status_code != 200:
            logger.error('invalid response code: ' + str(r.status_code))
        payload = r.json()
        fbt_files = [translate_mb_objkey_to_fbt_objkey(x['attributes']['CLOUD_PATH']) for x in payload['features'] if
                 x['attributes']['CLOUD_PATH'] is not None]

        logger.info(f'{len(fbt_files)} multibeam files match request')
        return fbt_files
    except Exception as e:
        logger.error(e)
        raise e

def query_mapservice2(bbox, query_params):
    sql = payload_to_sql2(query_params)
    logger.info(sql)

    params = {
        "where": sql,
        "outFields": "DATA_FILE",
        # "geometry": bbox,
        "returnGeometry": "false",
        "geometryType": "esriGeometryEnvelope",
        "spatialRel": "esriSpatialRelIntersects",
        "f": "json"
    }
    if bbox is not None:
        # expects coords in minx,miny,maxx,maxy order
        bbox_str = ','.join([str(i) for i in bbox])
        params["bbox"] = bbox_str

    try:
        r = requests.get(MAPSERVICE_URL, params=params, timeout=10)
        if r.status_code != 200:
            logger.error('invalid response code: ' + str(r.status_code))
        payload = r.json()
        fbt_files = [convert_data_file_to_fbt_objkey(x['attributes']['DATA_FILE']) for x in payload['features'] if
                 x['attributes']['DATA_FILE'] is not None]

        logger.info(f'{len(fbt_files)} multibeam files match request')
        return fbt_files
    except Exception as e:
        logger.error(e)
        raise e

def iso8601_to_utc_timestamp(datestring):
    # standardize to start of day UTC
    dt = datetime.fromisoformat(datestring[0:10]+'T00:00:00Z')
    return dt.timestamp()


# prepare strings for SQL by single quoting names and escaping single quotes w/in name
def sql_quote_and_escape(name):
    return "'" + name.replace("'", "''") + "'"

# dates are inclusive. either start, end, or both may be specified
def format_date_clause(column_name, period):
    if 'start' in period and 'end' in period:
        return f"{column_name} between timestamp '{period['start']} 00:00:00' and timestamp '{period['end']} 23:59:59'"
    elif 'start' in period:
        return f"{column_name} >= timestamp '{period['start']} 00:00:00'"
    elif 'end' in period:
        return f"{column_name} <= timestamp '{period['end']} 23:59:59'"
    else:
        return None


def payload_to_sql(query_params):
    where_clauses = []

    if 'platforms' in query_params:
        # create a list of SQL-friendly platform names from incoming SQS message
        platforms = [sql_quote_and_escape(i) for i in query_params['platforms']]
        where_clauses.append(f'PLATFORM in ({",".join(platforms)})')

    if 'providers' in query_params:
        providers = [sql_quote_and_escape(i) for i in query_params['providers']]
        where_clauses.append(f'SOURCE in ({",".join(providers)})')

    # dates are inclusive. either start, end, or both may be specified
    if 'collection_date' in query_params:
        start = ''
        end = ''
        if 'start' in query_params['collection_date']:
            # mapservice uses dates as string formatted YYYY/MM/DD rather than YYYY-MM-DD
            start = query_params['collection_date']['start'].replace('-', '/')

        if 'end' in query_params['collection_date']:
            end = query_params['collection_date']['end'].replace('-', '/')

        if start and end:
            where_clauses.append(f"(START_DATE >= '{start}' and END_DATE <= '{end}')")
        elif start:
            where_clauses.append(f"START_DATE >= '{start}'")
        elif end:
            where_clauses.append(f"END_DATE <= '{end}'")

    # archive date is in UTC and represented as UNIX timestamp
    if 'archive_date' in query_params:
        start = ''
        end = ''
        if 'start' in query_params['archive_date']:
            start = iso8601_to_utc_timestamp(query_params['archive_date']['start'])

        if 'end' in query_params['archive_date']:
            end = iso8601_to_utc_timestamp(query_params['archive_date']['end'])

        if start and end:
            where_clauses.append(f"(PUBLISH_DATE >= '{start}' and PUBLISH_DATE <= '{end}')")
        elif start:
            where_clauses.append(f"PUBLISH_DATE >= '{start}'")
        elif end:
            where_clauses.append(f"PUBLISH_DATE <= '{end}'")

    if 'exclude_surveys' in query_params:
        exclude_surveys = [sql_quote_and_escape(i) for i in query_params['exclude_surveys']]
        where_clauses.append(f'SURVEY_NAME not in ({",".join(exclude_surveys)})')

    if 'surveys' in query_params:
        surveys = [sql_quote_and_escape(i) for i in query_params['surveys']]
        # "surveys" parameter supersedes all other MB parameters except "processing_level"
        where_clauses = [f'SURVEY_NAME in ({",".join(surveys)})']

    if 'processing_level' in query_params:
        processing_level = 'MB RAW' if query_params["processing_level"] == 'raw' else 'MB PROCESSED'
        where_clauses.append(f"""DATASET_TYPE_NAME = '{processing_level}'""")

    return ' and '.join(where_clauses)


# modified to accommodate CRUISE schema and multibeam_files mapservice.
def payload_to_sql2(query_params):
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
        where_clauses.append(format_date_clause('COLLECTION_DATE', query_params['collection_date']))

    # archive date is in UTC and represented as UNIX timestamp
    if 'archive_date' in query_params:
        where_clauses.append(format_date_clause('PUBLISH_DATE', query_params['archive_date']))

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
