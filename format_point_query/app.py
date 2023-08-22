"""
construct SQL statement to extract points from CSB table per user request
"""
import json
import logging
import os
import copy

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "WARNING"))

DATABASE = os.getenv('ATHENA_DATABASE')
TABLE = os.getenv('ATHENA_TABLE')
S3_BUCKET = os.getenv('ATHENA_OUTPUT_BUCKET')


# select * from csb_h3_parquet where lon > -98.150 and lat > 27.451 and
# lon < -96.018 and lat < 28.807 and platform = 'BAILEY' and provider = 'Rose Point'
# and entry_date > date('2021-06-01') and time > date('2021-06-10')

def lambda_handler(event, context):
    # print(event)

    # verify all expected env variables found
    if not (DATABASE and TABLE and S3_BUCKET):
        logger.error("missing required environment variable")
        return

    where_clauses = []
    try:
        # only required parameter
        bbox = {
            'minx': event['bbox'][0],
            'miny': event['bbox'][1],
            'maxx': event['bbox'][2],
            'maxy': event['bbox'][3]
        }

        where_clauses.append(
            f"lon > {bbox['minx']} and lon < {bbox['maxx']} and "
            f"lat > {bbox['miny']} and lat < {bbox['maxy']}"
        )

        # f-strings not used due to problems with quote escaping
        if 'provider' in event['dataset']:
            # where_clauses.append("provider = '" + event['dataset']['provider'] + "'")
            where_clauses.append(f"provider = '{event['dataset']['provider']}'")

        if 'platform' in event['dataset']:
            where_clauses.append("platform_name = '" + event['dataset']['platform'] + "'")

        if 'date' in event['dataset']:
            where_clauses.append("time >= date('" + event['dataset']['date'] + "')")

        # entry_date only available in re-processed dataset, e.g. bathymetry.csb_h3_parquet
        if 'entry_date' in event['dataset']:
            where_clauses.append("entry_date >= date('" + event['dataset']['entry_date'] + "')")

        # WARNING: hardcoded dependency on Glue table structure. TODO read field list from env var?
        query_string = f"SELECT lon,lat,depth,time,platform_name,provider FROM {DATABASE}.{TABLE} where {' and '.join(where_clauses)}"

        result = copy.deepcopy(event)
        result['QUERY_STRING'] = query_string

        return result

    except Exception as e:
        logger.error(e)


class IllegalArgumentException(Exception):
    pass

