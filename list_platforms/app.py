import json
import boto3
import time
import logging
import os
from datetime import datetime
import re


athena = boto3.client('athena')
# APIGW times out in ~30 seconds
timeout_in_seconds = 25

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))
TABLE = os.getenv('ATHENA_TABLE', default='csb_parquet')
DATABASE = os.getenv('ATHENA_DATABASE', default='dcdb')

platform_name_pattern = re.compile("^[- .a-zA-Z0-9_/()',!]+$")
provider_name_pattern = re.compile("^[a-zA-Z0-9 ,]+$")
date_pattern = re.compile("^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}$")
unique_id_pattern = re.compile("^[a-zA-Z0-9-]+$")


def valid_bbox(coords: list[float]):
    if len(coords) != 4:
        return False
    if coords[0] < -180 or coords[0] > 180 or coords[2] < -180 or coords[2] > 180:
        return False
    if coords[1] < -90 or coords[1] > 90 or coords[3] < -90 or coords[3] > 90:
        return False
    # crosses antimeridian
    if coords[0] >= coords[2]:
        return False
    if coords[1] == coords[3]:
        return False

    return True


def create_sql_from_bbox(bbox_string: str) -> list[str]:
    try:
        coords = [float(i.strip()) for i in bbox_string.split(',')]
        if not valid_bbox(coords):
            raise IllegalArgumentException('invalid bbox coordinates: out of range or crosses antimeridian')
        minx = coords[0]
        miny = coords[1]
        maxx = coords[2]
        maxy = coords[3]
        return [
            f"(lon > {minx} and lon < {maxx})",
            f"(lat > {miny} and lat < {maxy})"
        ]
    except ValueError as e:
        raise IllegalArgumentException('invalid bbox coordinates: non-numeric values')


def iso8601_to_utc_timestamp(datestring):
    # standardize to start of day UTC
    dt = datetime.fromisoformat(datestring[0:10]+'T00:00:00Z')
    return dt.timestamp()


def utc_timestamp_to_iso8601(timestamp):
    datestring = datetime.fromtimestamp(timestamp).isoformat()
    # standardize to start of day UTC
    return datestring[0:10]+'T00:00:00Z'


# prepare strings for SQL by single quoting names and escaping single quotes w/in name
def sql_quote_and_escape(name):
    return "'" + name.replace("'", "''") + "'"


def filters_to_where_clause(filters: dict) -> list[str]:
    where_clauses = []

    if 'bbox' in filters:
        try:
            where_clauses += create_sql_from_bbox(filters['bbox'])
        except IllegalArgumentException as e:
            logger.warning(str(e))

    if 'platforms' in filters:
        # create a list of SQL-friendly platform names from URL query params
        if platform_name_pattern.match(filters['platforms']):
            platforms = [sql_quote_and_escape(i) for i in filters['platforms'].split(',')]
            where_clauses.append(f'platform_name in ({",".join(platforms)})')
        else:
            logger.warning('platforms parameter contains illegal characters')

    if 'providers' in filters:
        if provider_name_pattern.match(filters['providers']):
            providers = [sql_quote_and_escape(i) for i in filters['providers'].split(',')]
            where_clauses.append(f'provider in ({",".join(providers)})')
        else:
            logger.warning('providers parameter contains illegal characters')

    # dates are inclusive. either start, end, or both may be specified
    if 'collection_date_start' in filters or 'collection_date_end' in filters:
        start = ''
        end = ''
        # ignore values not in YYYY-MM-DD format
        if 'collection_date_start' in filters and date_pattern.match(filters['collection_date_start']):
            start = filters['collection_date_start']

        if 'collection_date_end' in filters and date_pattern.match(filters['collection_date_end']):
            end = filters['collection_date_end']

        if start and end:
            where_clauses.append(f"(time >= date('{start}') and time <= date('{end}'))")
        elif start:
            where_clauses.append(f"time >= date('{start}')")
        elif end:
            where_clauses.append(f"time <= date('{end}')")

    # archive date is in UTC and represented as UNIX timestamp
    if 'archive_date_start' in filters or 'archive_date_end' in filters:
        start = ''
        end = ''
        if 'archive_date_start' in filters and date_pattern.match(filters['archive_date_start']):
            start = filters['archive_date_start']

        if 'archive_date_end' in filters and date_pattern.match(filters['archive_date_end']):
            end = filters['archive_date_end']

        if start and end:
            where_clauses.append(f"(entry_date >= date('{start}') and entry_date <= date('{end}'))")
        elif start:
            where_clauses.append(f"entry_date >= date('{start}')")
        elif end:
            where_clauses.append(f"entry_date <= date('{end}')")

    if 'unique_id' in filters and unique_id_pattern.match(filters['unique_id']):
        unique_id = filters['unique_id']
        where_clauses.append(f"unique_id = '{unique_id}'")

    return where_clauses


def lambda_handler(event, context):
    logger.info(event)
    http_method = event['requestContext']['http']['method']
    sql = f'select distinct provider, platform_name from {DATABASE}.{TABLE}'

    if http_method == 'GET':
        if 'queryStringParameters' in event:
            where_clauses = filters_to_where_clause(event['queryStringParameters'])
            if len(where_clauses):
                sql += f" where {' and '.join(where_clauses)}"

    elif http_method == 'POST':
        # TODO
        pass
    elif http_method == 'OPTIONS':
        # TODO
        pass
    else:
        return {
            'statusCode': 405,
            'body': json.dumps({'message': 'Method Not Allowed'})
        }

    sql += ' order by 1, 2'
    logger.info(sql)
    response = athena.start_query_execution(
        QueryString=sql,
        WorkGroup='primary'
    )
    query_execution_id = response['QueryExecutionId']

    query_state = None
    check_count = 0
    while check_count < timeout_in_seconds and query_state != 'SUCCEEDED':
        time.sleep(1)
        response = athena.get_query_execution(QueryExecutionId=query_execution_id)
        query_state = response['QueryExecution']['Status']['State']
        check_count = check_count + 1

    if query_state != 'SUCCEEDED':
        execution_time = round(int(response['QueryExecution']['Statistics']['TotalExecutionTimeInMillis'])*1000)
        logger.info(f"query completed in approximately {execution_time} seconds")

        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'query took too long to respond'})
        }

    response = athena.get_query_results(QueryExecutionId=query_execution_id)
    results = []
    for i in response['ResultSet']['Rows']:
        results.append({'provider': i['Data'][0]['VarCharValue'], 'platform': i['Data'][1]['VarCharValue']})
    record_count = len(response['ResultSet']['Rows'])

    return {
        'statusCode': 200,
        'body': json.dumps({
            'count': record_count,
            'data': results[1:]
        })
    }


class IllegalArgumentException(Exception):
    pass
