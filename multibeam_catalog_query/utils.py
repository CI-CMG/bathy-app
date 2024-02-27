import logging
import os
from datetime import datetime
logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))


def iso8601_to_utc_timestamp(datestring):
    # standardize to start of day UTC
    dt = datetime.fromisoformat(datestring[0:10]+'T00:00:00Z')
    return dt.timestamp()


# prepare strings for SQL by single quoting names and escaping single quotes w/in name
def sql_quote_and_escape(name):
    return "'" + name.replace("'", "''") + "'"


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

