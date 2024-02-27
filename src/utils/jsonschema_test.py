import jsonschema
import json

# load payload schema definition
with open('../../create_order/pointstore_payload_schema.json', 'r') as file:
    payload_schema = json.load(file)

csb_payload_json = '''{
    "email": "john.cartwright@noaa.gov",
    "bbox": [5,60,6,61],
    "grid": {
       "resolution": 30,
        "format": 3
    },
    "datasets": [
        {
            "type": "csb",
            "providers": "PGS",
            "platforms": "Ramform Vanguard"
        }
    ]
}'''

mb_payload_json = '''{
    "email":"john.cartwright@noaa.gov",
    "bbox":"5,60,6,61",
    "grid":{
        "resolution":100,
        "background":"etopo"
    },
    "datasets":[
        {
            "label":"multibeam",
            "providers":[
                "University of New Hampshire, Center for Coastal and Ocean Mapping (UNH/CCOM)"
            ],
            "platforms":[
                "Hi'ialakai"
            ],
            "collection_date":{
                "start":"2023-02-12",
                "end":"2024-02-12"
            },
            "processing_level":"processed"
        }
    ]
}'''
payload = json.loads(mb_payload_json)

# print(payload_schema)
try:
    jsonschema.validate(instance=payload, schema=payload_schema)

except jsonschema.exceptions.ValidationError as e:
    print(e)
    print(e.message)