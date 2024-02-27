"""
    regex_tester.py

    utility script which checks the contents of the hardcoded map service fields SURVEY_NAME, SOURCE, and PLATFORM
    against the expected naming conventions
"""
import re
import requests

base_url = 'https://gis.ngdc.noaa.gov/arcgis/rest/services/test/MB_files_test/MapServer/0/query'
sources_regex = re.compile(r"^[\w| /(),.-]+$")

def check_survey_names():
    regex = re.compile(r"^[\w-]+$")

    params = {
        "where": "1=1",
        "outFields":  "SURVEY_NAME",
        "returnGeometry": "false",
        "returnDistinctValues": "true",
        "f": "json"
    }
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        raise Exception("server query failed for survey names")
    payload = response.json()
    names = [x['attributes']['SURVEY_NAME'] for x in payload['features'] if x['attributes']['SURVEY_NAME'] is not None ]
    # alternative to using conditional in the list comprehension above
    # names = filter(lambda x: x is not None, names)

    # regex.search() returns None for an invalid name, i.e. contains characters outside the specified set
    if not all(regex.search(i) for i in names):
        print('regex fails to match all survey names')
    else:
        print('regex matches all survey names')

    # uncomment for debugging
    # for i in names:
    #     if regex.search(i) is None:
    #         print(f'invalid name: {i}')


def check_sources():
    regex = re.compile(r"^[\w| /(),.-]+$")

    params = {
        "where": "1=1",
        "outFields":  "SOURCE",
        "returnGeometry": "false",
        "returnDistinctValues": "true",
        "f": "json"
    }
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        raise Exception("server query failed for sources")
    payload = response.json()
    names = [x['attributes']['SOURCE'] for x in payload['features'] if x['attributes']['SOURCE'] is not None ]

    if not all(regex.search(i) for i in names):
        print('regex fails to match all sources')
    else:
        print('regex matches all sources')


def check_platforms():
    regex = re.compile(r"^[\w /()'.-]+$")

    params = {
        "where": "1=1",
        "outFields":  "PLATFORM",
        "returnGeometry": "false",
        "returnDistinctValues": "true",
        "f": "json"
    }
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        raise Exception("server query failed for platforms")
    payload = response.json()
    names = [x['attributes']['PLATFORM'] for x in payload['features'] if x['attributes']['PLATFORM'] is not None ]

    if not all(regex.search(i) for i in names):
        print('regex fails to match all platforms')
    else:
        print('regex matches all platforms')


check_survey_names()
check_sources()
check_platforms()
