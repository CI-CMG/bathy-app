import json
import logging
import os
import copy

# setup logging
log_level = os.getenv('LOGLEVEL', default='WARNING').upper()
try:
    log_level = getattr(logging, log_level)
except:
    # use default in case of invalid log level
    log_level = getattr(logging, 'WARNING')
logger = logging.getLogger(__name__)
logger.setLevel(log_level)


# parse and validate bbox coordinates
def get_bbox(bbox_string):
    coords_list = [float(c.strip()) for c in bbox_string.split(',')]
    if (
            -180 <= coords_list[0] <= 180 and -180 <= coords_list[2] <= 180 and
            coords_list[0] < coords_list[2] and
            -90 <= coords_list[1] <= 90 and -90 <= coords_list[3] <= 90 and
            coords_list[1] < coords_list[3]
    ):
        # TODO standardize coordinate precision?
        return {'minx': coords_list[0], 'miny': coords_list[1], 'maxx': coords_list[2], 'maxy': coords_list[3]}
    else:
        raise Exception("invalid coordinates provided")


# select * from csb_h3_parquet where lon > -98.150 and lat > 27.451 and
# lon < -96.018 and lat < 28.807 and platform = 'BAILEY' and provider = 'Rose Point'
# and entry_date > date('2021-06-01') and time > date('2021-06-10')

def lambda_handler(event, context):
    """
    construct SQL statement to extract points from CSB table per user request
    """
    # print(event)

    DATABASE = os.getenv('ATHENA_DATABASE', default='bathymetry')
    TABLE = os.getenv('ATHENA_TABLE', default='csb_parquet')
    S3_BUCKET = os.getenv('ATHENA_OUTPUT_BUCKET', default='s3://csb-data-pickup/')

    # verify all expected env variables found
    if not (DATABASE and TABLE and S3_BUCKET):
        logger.error("missing required environment variable")
        return

    where_clauses = []
    try:
        # only required parameter
        bbox = get_bbox(event['bbox'])

        where_clauses.append((
            f"lon > {bbox['minx']} and lon < {bbox['maxx']} and "
            f"lat > {bbox['miny']} and lat < {bbox['maxy']}"
        ))

        # f-strings not used due to problems with quote escaping
        if 'provider' in event['dataset']:
            where_clauses.append("provider = '" + event['dataset']['provider'] + "'")

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

