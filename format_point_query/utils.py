import logging
import os
from datetime import datetime
logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))


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


def filters_to_where_clause(filters):
    where_clauses = []

    if 'platforms' in filters:
        # create a list of SQL-friendly platform names from incoming SQS message
        platforms = [sql_quote_and_escape(i) for i in filters['platforms']]
        where_clauses.append(f'platform_name in ({",".join(platforms)})')

    if 'providers' in filters:
        providers = [sql_quote_and_escape(i) for i in filters['providers']]
        where_clauses.append(f'provider in ({",".join(providers)})')

    # dates are inclusive. either start, end, or both may be specified
    if 'collection_date' in filters:
        start = ''
        end = ''
        if 'start' in filters['collection_date']:
            start = filters['collection_date']['start']

        if 'end' in filters['collection_date']:
            end = filters['collection_date']['end']

        if start and end:
            where_clauses.append(f"(time >= date('{start}') and time <= date('{end}'))")
        elif start:
            where_clauses.append(f"time >= date('{start}')")
        elif end:
            where_clauses.append(f"time <= date('{end}')")

    # archive date is in UTC and represented as UNIX timestamp
    if 'archive_date' in filters:
        start = ''
        end = ''
        if 'start' in filters['archive_date']:
            start = filters['archive_date']['start']

        if 'end' in filters['archive_date']:
            end = filters['archive_date']['end']

        if start and end:
            where_clauses.append(f"(entry_date >= date('{start}') and entry_date <= date('{end}'))")
        elif start:
            where_clauses.append(f"entry_date >= date('{start}')")
        elif end:
            where_clauses.append(f"entry_date <= date('{end}')")

    if 'unique_id' in filters:
        unique_id = filters['unique_id']
        where_clauses.append(f"unique_id = '{unique_id}'")

    return where_clauses

