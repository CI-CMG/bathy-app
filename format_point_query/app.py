"""
construct SQL statement to extract points from CSB table per user request
"""
import logging
import os
from utils import filters_to_where_clause

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "WARNING"))

DATABASE = os.getenv('ATHENA_DATABASE', 'dcdb')
TABLE = os.getenv('ATHENA_TABLE', 'csb_parquet')
S3_BUCKET = os.getenv('ATHENA_OUTPUT_BUCKET', 's3://order-pickup/')


def lambda_handler(event, context):
    where_clauses = []

    # only required parameter. Expects array of coords in minx,miny,maxx,maxy order
    bbox = {
        'minx': event['bbox'][0],
        'miny': event['bbox'][1],
        'maxx': event['bbox'][2],
        'maxy': event['bbox'][3]
    }
    where_clauses.append(f"(lon > {bbox['minx']} and lon < {bbox['maxx']})")
    where_clauses.append(f"(lat > {bbox['miny']} and lat < {bbox['maxy']})")

    where_clauses += filters_to_where_clause(event['dataset'])

    # WARNING: hardcoded dependency on Glue table schema.
    query_string = f"SELECT lon,lat,depth,time,platform_name,provider FROM {DATABASE}.{TABLE} where {' and '.join(where_clauses)}"

    return {
        'query_string': query_string,
        'label': event['dataset']['label'],
        'order_id': event['order_id']
    }


class IllegalArgumentException(Exception):
    pass

