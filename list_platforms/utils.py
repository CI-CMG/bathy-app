import os
import logging


log_level = os.getenv('LOGLEVEL', default='WARNING').upper()
try:
    log_level = getattr(logging, log_level)
except:
    log_level = getattr(logging, 'WARNING')
logger = logging.getLogger(__name__)
logger.setLevel(log_level)


def get_bbox(bbox_string):
    coords_list = [float(c.strip()) for c in bbox_string.split(',')]
    if (
            -180 <= coords_list[0] <= 180 and -180 <= coords_list[2] <= 180 and
            coords_list[0] < coords_list[2] and
            -90 <= coords_list[1] <= 90 and -90 <= coords_list[3] <= 90 and
            coords_list[1] < coords_list[3]
    ):
        return {'minx': coords_list[0], 'miny': coords_list[1], 'maxx': coords_list[2], 'maxy': coords_list[3]}
        # TODO standardize coordinate precision?
        # return ','.join([str(c) for c in coords_list])
    else:
        raise Exception("invalid coordinates provided")


def valid_resolution(res):
    if not (type(res) == int or type(res) == float):
        logger.debug(f"{res} is an invalid value for grid_resolution, will ignore")
        return False

    if res <= 0:
        return False
    # TODO add other restrictions, e.g. max_resolution?
    return True


# valid "-G gridkind" format identifiers as specified in mbgrid documentation
# see http://www3.mbari.org/products/mbsystem/html/mbgrid.html
def valid_grid_format(format_id):
    return format_id in [1, 2, 3, 4, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]


def validate_payload(payload):
    # require email
    if 'email' in payload:
        try:
            validate_email(payload['email'])
        except EmailNotValidError as e:
            logger.debug(f"{payload['email']} is invalid email address.\n{str(e)}")
            raise IllegalArgumentException("valid email address required ")
    else:
        raise IllegalArgumentException("valid email address required ")

    # require BBOX parameter
    if 'bbox' in payload:
        bbox = get_bbox(payload['bbox'])
    else:
        raise IllegalArgumentException("bbox required")

    # default to create_grid = False
    if 'create_grid' not in payload or payload['create_grid'] is not True:
        payload['create_grid'] = False

    # always have these attributes
    bbox_string = ','.join([str(c) for c in [bbox['minx'], bbox['miny'], bbox['maxx'], bbox['maxy']]])
    attributes = {
        'bbox': bbox_string,
        'email': payload['email'],
        'create_grid': payload['create_grid']
    }

    if attributes['create_grid']:
        if 'grid_resolution' in payload and valid_resolution(payload['grid_resolution']):
            # attributes['grid_resolution'] = payload['grid_resolution']
            pass
        else:
            # TODO allow default cell size?
            logger.warning("missing or invalid grid_resolution - skipping grid generation")
            attributes['create_grid'] = False

    if attributes['create_grid']:
        if 'grid_format' in payload and valid_grid_format(payload['grid_format']):
            # attributes['grid_format'] = payload['grid_format']
            pass
        else:
            logger.warning("missing or invalid grid_format - skipping grid generation")
            attributes['create_grid'] = False

    if attributes['create_grid']:
        attributes['grid_resolution'] = payload['grid_resolution']
        attributes['grid_format'] = payload['grid_format']

    return {"attributes": attributes, "bbox": bbox}


def format_query(bbox, table):
    # numeric attribute comparison slightly faster than spatial operator
    query = f"""SELECT * FROM {table} where \
    lon > {bbox['minx']} and lon < {bbox['maxx']} and \
    lat > {bbox['miny']} and lat < {bbox['maxy']}"""

    return query


class IllegalArgumentException(Exception):
    pass


class StateMachineException(Exception):
    pass
