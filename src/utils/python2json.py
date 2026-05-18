import json

# msg = {'version': '2.0', 'routeKey': 'GET /platforms', 'rawPath': '/platforms', 'rawQueryString': 'providers=AquaMap', 'headers': {'content-length': '0', 'host': 'q81rej0j12.execute-api.us-east-1.amazonaws.com', 'user-agent': 'RapidAPI/4.2.8 (Macintosh; OS X/14.7.4) GCDHTTPRequest', 'x-amzn-trace-id': 'Root=1-67d5cc00-3af6433861128c585ccd41b7', 'x-forwarded-for': '76.25.16.208', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https'}, 'queryStringParameters': {'providers': 'AquaMap'}, 'requestContext': {'accountId': '282856304593', 'apiId': 'q81rej0j12', 'domainName': 'q81rej0j12.execute-api.us-east-1.amazonaws.com', 'domainPrefix': 'q81rej0j12', 'http': {'method': 'GET', 'path': '/platforms', 'protocol': 'HTTP/1.1', 'sourceIp': '76.25.16.208', 'userAgent': 'RapidAPI/4.2.8 (Macintosh; OS X/14.7.4) GCDHTTPRequest'}, 'requestId': 'HezQMj_wIAMEPhw=', 'routeKey': 'GET /platforms', 'stage': '$default', 'time': '15/Mar/2025:18:50:40 +0000', 'timeEpoch': 1742064640809}, 'isBase64Encoded': False}
# msg = {'UpdateCount': 0, 'ResultSet': {'Rows': [{'Data': [{'VarCharValue': '_col0'}]}, {'Data': [{'VarCharValue': '1397991288'}]}], 'ResultSetMetadata': {'ColumnInfo': [{'CatalogName': 'hive', 'SchemaName': '', 'TableName': '', 'Name': '_col0', 'Label': '_col0', 'Type': 'bigint', 'Precision': 19, 'Scale': 0, 'Nullable': 'UNKNOWN', 'CaseSensitive': False}]}}, 'ResponseMetadata': {'RequestId': 'ca33e4ed-18ca-41b0-a527-90ba6d74b28e', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Fri, 21 Mar 2025 22:21:15 GMT', 'content-type': 'application/x-amz-json-1.1', 'content-length': '566', 'connection': 'keep-alive', 'x-amzn-requestid': 'ca33e4ed-18ca-41b0-a527-90ba6d74b28e'}, 'RetryAttempts': 0}}
msg = [
  {
    "Provider": "Alcatel Submarine Networks",
    "RecordCount": "243099",
    "PlatformCount": "1",
    "MinDateTime": "2024-07-23 16:32:00.170",
    "MaxDateTime": "2024-10-10 14:26:26.320",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "Ile de Molene",
        "Count": "243099",
        "FirstSubmission": "2024-11-20",
        "LastSubmission": "2025-01-29"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2024-10-01 00:00:00.000",
        "Count": "43327"
      },
      {
        "Month": "2024-07-01 00:00:00.000",
        "Count": "199772"
      }
    ],
    "ActiveProvider": "false"
  },
  {
    "Provider": "Anonymous",
    "RecordCount": "146633",
    "PlatformCount": "1",
    "MinDateTime": "2020-01-30 01:23:51.000",
    "MaxDateTime": "2021-12-17 20:25:22.000",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "Anonymous",
        "Count": "146633",
        "FirstSubmission": "2023-03-22",
        "LastSubmission": "2023-03-23"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2021-12-01 00:00:00.000",
        "Count": "2638"
      },
      {
        "Month": "2021-11-01 00:00:00.000",
        "Count": "1629"
      },
      {
        "Month": "2021-10-01 00:00:00.000",
        "Count": "8517"
      },
      {
        "Month": "2021-09-01 00:00:00.000",
        "Count": "9179"
      },
      {
        "Month": "2021-03-01 00:00:00.000",
        "Count": "12579"
      },
      {
        "Month": "2021-02-01 00:00:00.000",
        "Count": "9677"
      },
      {
        "Month": "2021-01-01 00:00:00.000",
        "Count": "16170"
      },
      {
        "Month": "2020-09-01 00:00:00.000",
        "Count": "7550"
      },
      {
        "Month": "2020-08-01 00:00:00.000",
        "Count": "12016"
      },
      {
        "Month": "2020-07-01 00:00:00.000",
        "Count": "14259"
      },
      {
        "Month": "2020-06-01 00:00:00.000",
        "Count": "17181"
      },
      {
        "Month": "2020-05-01 00:00:00.000",
        "Count": "17716"
      },
      {
        "Month": "2020-04-01 00:00:00.000",
        "Count": "9281"
      },
      {
        "Month": "2020-03-01 00:00:00.000",
        "Count": "4605"
      },
      {
        "Month": "2020-02-01 00:00:00.000",
        "Count": "3196"
      },
      {
        "Month": "2020-01-01 00:00:00.000",
        "Count": "440"
      }
    ],
    "ActiveProvider": "false"
  },
  {
    "Provider": "AquaMap",
    "RecordCount": "92754373",
    "PlatformCount": "121",
    "MinDateTime": "2023-02-09 23:42:02.000",
    "MaxDateTime": "2025-05-29 22:28:49.000",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "Anonymous",
        "Count": "43006740",
        "FirstSubmission": "2023-03-07",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Largo",
        "Count": "5262701",
        "FirstSubmission": "2023-03-26",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Earendil",
        "Count": "3838928",
        "FirstSubmission": "2023-03-08",
        "LastSubmission": "2025-04-11"
      },
      {
        "Platform": "Sea Wings",
        "Count": "3404364",
        "FirstSubmission": "2023-05-19",
        "LastSubmission": "2025-04-01"
      },
      {
        "Platform": "Problem Child",
        "Count": "2084268",
        "FirstSubmission": "2024-04-18",
        "LastSubmission": "2025-05-01"
      },
      {
        "Platform": "Bertha",
        "Count": "2054592",
        "FirstSubmission": "2023-12-14",
        "LastSubmission": "2025-03-28"
      },
      {
        "Platform": "Deep Playa",
        "Count": "2049793",
        "FirstSubmission": "2024-10-21",
        "LastSubmission": "2025-04-08"
      },
      {
        "Platform": "Hemispheres",
        "Count": "1629385",
        "FirstSubmission": "2024-12-11",
        "LastSubmission": "2025-05-01"
      },
      {
        "Platform": "SV Breathe",
        "Count": "1424594",
        "FirstSubmission": "2023-05-06",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Miss Eva",
        "Count": "1295385",
        "FirstSubmission": "2023-04-08",
        "LastSubmission": "2023-10-22"
      },
      {
        "Platform": "Accountan-sea",
        "Count": "1242479",
        "FirstSubmission": "2024-05-31",
        "LastSubmission": "2025-05-07"
      },
      {
        "Platform": "SparrowHawk",
        "Count": "1199484",
        "FirstSubmission": "2023-10-24",
        "LastSubmission": "2025-05-27"
      },
      {
        "Platform": "Chapter Four",
        "Count": "1075657",
        "FirstSubmission": "2023-03-02",
        "LastSubmission": "2024-09-16"
      },
      {
        "Platform": "Aventura",
        "Count": "1048756",
        "FirstSubmission": "2023-07-03",
        "LastSubmission": "2025-04-16"
      },
      {
        "Platform": "Bonita",
        "Count": "1019087",
        "FirstSubmission": "2023-08-14",
        "LastSubmission": "2025-04-27"
      },
      {
        "Platform": "Svall2well",
        "Count": "1016175",
        "FirstSubmission": "2024-05-27",
        "LastSubmission": "2025-05-27"
      },
      {
        "Platform": "Karuna",
        "Count": "848632",
        "FirstSubmission": "2023-02-27",
        "LastSubmission": "2025-04-01"
      },
      {
        "Platform": "Herkee",
        "Count": "831706",
        "FirstSubmission": "2023-10-17",
        "LastSubmission": "2025-04-20"
      },
      {
        "Platform": "Katinsky",
        "Count": "789256",
        "FirstSubmission": "2025-02-13",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Endurance",
        "Count": "758938",
        "FirstSubmission": "2023-08-20",
        "LastSubmission": "2025-05-09"
      },
      {
        "Platform": "Fancy Free",
        "Count": "745166",
        "FirstSubmission": "2024-08-12",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Southwind",
        "Count": "740856",
        "FirstSubmission": "2024-05-30",
        "LastSubmission": "2025-04-27"
      },
      {
        "Platform": "River Girl",
        "Count": "740674",
        "FirstSubmission": "2023-03-19",
        "LastSubmission": "2024-08-03"
      },
      {
        "Platform": "CLASSEA",
        "Count": "740030",
        "FirstSubmission": "2023-09-07",
        "LastSubmission": "2025-04-29"
      },
      {
        "Platform": "Sunset Delight",
        "Count": "723825",
        "FirstSubmission": "2024-11-01",
        "LastSubmission": "2025-05-12"
      },
      {
        "Platform": "Beach House",
        "Count": "680530",
        "FirstSubmission": "2025-01-20",
        "LastSubmission": "2025-05-26"
      },
      {
        "Platform": "Little Wing",
        "Count": "667486",
        "FirstSubmission": "2023-02-19",
        "LastSubmission": "2024-05-14"
      },
      {
        "Platform": "Heron",
        "Count": "666856",
        "FirstSubmission": "2024-04-22",
        "LastSubmission": "2024-07-17"
      },
      {
        "Platform": "Cariad",
        "Count": "658191",
        "FirstSubmission": "2023-11-12",
        "LastSubmission": "2024-09-08"
      },
      {
        "Platform": "Stinkpot",
        "Count": "618213",
        "FirstSubmission": "2023-05-13",
        "LastSubmission": "2025-05-08"
      },
      {
        "Platform": "Spirit",
        "Count": "558731",
        "FirstSubmission": "2023-04-03",
        "LastSubmission": "2023-05-21"
      },
      {
        "Platform": "Witts End",
        "Count": "523870",
        "FirstSubmission": "2023-04-14",
        "LastSubmission": "2024-10-22"
      },
      {
        "Platform": "Kainoa",
        "Count": "488716",
        "FirstSubmission": "2024-02-07",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Kemosabe",
        "Count": "465330",
        "FirstSubmission": "2024-09-26",
        "LastSubmission": "2024-10-31"
      },
      {
        "Platform": "Resolution",
        "Count": "438951",
        "FirstSubmission": "2025-03-26",
        "LastSubmission": "2025-05-26"
      },
      {
        "Platform": "Proost",
        "Count": "410622",
        "FirstSubmission": "2024-11-25",
        "LastSubmission": "2025-04-27"
      },
      {
        "Platform": "Daydreams",
        "Count": "381251",
        "FirstSubmission": "2023-05-10",
        "LastSubmission": "2024-12-10"
      },
      {
        "Platform": "Carousel",
        "Count": "375768",
        "FirstSubmission": "2023-05-20",
        "LastSubmission": "2025-02-14"
      },
      {
        "Platform": "Just Us",
        "Count": "348843",
        "FirstSubmission": "2024-05-26",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Rabun",
        "Count": "304083",
        "FirstSubmission": "2024-03-27",
        "LastSubmission": "2025-01-29"
      },
      {
        "Platform": "Island Girl",
        "Count": "303803",
        "FirstSubmission": "2024-01-30",
        "LastSubmission": "2024-05-25"
      },
      {
        "Platform": "That Wat",
        "Count": "299417",
        "FirstSubmission": "2024-11-17",
        "LastSubmission": "2025-04-21"
      },
      {
        "Platform": "Typhoon",
        "Count": "295031",
        "FirstSubmission": "2024-05-12",
        "LastSubmission": "2025-03-07"
      },
      {
        "Platform": "SeaSential",
        "Count": "234363",
        "FirstSubmission": "2024-02-22",
        "LastSubmission": "2024-07-09"
      },
      {
        "Platform": "Perikana",
        "Count": "230156",
        "FirstSubmission": "2023-02-25",
        "LastSubmission": "2023-05-29"
      },
      {
        "Platform": "S_V_Freedom",
        "Count": "216973",
        "FirstSubmission": "2024-05-10",
        "LastSubmission": "2025-02-07"
      },
      {
        "Platform": "Bug Out Boat",
        "Count": "203831",
        "FirstSubmission": "2023-10-20",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Arden",
        "Count": "196753",
        "FirstSubmission": "2024-06-05",
        "LastSubmission": "2024-08-31"
      },
      {
        "Platform": "Blue Latitudes",
        "Count": "193279",
        "FirstSubmission": "2023-12-29",
        "LastSubmission": "2025-05-11"
      },
      {
        "Platform": "Unstoppable",
        "Count": "191307",
        "FirstSubmission": "2023-12-06",
        "LastSubmission": "2024-07-21"
      },
      {
        "Platform": "Fleetwing",
        "Count": "181164",
        "FirstSubmission": "2023-02-27",
        "LastSubmission": "2023-04-27"
      },
      {
        "Platform": "Malibu Moon",
        "Count": "179102",
        "FirstSubmission": "2024-10-06",
        "LastSubmission": "2025-04-13"
      },
      {
        "Platform": "Eclipse",
        "Count": "178985",
        "FirstSubmission": "2023-06-12",
        "LastSubmission": "2025-05-08"
      },
      {
        "Platform": "Atsa",
        "Count": "170344",
        "FirstSubmission": "2024-05-09",
        "LastSubmission": "2024-05-23"
      },
      {
        "Platform": "Puffin",
        "Count": "169887",
        "FirstSubmission": "2023-12-07",
        "LastSubmission": "2024-04-22"
      },
      {
        "Platform": "BuBu3",
        "Count": "168743",
        "FirstSubmission": "2023-08-06",
        "LastSubmission": "2023-09-06"
      },
      {
        "Platform": "ILE DE REY",
        "Count": "157389",
        "FirstSubmission": "2025-02-13",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Canna",
        "Count": "154372",
        "FirstSubmission": "2023-04-17",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Alectryon",
        "Count": "146751",
        "FirstSubmission": "2025-05-23",
        "LastSubmission": "2025-05-25"
      },
      {
        "Platform": "\"Another Summer \"",
        "Count": "140436",
        "FirstSubmission": "2023-07-06",
        "LastSubmission": "2024-07-16"
      },
      {
        "Platform": "TBD",
        "Count": "133385",
        "FirstSubmission": "2024-06-25",
        "LastSubmission": "2024-08-29"
      },
      {
        "Platform": "Serenity KK48",
        "Count": "128057",
        "FirstSubmission": "2023-04-14",
        "LastSubmission": "2023-05-02"
      },
      {
        "Platform": "Lady B",
        "Count": "122022",
        "FirstSubmission": "2024-09-05",
        "LastSubmission": "2024-10-20"
      },
      {
        "Platform": "Forever Young",
        "Count": "110346",
        "FirstSubmission": "2023-10-09",
        "LastSubmission": "2024-07-06"
      },
      {
        "Platform": "Flying Colors",
        "Count": "92620",
        "FirstSubmission": "2023-06-22",
        "LastSubmission": "2024-10-08"
      },
      {
        "Platform": "Bonzai",
        "Count": "87044",
        "FirstSubmission": "2023-03-06",
        "LastSubmission": "2023-04-28"
      },
      {
        "Platform": "Dulcinea",
        "Count": "75458",
        "FirstSubmission": "2023-06-09",
        "LastSubmission": "2023-06-19"
      },
      {
        "Platform": "Mira",
        "Count": "60363",
        "FirstSubmission": "2024-03-30",
        "LastSubmission": "2025-05-23"
      },
      {
        "Platform": "Anastasia",
        "Count": "58775",
        "FirstSubmission": "2025-05-09",
        "LastSubmission": "2025-05-10"
      },
      {
        "Platform": "Kairos",
        "Count": "55929",
        "FirstSubmission": "2024-04-02",
        "LastSubmission": "2024-04-20"
      },
      {
        "Platform": "Chanceux",
        "Count": "53801",
        "FirstSubmission": "2024-02-24",
        "LastSubmission": "2024-12-03"
      },
      {
        "Platform": "Hike & Sail",
        "Count": "52286",
        "FirstSubmission": "2025-04-16",
        "LastSubmission": "2025-04-16"
      },
      {
        "Platform": "Muse 10",
        "Count": "40223",
        "FirstSubmission": "2023-04-10",
        "LastSubmission": "2024-03-15"
      },
      {
        "Platform": "The Concession",
        "Count": "38110",
        "FirstSubmission": "2023-05-08",
        "LastSubmission": "2024-08-09"
      },
      {
        "Platform": "Libre",
        "Count": "37622",
        "FirstSubmission": "2023-07-23",
        "LastSubmission": "2024-10-17"
      },
      {
        "Platform": "That Way",
        "Count": "36243",
        "FirstSubmission": "2024-04-06",
        "LastSubmission": "2024-11-09"
      },
      {
        "Platform": "Taylor'd For 2",
        "Count": "34272",
        "FirstSubmission": "2024-01-27",
        "LastSubmission": "2024-04-14"
      },
      {
        "Platform": "Azur",
        "Count": "32580",
        "FirstSubmission": "2024-07-02",
        "LastSubmission": "2024-10-22"
      },
      {
        "Platform": "Biscuit",
        "Count": "29804",
        "FirstSubmission": "2024-06-08",
        "LastSubmission": "2024-06-14"
      },
      {
        "Platform": "Let's Dance",
        "Count": "26564",
        "FirstSubmission": "2025-04-30",
        "LastSubmission": "2025-05-10"
      },
      {
        "Platform": "Bluebird",
        "Count": "25765",
        "FirstSubmission": "2023-03-01",
        "LastSubmission": "2024-08-23"
      },
      {
        "Platform": "Summer  Salt",
        "Count": "25307",
        "FirstSubmission": "2024-07-17",
        "LastSubmission": "2024-12-21"
      },
      {
        "Platform": "Andiamo",
        "Count": "24755",
        "FirstSubmission": "2024-10-03",
        "LastSubmission": "2025-05-26"
      },
      {
        "Platform": "Hank The Tank",
        "Count": "21140",
        "FirstSubmission": "2023-11-11",
        "LastSubmission": "2024-10-10"
      },
      {
        "Platform": "Misty",
        "Count": "20021",
        "FirstSubmission": "2025-01-03",
        "LastSubmission": "2025-01-18"
      },
      {
        "Platform": "Canopus",
        "Count": "18674",
        "FirstSubmission": "2023-04-25",
        "LastSubmission": "2024-10-24"
      },
      {
        "Platform": "Cookie",
        "Count": "17718",
        "FirstSubmission": "2024-10-13",
        "LastSubmission": "2024-11-09"
      },
      {
        "Platform": "Perfect Agenda",
        "Count": "17182",
        "FirstSubmission": "2024-08-12",
        "LastSubmission": "2024-10-08"
      },
      {
        "Platform": "Freebird",
        "Count": "14168",
        "FirstSubmission": "2024-05-05",
        "LastSubmission": "2025-04-25"
      },
      {
        "Platform": "Consuelo",
        "Count": "12765",
        "FirstSubmission": "2024-09-23",
        "LastSubmission": "2024-11-10"
      },
      {
        "Platform": "Bella Mia",
        "Count": "11081",
        "FirstSubmission": "2024-02-28",
        "LastSubmission": "2024-03-09"
      },
      {
        "Platform": "Patience",
        "Count": "9284",
        "FirstSubmission": "2024-05-16",
        "LastSubmission": "2024-05-28"
      },
      {
        "Platform": "Voyager",
        "Count": "7570",
        "FirstSubmission": "2024-07-10",
        "LastSubmission": "2025-04-17"
      },
      {
        "Platform": "Etoile de MER",
        "Count": "6234",
        "FirstSubmission": "2023-11-13",
        "LastSubmission": "2023-11-13"
      },
      {
        "Platform": "Merlin",
        "Count": "6175",
        "FirstSubmission": "2024-02-24",
        "LastSubmission": "2024-05-27"
      },
      {
        "Platform": "Querencia",
        "Count": "5233",
        "FirstSubmission": "2023-04-20",
        "LastSubmission": "2023-07-29"
      },
      {
        "Platform": "Sweet Caroline",
        "Count": "4428",
        "FirstSubmission": "2024-07-12",
        "LastSubmission": "2024-07-16"
      },
      {
        "Platform": "Mischief Managed",
        "Count": "3613",
        "FirstSubmission": "2023-03-27",
        "LastSubmission": "2023-03-28"
      },
      {
        "Platform": "Gratitude",
        "Count": "3353",
        "FirstSubmission": "2023-11-08",
        "LastSubmission": "2024-05-30"
      },
      {
        "Platform": "Iskra",
        "Count": "3270",
        "FirstSubmission": "2025-05-24",
        "LastSubmission": "2025-05-24"
      },
      {
        "Platform": "Knot Supersonic",
        "Count": "2817",
        "FirstSubmission": "2024-06-02",
        "LastSubmission": "2024-06-12"
      },
      {
        "Platform": "Untethered",
        "Count": "2582",
        "FirstSubmission": "2024-11-01",
        "LastSubmission": "2024-11-04"
      },
      {
        "Platform": "Its About Time",
        "Count": "2465",
        "FirstSubmission": "2024-07-29",
        "LastSubmission": "2024-07-29"
      },
      {
        "Platform": "Latidoods",
        "Count": "1884",
        "FirstSubmission": "2025-05-25",
        "LastSubmission": "2025-05-25"
      },
      {
        "Platform": "Brigadoon",
        "Count": "1710",
        "FirstSubmission": "2025-02-03",
        "LastSubmission": "2025-02-03"
      },
      {
        "Platform": "Jedi",
        "Count": "1472",
        "FirstSubmission": "2024-04-01",
        "LastSubmission": "2024-11-04"
      },
      {
        "Platform": "A New Hope",
        "Count": "1407",
        "FirstSubmission": "2023-10-15",
        "LastSubmission": "2023-11-29"
      },
      {
        "Platform": "Aruna",
        "Count": "1403",
        "FirstSubmission": "2024-06-28",
        "LastSubmission": "2025-05-06"
      },
      {
        "Platform": "RV Argo",
        "Count": "1003",
        "FirstSubmission": "2024-08-08",
        "LastSubmission": "2024-08-08"
      },
      {
        "Platform": "Three Seas",
        "Count": "799",
        "FirstSubmission": "2024-04-02",
        "LastSubmission": "2024-04-06"
      },
      {
        "Platform": "\"Airwaves \"",
        "Count": "518",
        "FirstSubmission": "2023-04-11",
        "LastSubmission": "2023-04-15"
      },
      {
        "Platform": "Privateer",
        "Count": "386",
        "FirstSubmission": "2023-11-02",
        "LastSubmission": "2023-11-02"
      },
      {
        "Platform": "Seabatical II",
        "Count": "332",
        "FirstSubmission": "2025-01-17",
        "LastSubmission": "2025-01-17"
      },
      {
        "Platform": "Regular Eggs",
        "Count": "323",
        "FirstSubmission": "2023-11-21",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Astrid",
        "Count": "263",
        "FirstSubmission": "2023-12-25",
        "LastSubmission": "2023-12-25"
      },
      {
        "Platform": "Treasure island",
        "Count": "171",
        "FirstSubmission": "2024-05-08",
        "LastSubmission": "2024-05-08"
      },
      {
        "Platform": "Sanook",
        "Count": "147",
        "FirstSubmission": "2023-10-27",
        "LastSubmission": "2023-10-27"
      },
      {
        "Platform": "Stella mari",
        "Count": "142",
        "FirstSubmission": "2025-04-12",
        "LastSubmission": "2025-04-12"
      },
      {
        "Platform": "Surrendered Life",
        "Count": "133",
        "FirstSubmission": "2023-04-03",
        "LastSubmission": "2023-04-04"
      },
      {
        "Platform": "Granata",
        "Count": "97",
        "FirstSubmission": "2023-12-18",
        "LastSubmission": "2024-01-26"
      },
      {
        "Platform": "Hear We Go",
        "Count": "81",
        "FirstSubmission": "2023-06-04",
        "LastSubmission": "2023-06-04"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2025-05-01 00:00:00.000",
        "Count": "3520036"
      },
      {
        "Month": "2025-04-01 00:00:00.000",
        "Count": "9534339"
      },
      {
        "Month": "2025-03-01 00:00:00.000",
        "Count": "5900361"
      },
      {
        "Month": "2025-02-01 00:00:00.000",
        "Count": "1719223"
      },
      {
        "Month": "2025-01-01 00:00:00.000",
        "Count": "5629270"
      },
      {
        "Month": "2024-12-01 00:00:00.000",
        "Count": "10797692"
      },
      {
        "Month": "2024-11-01 00:00:00.000",
        "Count": "10630971"
      },
      {
        "Month": "2024-10-01 00:00:00.000",
        "Count": "5341572"
      },
      {
        "Month": "2024-09-01 00:00:00.000",
        "Count": "1949787"
      },
      {
        "Month": "2024-08-01 00:00:00.000",
        "Count": "1865028"
      },
      {
        "Month": "2024-07-01 00:00:00.000",
        "Count": "1702566"
      },
      {
        "Month": "2024-06-01 00:00:00.000",
        "Count": "3437683"
      },
      {
        "Month": "2024-05-01 00:00:00.000",
        "Count": "5203235"
      },
      {
        "Month": "2024-04-01 00:00:00.000",
        "Count": "5056293"
      },
      {
        "Month": "2024-03-01 00:00:00.000",
        "Count": "2303176"
      },
      {
        "Month": "2024-02-01 00:00:00.000",
        "Count": "788268"
      },
      {
        "Month": "2024-01-01 00:00:00.000",
        "Count": "1575869"
      },
      {
        "Month": "2023-12-01 00:00:00.000",
        "Count": "1723388"
      },
      {
        "Month": "2023-11-01 00:00:00.000",
        "Count": "2921703"
      },
      {
        "Month": "2023-10-01 00:00:00.000",
        "Count": "2302612"
      },
      {
        "Month": "2023-09-01 00:00:00.000",
        "Count": "1177826"
      },
      {
        "Month": "2023-08-01 00:00:00.000",
        "Count": "803167"
      },
      {
        "Month": "2023-07-01 00:00:00.000",
        "Count": "1642930"
      },
      {
        "Month": "2023-06-01 00:00:00.000",
        "Count": "1144757"
      },
      {
        "Month": "2023-05-01 00:00:00.000",
        "Count": "1810425"
      },
      {
        "Month": "2023-04-01 00:00:00.000",
        "Count": "1583366"
      },
      {
        "Month": "2023-03-01 00:00:00.000",
        "Count": "588239"
      },
      {
        "Month": "2023-02-01 00:00:00.000",
        "Count": "100591"
      }
    ],
    "ActiveProvider": "true"
  },
  {
    "Provider": "CIDCO",
    "RecordCount": "15480",
    "PlatformCount": "2",
    "MinDateTime": "2022-10-13 06:34:23.310",
    "MaxDateTime": "2024-09-12 07:52:56.755",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "BELLA DESGAGNES",
        "Count": "14888",
        "FirstSubmission": "2023-11-22",
        "LastSubmission": "2024-09-12"
      },
      {
        "Platform": "Numas - Tlowitsis",
        "Count": "592",
        "FirstSubmission": "2024-04-11",
        "LastSubmission": "2024-04-11"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2024-09-01 00:00:00.000",
        "Count": "3602"
      },
      {
        "Month": "2023-12-01 00:00:00.000",
        "Count": "7092"
      },
      {
        "Month": "2023-11-01 00:00:00.000",
        "Count": "3602"
      },
      {
        "Month": "2022-10-01 00:00:00.000",
        "Count": "1184"
      }
    ],
    "ActiveProvider": "false"
  },
  {
    "Provider": "COMIT USF",
    "RecordCount": "5154188",
    "PlatformCount": "10",
    "MinDateTime": "2024-02-14 20:06:40.000",
    "MaxDateTime": "2025-05-28 13:55:44.000",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "COMIT 3 - Rescue 7 (Eckerd College)",
        "Count": "2243970",
        "FirstSubmission": "2024-06-28",
        "LastSubmission": "2025-05-11"
      },
      {
        "Platform": "COMIT 2 - Rescue 5 (Eckerd College)",
        "Count": "1350020",
        "FirstSubmission": "2024-06-25",
        "LastSubmission": "2025-04-06"
      },
      {
        "Platform": "COMIT 4 - Privateer (Pinellas County)",
        "Count": "299330",
        "FirstSubmission": "2024-06-25",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "COMIT 3",
        "Count": "289210",
        "FirstSubmission": "2024-04-20",
        "LastSubmission": "2024-05-14"
      },
      {
        "Platform": "COMIT 1 - Rescue 4 (Eckerd College)",
        "Count": "280732",
        "FirstSubmission": "2025-04-11",
        "LastSubmission": "2025-04-30"
      },
      {
        "Platform": "MC-29",
        "Count": "268736",
        "FirstSubmission": "2024-05-15",
        "LastSubmission": "2024-05-15"
      },
      {
        "Platform": "COMIT 3 - Rescue 7",
        "Count": "169600",
        "FirstSubmission": "2024-05-28",
        "LastSubmission": "2024-06-23"
      },
      {
        "Platform": "COMIT 2",
        "Count": "134940",
        "FirstSubmission": "2024-04-20",
        "LastSubmission": "2024-05-11"
      },
      {
        "Platform": "COMIT 2 - Rescue 5",
        "Count": "108148",
        "FirstSubmission": "2024-05-18",
        "LastSubmission": "2024-06-23"
      },
      {
        "Platform": "COMIT 4",
        "Count": "9502",
        "FirstSubmission": "2024-06-13",
        "LastSubmission": "2024-06-25"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2025-05-01 00:00:00.000",
        "Count": "65874"
      },
      {
        "Month": "2025-04-01 00:00:00.000",
        "Count": "663786"
      },
      {
        "Month": "2025-03-01 00:00:00.000",
        "Count": "550728"
      },
      {
        "Month": "2025-02-01 00:00:00.000",
        "Count": "521104"
      },
      {
        "Month": "2025-01-01 00:00:00.000",
        "Count": "57500"
      },
      {
        "Month": "2024-12-01 00:00:00.000",
        "Count": "90474"
      },
      {
        "Month": "2024-11-01 00:00:00.000",
        "Count": "806378"
      },
      {
        "Month": "2024-10-01 00:00:00.000",
        "Count": "50000"
      },
      {
        "Month": "2024-09-01 00:00:00.000",
        "Count": "369480"
      },
      {
        "Month": "2024-08-01 00:00:00.000",
        "Count": "835698"
      },
      {
        "Month": "2024-07-01 00:00:00.000",
        "Count": "110238"
      },
      {
        "Month": "2024-06-01 00:00:00.000",
        "Count": "285366"
      },
      {
        "Month": "2024-05-01 00:00:00.000",
        "Count": "266690"
      },
      {
        "Month": "2024-04-01 00:00:00.000",
        "Count": "212136"
      },
      {
        "Month": "2024-02-01 00:00:00.000",
        "Count": "268736"
      }
    ],
    "ActiveProvider": "true"
  },
  {
    "Provider": "Carnival",
    "RecordCount": "12252879",
    "PlatformCount": "82",
    "MinDateTime": "2024-11-16 00:00:00.000",
    "MaxDateTime": "2025-05-28 23:59:30.000",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "AIDAsol",
        "Count": "527232",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-27"
      },
      {
        "Platform": "AIDAnova",
        "Count": "498567",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Carnival Spirit",
        "Count": "498135",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Queen Mary 2",
        "Count": "485103",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Carnival Pride",
        "Count": "458653",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "MS Westerdam",
        "Count": "420386",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Carnival Sunshine",
        "Count": "384337",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Aurora",
        "Count": "362158",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-09"
      },
      {
        "Platform": "Carnival Elation",
        "Count": "343768",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Sapphire Princess",
        "Count": "331397",
        "FirstSubmission": "2025-03-27",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Grand Princess",
        "Count": "325630",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "AIDAmar",
        "Count": "324072",
        "FirstSubmission": "2025-03-26",
        "LastSubmission": "2025-05-24"
      },
      {
        "Platform": "MS Koningsdam",
        "Count": "302211",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Discovery Princess",
        "Count": "297821",
        "FirstSubmission": "2025-03-31",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Carnival Radiance",
        "Count": "233406",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-27"
      },
      {
        "Platform": "MS Zuiderdam",
        "Count": "229910",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Iona",
        "Count": "224136",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Carnival Paradise",
        "Count": "218919",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Carnival Miracle",
        "Count": "218510",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Carnival Dream",
        "Count": "200303",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Ventura",
        "Count": "190676",
        "FirstSubmission": "2025-03-26",
        "LastSubmission": "2025-05-24"
      },
      {
        "Platform": "Carnival Valor",
        "Count": "189003",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-25"
      },
      {
        "Platform": "AIDAperla",
        "Count": "181172",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Carnival Legend",
        "Count": "178017",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Carnival Breeze",
        "Count": "175503",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "MS Eurodam",
        "Count": "169651",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "MS Nieuw Amsterdam",
        "Count": "167067",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Carnival Liberty",
        "Count": "165333",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Carnival Splendor",
        "Count": "163353",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-09"
      },
      {
        "Platform": "Caribbean Princess",
        "Count": "158012",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Arvia",
        "Count": "146814",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-09"
      },
      {
        "Platform": "MS Rotterdam",
        "Count": "146463",
        "FirstSubmission": "2025-03-26",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Seabourn Encore",
        "Count": "144333",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-24"
      },
      {
        "Platform": "Carnival Glory",
        "Count": "142933",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-27"
      },
      {
        "Platform": "AIDAbella",
        "Count": "141775",
        "FirstSubmission": "2025-03-27",
        "LastSubmission": "2025-05-27"
      },
      {
        "Platform": "Ruby Princess",
        "Count": "138187",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Carnival Venezia",
        "Count": "135849",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Coral Princess",
        "Count": "135525",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Seabourn Ovation",
        "Count": "126755",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-09"
      },
      {
        "Platform": "Costa Deliziosa",
        "Count": "126689",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-09"
      },
      {
        "Platform": "AIDAluna",
        "Count": "123614",
        "FirstSubmission": "2025-04-10",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "AIDAprima",
        "Count": "123233",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Royal Princess",
        "Count": "117818",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "MS Noordam",
        "Count": "112076",
        "FirstSubmission": "2025-05-01",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Carnival Jubilee",
        "Count": "110432",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Carnival Luminosa",
        "Count": "109266",
        "FirstSubmission": "2025-03-27",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Carnival Firenze",
        "Count": "103812",
        "FirstSubmission": "2025-03-27",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Queen Anne",
        "Count": "102382",
        "FirstSubmission": "2025-03-30",
        "LastSubmission": "2025-05-27"
      },
      {
        "Platform": "MS Zaandam",
        "Count": "96452",
        "FirstSubmission": "2025-03-26",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Costa Fascinosa",
        "Count": "92136",
        "FirstSubmission": "2025-03-29",
        "LastSubmission": "2025-05-09"
      },
      {
        "Platform": "MS Volendam",
        "Count": "90198",
        "FirstSubmission": "2025-03-26",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Costa Smeralda",
        "Count": "87774",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-09"
      },
      {
        "Platform": "Sky Princess",
        "Count": "86141",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Regal Princess",
        "Count": "75203",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-09"
      },
      {
        "Platform": "Carnival Horizon",
        "Count": "74829",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Arcadia",
        "Count": "64147",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Seabourn Quest",
        "Count": "63855",
        "FirstSubmission": "2025-05-08",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "MS Nieuw Statendam",
        "Count": "63498",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Carnival Conquest",
        "Count": "54869",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-24"
      },
      {
        "Platform": "Carnival Celebration",
        "Count": "52527",
        "FirstSubmission": "2025-03-26",
        "LastSubmission": "2025-05-25"
      },
      {
        "Platform": "Britannia",
        "Count": "46188",
        "FirstSubmission": "2025-03-26",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "MS Oosterdam",
        "Count": "42122",
        "FirstSubmission": "2025-03-26",
        "LastSubmission": "2025-05-27"
      },
      {
        "Platform": "Carnival Magic",
        "Count": "41990",
        "FirstSubmission": "2025-03-26",
        "LastSubmission": "2025-05-24"
      },
      {
        "Platform": "Sun Princess",
        "Count": "40909",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-09"
      },
      {
        "Platform": "Emerald Princess",
        "Count": "38343",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Island Princess",
        "Count": "36662",
        "FirstSubmission": "2025-03-25",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "AIDAdiva",
        "Count": "28350",
        "FirstSubmission": "2025-04-30",
        "LastSubmission": "2025-05-27"
      },
      {
        "Platform": "Queen Victoria",
        "Count": "26061",
        "FirstSubmission": "2025-03-26",
        "LastSubmission": "2025-05-24"
      },
      {
        "Platform": "Costa Fortuna",
        "Count": "23860",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-27"
      },
      {
        "Platform": "Crown Princess",
        "Count": "20412",
        "FirstSubmission": "2025-03-27",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Costa Favolosa",
        "Count": "16199",
        "FirstSubmission": "2025-05-10",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Carnival Freedom",
        "Count": "15775",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Mardi Gras",
        "Count": "13938",
        "FirstSubmission": "2025-03-27",
        "LastSubmission": "2025-05-25"
      },
      {
        "Platform": "Carnival Vista",
        "Count": "11607",
        "FirstSubmission": "2025-04-14",
        "LastSubmission": "2025-05-24"
      },
      {
        "Platform": "Costa Diadema",
        "Count": "9893",
        "FirstSubmission": "2025-04-30",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Carnival Encounter",
        "Count": "8190",
        "FirstSubmission": "2025-05-08",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Enchanted Princess",
        "Count": "7680",
        "FirstSubmission": "2025-03-26",
        "LastSubmission": "2025-05-24"
      },
      {
        "Platform": "Seabourn Sojourn",
        "Count": "5189",
        "FirstSubmission": "2025-04-05",
        "LastSubmission": "2025-05-07"
      },
      {
        "Platform": "AIDAstella",
        "Count": "3168",
        "FirstSubmission": "2025-05-24",
        "LastSubmission": "2025-05-27"
      },
      {
        "Platform": "Diamond Princess",
        "Count": "1904",
        "FirstSubmission": "2025-03-27",
        "LastSubmission": "2025-04-29"
      },
      {
        "Platform": "Carnival Adventure",
        "Count": "1223",
        "FirstSubmission": "2025-05-24",
        "LastSubmission": "2025-05-24"
      },
      {
        "Platform": "Carnival Panorama",
        "Count": "1190",
        "FirstSubmission": "2025-05-24",
        "LastSubmission": "2025-05-27"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2025-05-01 00:00:00.000",
        "Count": "2559807"
      },
      {
        "Month": "2025-04-01 00:00:00.000",
        "Count": "4274747"
      },
      {
        "Month": "2025-03-01 00:00:00.000",
        "Count": "5255233"
      },
      {
        "Month": "2025-02-01 00:00:00.000",
        "Count": "159324"
      },
      {
        "Month": "2025-01-01 00:00:00.000",
        "Count": "2250"
      },
      {
        "Month": "2024-11-01 00:00:00.000",
        "Count": "1518"
      }
    ],
    "ActiveProvider": "true"
  },
  {
    "Provider": "FarSounder",
    "RecordCount": "13393501",
    "PlatformCount": "1",
    "MinDateTime": "2017-10-07 13:08:47.094",
    "MaxDateTime": "2025-05-28 08:53:16.461",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "Anonymous",
        "Count": "13393501",
        "FirstSubmission": "2019-10-04",
        "LastSubmission": "2025-05-28"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2025-05-01 00:00:00.000",
        "Count": "367755"
      },
      {
        "Month": "2025-04-01 00:00:00.000",
        "Count": "609910"
      },
      {
        "Month": "2025-03-01 00:00:00.000",
        "Count": "17819"
      },
      {
        "Month": "2025-02-01 00:00:00.000",
        "Count": "16535"
      },
      {
        "Month": "2025-01-01 00:00:00.000",
        "Count": "85783"
      },
      {
        "Month": "2024-12-01 00:00:00.000",
        "Count": "438467"
      },
      {
        "Month": "2024-11-01 00:00:00.000",
        "Count": "153458"
      },
      {
        "Month": "2024-10-01 00:00:00.000",
        "Count": "265194"
      },
      {
        "Month": "2024-09-01 00:00:00.000",
        "Count": "679323"
      },
      {
        "Month": "2024-08-01 00:00:00.000",
        "Count": "2735342"
      },
      {
        "Month": "2024-07-01 00:00:00.000",
        "Count": "2034361"
      },
      {
        "Month": "2024-06-01 00:00:00.000",
        "Count": "1446934"
      },
      {
        "Month": "2024-05-01 00:00:00.000",
        "Count": "1367947"
      },
      {
        "Month": "2024-04-01 00:00:00.000",
        "Count": "206"
      },
      {
        "Month": "2024-03-01 00:00:00.000",
        "Count": "396244"
      },
      {
        "Month": "2022-02-01 00:00:00.000",
        "Count": "665254"
      },
      {
        "Month": "2022-01-01 00:00:00.000",
        "Count": "507521"
      },
      {
        "Month": "2019-09-01 00:00:00.000",
        "Count": "169111"
      },
      {
        "Month": "2019-08-01 00:00:00.000",
        "Count": "169024"
      },
      {
        "Month": "2019-05-01 00:00:00.000",
        "Count": "199263"
      },
      {
        "Month": "2019-03-01 00:00:00.000",
        "Count": "65985"
      },
      {
        "Month": "2018-02-01 00:00:00.000",
        "Count": "299401"
      },
      {
        "Month": "2018-01-01 00:00:00.000",
        "Count": "265313"
      },
      {
        "Month": "2017-12-01 00:00:00.000",
        "Count": "337341"
      },
      {
        "Month": "2017-10-01 00:00:00.000",
        "Count": "100010"
      }
    ],
    "ActiveProvider": "true"
  },
  {
    "Provider": "GLOS",
    "RecordCount": "28016755",
    "PlatformCount": "11",
    "MinDateTime": "2021-04-25 17:43:47.000",
    "MaxDateTime": "2025-05-29 19:06:54.000",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "PARA Marine",
        "Count": "14335036",
        "FirstSubmission": "2022-07-20",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Huron Explorer",
        "Count": "3020437",
        "FirstSubmission": "2024-05-21",
        "LastSubmission": "2025-05-27"
      },
      {
        "Platform": "Erie Explorer",
        "Count": "2282038",
        "FirstSubmission": "2022-07-20",
        "LastSubmission": "2023-11-23"
      },
      {
        "Platform": "RV Northwestern",
        "Count": "1870480",
        "FirstSubmission": "2022-10-10",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Orange Apex",
        "Count": "1490130",
        "FirstSubmission": "2022-07-20",
        "LastSubmission": "2023-04-29"
      },
      {
        "Platform": "Vigilant",
        "Count": "1184272",
        "FirstSubmission": "2023-06-05",
        "LastSubmission": "2025-01-04"
      },
      {
        "Platform": "Erie Guardian",
        "Count": "1156624",
        "FirstSubmission": "2022-07-20",
        "LastSubmission": "2025-01-04"
      },
      {
        "Platform": "Keenosay",
        "Count": "991924",
        "FirstSubmission": "2022-07-26",
        "LastSubmission": "2024-07-17"
      },
      {
        "Platform": "SV Wind Goddess",
        "Count": "949674",
        "FirstSubmission": "2024-08-04",
        "LastSubmission": "2024-09-11"
      },
      {
        "Platform": "RV Cisco",
        "Count": "369780",
        "FirstSubmission": "2022-09-27",
        "LastSubmission": "2023-11-23"
      },
      {
        "Platform": "Ontario Explorer",
        "Count": "366360",
        "FirstSubmission": "2022-07-20",
        "LastSubmission": "2024-08-03"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2025-05-01 00:00:00.000",
        "Count": "182070"
      },
      {
        "Month": "2025-04-01 00:00:00.000",
        "Count": "94698"
      },
      {
        "Month": "2025-01-01 00:00:00.000",
        "Count": "2130"
      },
      {
        "Month": "2024-11-01 00:00:00.000",
        "Count": "79504"
      },
      {
        "Month": "2024-10-01 00:00:00.000",
        "Count": "406848"
      },
      {
        "Month": "2024-09-01 00:00:00.000",
        "Count": "1230260"
      },
      {
        "Month": "2024-08-01 00:00:00.000",
        "Count": "1329644"
      },
      {
        "Month": "2024-07-01 00:00:00.000",
        "Count": "2474550"
      },
      {
        "Month": "2024-06-01 00:00:00.000",
        "Count": "1741929"
      },
      {
        "Month": "2024-05-01 00:00:00.000",
        "Count": "1329920"
      },
      {
        "Month": "2024-04-01 00:00:00.000",
        "Count": "392584"
      },
      {
        "Month": "2023-11-01 00:00:00.000",
        "Count": "74284"
      },
      {
        "Month": "2023-10-01 00:00:00.000",
        "Count": "1355146"
      },
      {
        "Month": "2023-09-01 00:00:00.000",
        "Count": "1189648"
      },
      {
        "Month": "2023-08-01 00:00:00.000",
        "Count": "1360408"
      },
      {
        "Month": "2023-07-01 00:00:00.000",
        "Count": "2124316"
      },
      {
        "Month": "2023-06-01 00:00:00.000",
        "Count": "2515642"
      },
      {
        "Month": "2023-05-01 00:00:00.000",
        "Count": "825508"
      },
      {
        "Month": "2023-04-01 00:00:00.000",
        "Count": "229340"
      },
      {
        "Month": "2022-11-01 00:00:00.000",
        "Count": "480670"
      },
      {
        "Month": "2022-10-01 00:00:00.000",
        "Count": "715840"
      },
      {
        "Month": "2022-09-01 00:00:00.000",
        "Count": "914268"
      },
      {
        "Month": "2022-08-01 00:00:00.000",
        "Count": "1277988"
      },
      {
        "Month": "2022-07-01 00:00:00.000",
        "Count": "979946"
      },
      {
        "Month": "2022-06-01 00:00:00.000",
        "Count": "569110"
      },
      {
        "Month": "2022-05-01 00:00:00.000",
        "Count": "406188"
      },
      {
        "Month": "2022-04-01 00:00:00.000",
        "Count": "65864"
      },
      {
        "Month": "2022-03-01 00:00:00.000",
        "Count": "4518"
      },
      {
        "Month": "2021-11-01 00:00:00.000",
        "Count": "11454"
      },
      {
        "Month": "2021-10-01 00:00:00.000",
        "Count": "564744"
      },
      {
        "Month": "2021-09-01 00:00:00.000",
        "Count": "1213372"
      },
      {
        "Month": "2021-08-01 00:00:00.000",
        "Count": "869832"
      },
      {
        "Month": "2021-07-01 00:00:00.000",
        "Count": "534596"
      },
      {
        "Month": "2021-06-01 00:00:00.000",
        "Count": "336486"
      },
      {
        "Month": "2021-05-01 00:00:00.000",
        "Count": "123916"
      },
      {
        "Month": "2021-04-01 00:00:00.000",
        "Count": "9534"
      }
    ],
    "ActiveProvider": "true"
  },
  {
    "Provider": "M2Ocean",
    "RecordCount": "128995",
    "PlatformCount": "1",
    "MinDateTime": "2020-08-12 15:30:54.068",
    "MaxDateTime": "2021-09-02 16:54:03.028",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "Anonymous",
        "Count": "128995",
        "FirstSubmission": "2022-05-23",
        "LastSubmission": "2022-05-23"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2021-09-01 00:00:00.000",
        "Count": "9247"
      },
      {
        "Month": "2021-08-01 00:00:00.000",
        "Count": "17485"
      },
      {
        "Month": "2021-07-01 00:00:00.000",
        "Count": "54397"
      },
      {
        "Month": "2020-09-01 00:00:00.000",
        "Count": "14491"
      },
      {
        "Month": "2020-08-01 00:00:00.000",
        "Count": "33375"
      }
    ],
    "ActiveProvider": "false"
  },
  {
    "Provider": "MacGregor",
    "RecordCount": "23642442",
    "PlatformCount": "11",
    "MinDateTime": "2020-02-04 21:41:55.000",
    "MaxDateTime": "2020-12-03 13:29:12.000",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "Anonymous",
        "Count": "22003245",
        "FirstSubmission": "2020-02-18",
        "LastSubmission": "2020-12-03"
      },
      {
        "Platform": "AIDAcara",
        "Count": "483673",
        "FirstSubmission": "2020-02-18",
        "LastSubmission": "2020-12-03"
      },
      {
        "Platform": "AIDAnova",
        "Count": "355667",
        "FirstSubmission": "2020-02-23",
        "LastSubmission": "2020-09-02"
      },
      {
        "Platform": "AIDAluna",
        "Count": "231868",
        "FirstSubmission": "2020-02-25",
        "LastSubmission": "2020-08-01"
      },
      {
        "Platform": "AIDAmar",
        "Count": "146512",
        "FirstSubmission": "2020-02-21",
        "LastSubmission": "2020-10-19"
      },
      {
        "Platform": "AIDAblu",
        "Count": "111928",
        "FirstSubmission": "2020-04-16",
        "LastSubmission": "2020-10-09"
      },
      {
        "Platform": "AIDAprima",
        "Count": "99553",
        "FirstSubmission": "2020-10-09",
        "LastSubmission": "2020-10-17"
      },
      {
        "Platform": "AIDAperla",
        "Count": "92538",
        "FirstSubmission": "2020-02-22",
        "LastSubmission": "2020-12-02"
      },
      {
        "Platform": "AIDAaura",
        "Count": "85632",
        "FirstSubmission": "2020-02-21",
        "LastSubmission": "2020-07-15"
      },
      {
        "Platform": "AIDAdiva",
        "Count": "31454",
        "FirstSubmission": "2020-03-31",
        "LastSubmission": "2020-12-02"
      },
      {
        "Platform": "AIDAsol",
        "Count": "372",
        "FirstSubmission": "2020-02-23",
        "LastSubmission": "2020-03-01"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2020-12-01 00:00:00.000",
        "Count": "113433"
      },
      {
        "Month": "2020-11-01 00:00:00.000",
        "Count": "82703"
      },
      {
        "Month": "2020-10-01 00:00:00.000",
        "Count": "813488"
      },
      {
        "Month": "2020-09-01 00:00:00.000",
        "Count": "13756"
      },
      {
        "Month": "2020-08-01 00:00:00.000",
        "Count": "504038"
      },
      {
        "Month": "2020-07-01 00:00:00.000",
        "Count": "4462634"
      },
      {
        "Month": "2020-06-01 00:00:00.000",
        "Count": "1760332"
      },
      {
        "Month": "2020-05-01 00:00:00.000",
        "Count": "4296786"
      },
      {
        "Month": "2020-04-01 00:00:00.000",
        "Count": "2424572"
      },
      {
        "Month": "2020-03-01 00:00:00.000",
        "Count": "6278096"
      },
      {
        "Month": "2020-02-01 00:00:00.000",
        "Count": "2892604"
      }
    ],
    "ActiveProvider": "false"
  },
  {
    "Provider": "OMS Group",
    "RecordCount": "7087",
    "PlatformCount": "2",
    "MinDateTime": "2024-04-11 04:20:47.840",
    "MaxDateTime": "2025-01-20 22:54:41.410",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "Cable Vigilance",
        "Count": "6887",
        "FirstSubmission": "2024-11-20",
        "LastSubmission": "2025-01-21"
      },
      {
        "Platform": "Lodbrog",
        "Count": "200",
        "FirstSubmission": "2025-01-29",
        "LastSubmission": "2025-01-29"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2025-01-01 00:00:00.000",
        "Count": "77"
      },
      {
        "Month": "2024-12-01 00:00:00.000",
        "Count": "6211"
      },
      {
        "Month": "2024-09-01 00:00:00.000",
        "Count": "73"
      },
      {
        "Month": "2024-04-01 00:00:00.000",
        "Count": "726"
      }
    ],
    "ActiveProvider": "false"
  },
  {
    "Provider": "Orange Force Marine",
    "RecordCount": "4691424",
    "PlatformCount": "4",
    "MinDateTime": "2022-12-28 18:15:31.000",
    "MaxDateTime": "2025-04-29 01:20:55.000",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "USF - Sunlife",
        "Count": "3015328",
        "FirstSubmission": "2023-10-27",
        "LastSubmission": "2023-11-22"
      },
      {
        "Platform": "NIWA Orca",
        "Count": "1372200",
        "FirstSubmission": "2025-01-07",
        "LastSubmission": "2025-04-29"
      },
      {
        "Platform": "Sunlife",
        "Count": "302098",
        "FirstSubmission": "2023-01-17",
        "LastSubmission": "2023-04-16"
      },
      {
        "Platform": "TBD 15",
        "Count": "1798",
        "FirstSubmission": "2023-01-17",
        "LastSubmission": "2023-01-17"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2025-04-01 00:00:00.000",
        "Count": "57254"
      },
      {
        "Month": "2025-03-01 00:00:00.000",
        "Count": "342432"
      },
      {
        "Month": "2025-02-01 00:00:00.000",
        "Count": "517044"
      },
      {
        "Month": "2025-01-01 00:00:00.000",
        "Count": "356514"
      },
      {
        "Month": "2024-12-01 00:00:00.000",
        "Count": "86472"
      },
      {
        "Month": "2024-11-01 00:00:00.000",
        "Count": "12484"
      },
      {
        "Month": "2023-04-01 00:00:00.000",
        "Count": "460172"
      },
      {
        "Month": "2023-03-01 00:00:00.000",
        "Count": "1184336"
      },
      {
        "Month": "2023-02-01 00:00:00.000",
        "Count": "1020270"
      },
      {
        "Month": "2023-01-01 00:00:00.000",
        "Count": "647514"
      },
      {
        "Month": "2022-12-01 00:00:00.000",
        "Count": "6932"
      }
    ],
    "ActiveProvider": "false"
  },
  {
    "Provider": "PGS",
    "RecordCount": "49785831",
    "PlatformCount": "6",
    "MinDateTime": "2019-12-23 11:34:13.000",
    "MaxDateTime": "2025-05-29 21:59:59.000",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "Ramform Hyperion",
        "Count": "13236911",
        "FirstSubmission": "2021-05-12",
        "LastSubmission": "2025-04-04"
      },
      {
        "Platform": "Ramform Atlas",
        "Count": "11654726",
        "FirstSubmission": "2021-01-11",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Ramform Titan",
        "Count": "7538291",
        "FirstSubmission": "2020-12-02",
        "LastSubmission": "2025-05-07"
      },
      {
        "Platform": "Ramform Vanguard",
        "Count": "7276901",
        "FirstSubmission": "2021-06-05",
        "LastSubmission": "2025-04-16"
      },
      {
        "Platform": "Ramform Sovereign",
        "Count": "5516137",
        "FirstSubmission": "2021-01-08",
        "LastSubmission": "2025-01-19"
      },
      {
        "Platform": "Ramform Tethys",
        "Count": "4562865",
        "FirstSubmission": "2021-05-13",
        "LastSubmission": "2025-05-29"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2025-05-01 00:00:00.000",
        "Count": "446766"
      },
      {
        "Month": "2025-04-01 00:00:00.000",
        "Count": "495006"
      },
      {
        "Month": "2025-03-01 00:00:00.000",
        "Count": "507471"
      },
      {
        "Month": "2025-02-01 00:00:00.000",
        "Count": "641490"
      },
      {
        "Month": "2025-01-01 00:00:00.000",
        "Count": "285166"
      },
      {
        "Month": "2024-12-01 00:00:00.000",
        "Count": "369417"
      },
      {
        "Month": "2024-11-01 00:00:00.000",
        "Count": "514679"
      },
      {
        "Month": "2024-10-01 00:00:00.000",
        "Count": "21616"
      },
      {
        "Month": "2024-09-01 00:00:00.000",
        "Count": "472433"
      },
      {
        "Month": "2024-08-01 00:00:00.000",
        "Count": "1516451"
      },
      {
        "Month": "2024-07-01 00:00:00.000",
        "Count": "1129135"
      },
      {
        "Month": "2024-06-01 00:00:00.000",
        "Count": "1550524"
      },
      {
        "Month": "2024-05-01 00:00:00.000",
        "Count": "1219950"
      },
      {
        "Month": "2024-04-01 00:00:00.000",
        "Count": "966901"
      },
      {
        "Month": "2024-03-01 00:00:00.000",
        "Count": "602266"
      },
      {
        "Month": "2024-02-01 00:00:00.000",
        "Count": "720414"
      },
      {
        "Month": "2024-01-01 00:00:00.000",
        "Count": "753710"
      },
      {
        "Month": "2023-12-01 00:00:00.000",
        "Count": "582390"
      },
      {
        "Month": "2023-11-01 00:00:00.000",
        "Count": "391409"
      },
      {
        "Month": "2023-10-01 00:00:00.000",
        "Count": "646169"
      },
      {
        "Month": "2023-09-01 00:00:00.000",
        "Count": "1138986"
      },
      {
        "Month": "2023-08-01 00:00:00.000",
        "Count": "1764347"
      },
      {
        "Month": "2023-07-01 00:00:00.000",
        "Count": "1773045"
      },
      {
        "Month": "2023-06-01 00:00:00.000",
        "Count": "1902255"
      },
      {
        "Month": "2023-05-01 00:00:00.000",
        "Count": "1589480"
      },
      {
        "Month": "2023-04-01 00:00:00.000",
        "Count": "726659"
      },
      {
        "Month": "2023-03-01 00:00:00.000",
        "Count": "141278"
      },
      {
        "Month": "2023-02-01 00:00:00.000",
        "Count": "221857"
      },
      {
        "Month": "2023-01-01 00:00:00.000",
        "Count": "124748"
      },
      {
        "Month": "2022-11-01 00:00:00.000",
        "Count": "187942"
      },
      {
        "Month": "2022-10-01 00:00:00.000",
        "Count": "635239"
      },
      {
        "Month": "2022-09-01 00:00:00.000",
        "Count": "1527021"
      },
      {
        "Month": "2022-08-01 00:00:00.000",
        "Count": "2195348"
      },
      {
        "Month": "2022-07-01 00:00:00.000",
        "Count": "2989525"
      },
      {
        "Month": "2022-06-01 00:00:00.000",
        "Count": "2280141"
      },
      {
        "Month": "2022-05-01 00:00:00.000",
        "Count": "3460"
      },
      {
        "Month": "2022-04-01 00:00:00.000",
        "Count": "1198"
      },
      {
        "Month": "2022-03-01 00:00:00.000",
        "Count": "318095"
      },
      {
        "Month": "2022-02-01 00:00:00.000",
        "Count": "592462"
      },
      {
        "Month": "2022-01-01 00:00:00.000",
        "Count": "85532"
      },
      {
        "Month": "2021-12-01 00:00:00.000",
        "Count": "144294"
      },
      {
        "Month": "2021-11-01 00:00:00.000",
        "Count": "31362"
      },
      {
        "Month": "2021-10-01 00:00:00.000",
        "Count": "1182273"
      },
      {
        "Month": "2021-09-01 00:00:00.000",
        "Count": "2101225"
      },
      {
        "Month": "2021-08-01 00:00:00.000",
        "Count": "3219028"
      },
      {
        "Month": "2021-07-01 00:00:00.000",
        "Count": "3670919"
      },
      {
        "Month": "2021-06-01 00:00:00.000",
        "Count": "3296595"
      },
      {
        "Month": "2021-05-01 00:00:00.000",
        "Count": "1261765"
      },
      {
        "Month": "2021-04-01 00:00:00.000",
        "Count": "15909"
      },
      {
        "Month": "2021-03-01 00:00:00.000",
        "Count": "53278"
      },
      {
        "Month": "2021-02-01 00:00:00.000",
        "Count": "320705"
      },
      {
        "Month": "2021-01-01 00:00:00.000",
        "Count": "323633"
      },
      {
        "Month": "2020-12-01 00:00:00.000",
        "Count": "16588"
      },
      {
        "Month": "2020-11-01 00:00:00.000",
        "Count": "9844"
      },
      {
        "Month": "2020-10-01 00:00:00.000",
        "Count": "3"
      },
      {
        "Month": "2020-09-01 00:00:00.000",
        "Count": "13"
      },
      {
        "Month": "2020-08-01 00:00:00.000",
        "Count": "29661"
      },
      {
        "Month": "2020-07-01 00:00:00.000",
        "Count": "20960"
      },
      {
        "Month": "2020-06-01 00:00:00.000",
        "Count": "24432"
      },
      {
        "Month": "2020-05-01 00:00:00.000",
        "Count": "31341"
      },
      {
        "Month": "2020-04-01 00:00:00.000",
        "Count": "1"
      },
      {
        "Month": "2020-03-01 00:00:00.000",
        "Count": "4"
      },
      {
        "Month": "2020-02-01 00:00:00.000",
        "Count": "4"
      },
      {
        "Month": "2020-01-01 00:00:00.000",
        "Count": "12"
      },
      {
        "Month": "2019-12-01 00:00:00.000",
        "Count": "1"
      }
    ],
    "ActiveProvider": "true"
  },
  {
    "Provider": "Rosepoint",
    "RecordCount": "1220847974",
    "PlatformCount": "324",
    "MinDateTime": "1601-01-01 00:00:00.000",
    "MaxDateTime": "2025-05-29 23:52:07.000",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "THREE RIVERS",
        "Count": "134817293",
        "FirstSubmission": "2019-08-27",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Genesis Patriot",
        "Count": "65151755",
        "FirstSubmission": "2021-06-17",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Anonymous",
        "Count": "60710001",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "MELVIN R.TODD",
        "Count": "46036737",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2023-08-25"
      },
      {
        "Platform": "POINT MALLARD",
        "Count": "43625124",
        "FirstSubmission": "2021-07-11",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "GENE NEAL",
        "Count": "41193638",
        "FirstSubmission": "2020-01-31",
        "LastSubmission": "2021-06-08"
      },
      {
        "Platform": "CAPT JERRY J.WILTZ",
        "Count": "37171264",
        "FirstSubmission": "2021-03-24",
        "LastSubmission": "2024-02-16"
      },
      {
        "Platform": "CIBOLO",
        "Count": "33374518",
        "FirstSubmission": "2019-02-16",
        "LastSubmission": "2021-05-19"
      },
      {
        "Platform": "DENNIS J PASENTINE",
        "Count": "31575308",
        "FirstSubmission": "2018-01-13",
        "LastSubmission": "2020-06-30"
      },
      {
        "Platform": "LOUIE LEONE",
        "Count": "29277658",
        "FirstSubmission": "2023-10-29",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "MV Dennis J Pasentine",
        "Count": "26296403",
        "FirstSubmission": "2023-08-04",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Miss Kathy",
        "Count": "25841010",
        "FirstSubmission": "2021-02-02",
        "LastSubmission": "2024-01-18"
      },
      {
        "Platform": "WALLER",
        "Count": "22513939",
        "FirstSubmission": "2021-03-09",
        "LastSubmission": "2021-12-14"
      },
      {
        "Platform": "the Colonel",
        "Count": "20851027",
        "FirstSubmission": "2023-09-07",
        "LastSubmission": "2025-02-11"
      },
      {
        "Platform": "Sempre Avanti",
        "Count": "19893826",
        "FirstSubmission": "2017-10-03",
        "LastSubmission": "2025-03-19"
      },
      {
        "Platform": "SERENITY",
        "Count": "17275636",
        "FirstSubmission": "2019-02-01",
        "LastSubmission": "2021-07-27"
      },
      {
        "Platform": "ATB GENESIS PATRIOT",
        "Count": "16343018",
        "FirstSubmission": "2020-03-07",
        "LastSubmission": "2021-03-20"
      },
      {
        "Platform": "CAPT. ELLIOT CROCHET",
        "Count": "14769284",
        "FirstSubmission": "2023-03-23",
        "LastSubmission": "2025-05-07"
      },
      {
        "Platform": "KATHY LYNN",
        "Count": "14595417",
        "FirstSubmission": "2020-06-09",
        "LastSubmission": "2021-07-16"
      },
      {
        "Platform": "LA FORCE",
        "Count": "14508081",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2021-10-16"
      },
      {
        "Platform": "TUG RANGER",
        "Count": "14405211",
        "FirstSubmission": "2022-02-26",
        "LastSubmission": "2024-08-12"
      },
      {
        "Platform": "Laperouse",
        "Count": "13966807",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2022-09-02"
      },
      {
        "Platform": "San Salvador",
        "Count": "12923279",
        "FirstSubmission": "2023-07-20",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Capt. Kirk Colletti",
        "Count": "12739614",
        "FirstSubmission": "2020-05-02",
        "LastSubmission": "2024-12-27"
      },
      {
        "Platform": "CAPT PETE",
        "Count": "12353807",
        "FirstSubmission": "2021-04-13",
        "LastSubmission": "2022-05-19"
      },
      {
        "Platform": "Whit Golding",
        "Count": "11047375",
        "FirstSubmission": "2024-06-05",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Dulce Vida",
        "Count": "10937204",
        "FirstSubmission": "2021-03-11",
        "LastSubmission": "2024-11-17"
      },
      {
        "Platform": "MV Grace Nicole",
        "Count": "10235378",
        "FirstSubmission": "2024-03-16",
        "LastSubmission": "2025-05-24"
      },
      {
        "Platform": "J THOMAS",
        "Count": "10211714",
        "FirstSubmission": "2023-03-10",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "MV Eric Livingston",
        "Count": "10163658",
        "FirstSubmission": "2024-05-01",
        "LastSubmission": "2025-05-12"
      },
      {
        "Platform": "NOAA Ship Pisces",
        "Count": "10158564",
        "FirstSubmission": "2023-03-17",
        "LastSubmission": "2025-04-15"
      },
      {
        "Platform": "MISS CYNTHIA",
        "Count": "10104421",
        "FirstSubmission": "2019-06-17",
        "LastSubmission": "2020-07-06"
      },
      {
        "Platform": "PAMLICO",
        "Count": "9913345",
        "FirstSubmission": "2022-11-26",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "SENATOR STENNIS",
        "Count": "9667495",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2018-08-18"
      },
      {
        "Platform": "MISSISSIPPI",
        "Count": "9133363",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2025-02-24"
      },
      {
        "Platform": "Point Comfort",
        "Count": "9119418",
        "FirstSubmission": "2023-08-26",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "RON HULL",
        "Count": "8943102",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2018-04-07"
      },
      {
        "Platform": "GREEN WING",
        "Count": "8571969",
        "FirstSubmission": "2024-05-24",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "SHANNON DANN",
        "Count": "8500978",
        "FirstSubmission": "2024-07-06",
        "LastSubmission": "2025-05-11"
      },
      {
        "Platform": "ALULAQ",
        "Count": "8028776",
        "FirstSubmission": "2019-11-21",
        "LastSubmission": "2024-04-09"
      },
      {
        "Platform": "BAYOU ST.JOHN",
        "Count": "8018512",
        "FirstSubmission": "2019-12-29",
        "LastSubmission": "2021-04-12"
      },
      {
        "Platform": "BAILEY",
        "Count": "7712253",
        "FirstSubmission": "2021-03-08",
        "LastSubmission": "2021-07-12"
      },
      {
        "Platform": "COOKE",
        "Count": "7274949",
        "FirstSubmission": "2019-11-04",
        "LastSubmission": "2021-04-06"
      },
      {
        "Platform": "R/V Bay Hydro II",
        "Count": "7023515",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2021-11-03"
      },
      {
        "Platform": "LCPL PHILLIP GEORGE",
        "Count": "7007816",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2018-06-26"
      },
      {
        "Platform": "BILL GARVEY",
        "Count": "6783595",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2019-05-22"
      },
      {
        "Platform": "Andy Mac",
        "Count": "6715435",
        "FirstSubmission": "2023-09-30",
        "LastSubmission": "2024-04-10"
      },
      {
        "Platform": "Clayton W. Moran",
        "Count": "6674559",
        "FirstSubmission": "2023-12-01",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "ROY MICHAEL",
        "Count": "6452050",
        "FirstSubmission": "2019-09-13",
        "LastSubmission": "2020-10-26"
      },
      {
        "Platform": "Tapestry",
        "Count": "6426646",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2022-05-16"
      },
      {
        "Platform": "Sea Crescent",
        "Count": "6247335",
        "FirstSubmission": "2024-08-26",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "CLARENCE NIXON",
        "Count": "6053671",
        "FirstSubmission": "2019-06-17",
        "LastSubmission": "2022-05-02"
      },
      {
        "Platform": "American Century",
        "Count": "5882125",
        "FirstSubmission": "2023-06-07",
        "LastSubmission": "2024-07-07"
      },
      {
        "Platform": "LOUISE NEWELL",
        "Count": "5813459",
        "FirstSubmission": "2024-05-31",
        "LastSubmission": "2025-05-25"
      },
      {
        "Platform": "san pedro",
        "Count": "5598786",
        "FirstSubmission": "2023-05-17",
        "LastSubmission": "2024-08-30"
      },
      {
        "Platform": "KAREN C",
        "Count": "5495069",
        "FirstSubmission": "2024-05-17",
        "LastSubmission": "2025-04-09"
      },
      {
        "Platform": "Nat Geo Quest",
        "Count": "4990625",
        "FirstSubmission": "2024-04-23",
        "LastSubmission": "2025-03-14"
      },
      {
        "Platform": "RUTH M. REINAUER",
        "Count": "4933002",
        "FirstSubmission": "2022-10-02",
        "LastSubmission": "2023-03-01"
      },
      {
        "Platform": "Skipjack",
        "Count": "4843575",
        "FirstSubmission": "2024-03-09",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Panache",
        "Count": "4584884",
        "FirstSubmission": "2020-07-26",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "ELIANA M GONDRAN",
        "Count": "4582033",
        "FirstSubmission": "2023-01-21",
        "LastSubmission": "2024-09-01"
      },
      {
        "Platform": "Silence Rising",
        "Count": "4563749",
        "FirstSubmission": "2018-03-29",
        "LastSubmission": "2021-05-28"
      },
      {
        "Platform": "JOHN T MCMAHAN",
        "Count": "4551917",
        "FirstSubmission": "2018-07-23",
        "LastSubmission": "2019-08-30"
      },
      {
        "Platform": "DIXIE VALOUR",
        "Count": "4530915",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2018-04-24"
      },
      {
        "Platform": "Douglas Murphy",
        "Count": "4363847",
        "FirstSubmission": "2024-02-16",
        "LastSubmission": "2024-10-10"
      },
      {
        "Platform": "MARGARET ANNE",
        "Count": "4249720",
        "FirstSubmission": "2019-10-06",
        "LastSubmission": "2019-12-30"
      },
      {
        "Platform": "Ren Chai",
        "Count": "4204253",
        "FirstSubmission": "2020-06-16",
        "LastSubmission": "2024-10-30"
      },
      {
        "Platform": "Blue Note",
        "Count": "4129186",
        "FirstSubmission": "2021-06-07",
        "LastSubmission": "2025-05-23"
      },
      {
        "Platform": "\"TM Diligence \"",
        "Count": "3887027",
        "FirstSubmission": "2023-11-21",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Infinity",
        "Count": "3616167",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2024-02-17"
      },
      {
        "Platform": "Mystic Dancer",
        "Count": "3580249",
        "FirstSubmission": "2019-05-17",
        "LastSubmission": "2024-01-06"
      },
      {
        "Platform": "Diane Moran",
        "Count": "3541581",
        "FirstSubmission": "2024-04-08",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "DODIE SIBEN",
        "Count": "3464177",
        "FirstSubmission": "2024-11-14",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "CHARLEVOIX",
        "Count": "3461296",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2024-08-10"
      },
      {
        "Platform": "NAT GEO Sea Bird",
        "Count": "3459799",
        "FirstSubmission": "2024-07-19",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "PANACHE",
        "Count": "3443680",
        "FirstSubmission": "2021-03-27",
        "LastSubmission": "2021-08-07"
      },
      {
        "Platform": "Susan J Gundlach",
        "Count": "3226613",
        "FirstSubmission": "2022-07-05",
        "LastSubmission": "2022-09-21"
      },
      {
        "Platform": "Thomas R Morrish",
        "Count": "3175036",
        "FirstSubmission": "2021-05-28",
        "LastSubmission": "2025-05-09"
      },
      {
        "Platform": "Tony&apos;s Place",
        "Count": "2648830",
        "FirstSubmission": "2020-12-29",
        "LastSubmission": "2022-02-19"
      },
      {
        "Platform": "MV Walter Blessey Jr",
        "Count": "2647868",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-04-26"
      },
      {
        "Platform": "THOMAS JEFFERSON",
        "Count": "2595639",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2018-02-26"
      },
      {
        "Platform": "Kathryn Louise",
        "Count": "2547542",
        "FirstSubmission": "2020-04-15",
        "LastSubmission": "2020-06-30"
      },
      {
        "Platform": "Sweet Ride",
        "Count": "2478692",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2019-03-11"
      },
      {
        "Platform": "Miss Sadie",
        "Count": "2440451",
        "FirstSubmission": "2024-12-04",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "SAILS",
        "Count": "2422330",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2024-10-12"
      },
      {
        "Platform": "Silver Bay",
        "Count": "2219499",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2025-05-26"
      },
      {
        "Platform": "MARTIN EXPLORER",
        "Count": "2181766",
        "FirstSubmission": "2025-01-02",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Explorer",
        "Count": "2176906",
        "FirstSubmission": "2018-06-01",
        "LastSubmission": "2021-01-03"
      },
      {
        "Platform": "Shiney V. Moran",
        "Count": "1896285",
        "FirstSubmission": "2025-01-02",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Atlas",
        "Count": "1887816",
        "FirstSubmission": "2024-07-22",
        "LastSubmission": "2025-01-09"
      },
      {
        "Platform": "NAUTILUS",
        "Count": "1769473",
        "FirstSubmission": "2018-05-09",
        "LastSubmission": "2024-09-06"
      },
      {
        "Platform": "NUECES",
        "Count": "1767687",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-08-14"
      },
      {
        "Platform": "DELTA",
        "Count": "1756596",
        "FirstSubmission": "2021-11-11",
        "LastSubmission": "2022-02-07"
      },
      {
        "Platform": "Sea &#32;Dweller",
        "Count": "1726359",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2018-07-17"
      },
      {
        "Platform": "GRAYSON",
        "Count": "1590294",
        "FirstSubmission": "2020-03-12",
        "LastSubmission": "2021-03-31"
      },
      {
        "Platform": "Calypso",
        "Count": "1485761",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2022-03-01"
      },
      {
        "Platform": "HarborLark",
        "Count": "1483441",
        "FirstSubmission": "2022-07-04",
        "LastSubmission": "2025-04-01"
      },
      {
        "Platform": "Pyxis",
        "Count": "1480375",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2024-10-11"
      },
      {
        "Platform": "Okeanos Explorer",
        "Count": "1464955",
        "FirstSubmission": "2021-05-15",
        "LastSubmission": "2023-06-17"
      },
      {
        "Platform": "kathryn louise",
        "Count": "1456546",
        "FirstSubmission": "2025-03-11",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Enemy Glory",
        "Count": "1416760",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2025-05-24"
      },
      {
        "Platform": "Off the Clock",
        "Count": "1406493",
        "FirstSubmission": "2019-12-06",
        "LastSubmission": "2021-12-22"
      },
      {
        "Platform": "Suzy Q 70 yds Poach 40 yds",
        "Count": "1362564",
        "FirstSubmission": "2018-04-21",
        "LastSubmission": "2021-09-21"
      },
      {
        "Platform": "Gray Eagle",
        "Count": "1357503",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2024-08-17"
      },
      {
        "Platform": "Nat Geo Sea Bird",
        "Count": "1341391",
        "FirstSubmission": "2022-10-20",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "FORT BRAGG",
        "Count": "1319147",
        "FirstSubmission": "2024-04-22",
        "LastSubmission": "2025-03-30"
      },
      {
        "Platform": "LAPEROUSE",
        "Count": "1245845",
        "FirstSubmission": "2017-04-25",
        "LastSubmission": "2019-07-11"
      },
      {
        "Platform": "Hank The Tank",
        "Count": "1234453",
        "FirstSubmission": "2018-12-16",
        "LastSubmission": "2025-01-30"
      },
      {
        "Platform": "Largo",
        "Count": "1216181",
        "FirstSubmission": "2024-02-29",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "SAM B",
        "Count": "1139527",
        "FirstSubmission": "2019-11-22",
        "LastSubmission": "2022-04-04"
      },
      {
        "Platform": "M/V Gambit",
        "Count": "1124446",
        "FirstSubmission": "2021-02-06",
        "LastSubmission": "2022-04-02"
      },
      {
        "Platform": "Evergreen",
        "Count": "1104066",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2018-08-10"
      },
      {
        "Platform": "Vega",
        "Count": "1098224",
        "FirstSubmission": "2021-10-06",
        "LastSubmission": "2024-07-04"
      },
      {
        "Platform": "EXPLORER",
        "Count": "1090873",
        "FirstSubmission": "2025-02-03",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Prestissimo",
        "Count": "1072771",
        "FirstSubmission": "2017-09-19",
        "LastSubmission": "2024-06-22"
      },
      {
        "Platform": "Weston Merrit",
        "Count": "1067718",
        "FirstSubmission": "2021-09-02",
        "LastSubmission": "2024-09-13"
      },
      {
        "Platform": "Caper",
        "Count": "1064070",
        "FirstSubmission": "2020-05-06",
        "LastSubmission": "2020-11-17"
      },
      {
        "Platform": "Atlantic Power",
        "Count": "1051776",
        "FirstSubmission": "2024-10-19",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Sea Dweller",
        "Count": "1026176",
        "FirstSubmission": "2017-08-09",
        "LastSubmission": "2019-12-26"
      },
      {
        "Platform": "St. Dominick",
        "Count": "1015865",
        "FirstSubmission": "2017-08-25",
        "LastSubmission": "2022-09-10"
      },
      {
        "Platform": "Melissa Lynn",
        "Count": "983060",
        "FirstSubmission": "2023-05-24",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "MV Margrete Anne",
        "Count": "972700",
        "FirstSubmission": "2019-12-31",
        "LastSubmission": "2020-02-01"
      },
      {
        "Platform": "Pacific Blue",
        "Count": "971217",
        "FirstSubmission": "2022-10-16",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Jenny",
        "Count": "967703",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2019-02-09"
      },
      {
        "Platform": "Breakaway",
        "Count": "916707",
        "FirstSubmission": "2017-06-02",
        "LastSubmission": "2024-12-03"
      },
      {
        "Platform": "SAINT CHARLES",
        "Count": "894410",
        "FirstSubmission": "2022-03-17",
        "LastSubmission": "2022-06-01"
      },
      {
        "Platform": "SATORI",
        "Count": "841846",
        "FirstSubmission": "2023-06-06",
        "LastSubmission": "2024-10-23"
      },
      {
        "Platform": "NOAA Ship Thomas Jefferson",
        "Count": "780118",
        "FirstSubmission": "2018-07-06",
        "LastSubmission": "2021-07-01"
      },
      {
        "Platform": "Pacific Link",
        "Count": "767399",
        "FirstSubmission": "2017-05-10",
        "LastSubmission": "2018-07-08"
      },
      {
        "Platform": "Ibis",
        "Count": "750239",
        "FirstSubmission": "2017-08-12",
        "LastSubmission": "2022-09-08"
      },
      {
        "Platform": "Timbalier Bay",
        "Count": "694678",
        "FirstSubmission": "2024-05-18",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "MV Judith Ellen",
        "Count": "685178",
        "FirstSubmission": "2023-08-04",
        "LastSubmission": "2023-09-09"
      },
      {
        "Platform": "OLIVER SHEARER",
        "Count": "672578",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2018-01-12"
      },
      {
        "Platform": "RV ZEPHYR",
        "Count": "641727",
        "FirstSubmission": "2021-05-15",
        "LastSubmission": "2022-01-04"
      },
      {
        "Platform": "Spirit Bear",
        "Count": "633517",
        "FirstSubmission": "2022-06-12",
        "LastSubmission": "2024-12-16"
      },
      {
        "Platform": "MV Renee T Whatley",
        "Count": "604847",
        "FirstSubmission": "2024-08-12",
        "LastSubmission": "2024-09-23"
      },
      {
        "Platform": "THOMAS R MORRISH",
        "Count": "592983",
        "FirstSubmission": "2019-09-24",
        "LastSubmission": "2021-04-21"
      },
      {
        "Platform": "HIAQUA",
        "Count": "589898",
        "FirstSubmission": "2019-04-11",
        "LastSubmission": "2024-04-18"
      },
      {
        "Platform": "REX DOBSON",
        "Count": "538155",
        "FirstSubmission": "2019-11-05",
        "LastSubmission": "2020-04-16"
      },
      {
        "Platform": "Marie Louise II",
        "Count": "535196",
        "FirstSubmission": "2018-07-03",
        "LastSubmission": "2024-09-11"
      },
      {
        "Platform": "Helen A",
        "Count": "531086",
        "FirstSubmission": "2022-05-21",
        "LastSubmission": "2023-11-20"
      },
      {
        "Platform": "MV David Goin",
        "Count": "514557",
        "FirstSubmission": "2025-05-23",
        "LastSubmission": "2025-05-26"
      },
      {
        "Platform": "Copper Star",
        "Count": "474928",
        "FirstSubmission": "2019-02-22",
        "LastSubmission": "2024-05-30"
      },
      {
        "Platform": "Tugaway",
        "Count": "472024",
        "FirstSubmission": "2024-05-03",
        "LastSubmission": "2025-04-26"
      },
      {
        "Platform": "Eloisa",
        "Count": "453187",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2020-11-20"
      },
      {
        "Platform": "R5503",
        "Count": "440775",
        "FirstSubmission": "2024-07-16",
        "LastSubmission": "2025-05-07"
      },
      {
        "Platform": "Lay Time",
        "Count": "423584",
        "FirstSubmission": "2019-03-01",
        "LastSubmission": "2024-07-07"
      },
      {
        "Platform": "Ariel",
        "Count": "415122",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2022-07-06"
      },
      {
        "Platform": "BUNKER KING",
        "Count": "409405",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2018-01-05"
      },
      {
        "Platform": "New Freedom",
        "Count": "390514",
        "FirstSubmission": "2022-07-12",
        "LastSubmission": "2024-10-01"
      },
      {
        "Platform": "PATRIARCH",
        "Count": "362958",
        "FirstSubmission": "2020-01-14",
        "LastSubmission": "2021-12-09"
      },
      {
        "Platform": "SPIRIT",
        "Count": "346269",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-11-01"
      },
      {
        "Platform": "Seaborne",
        "Count": "339828",
        "FirstSubmission": "2018-05-25",
        "LastSubmission": "2020-10-27"
      },
      {
        "Platform": "Tug Allie B",
        "Count": "339693",
        "FirstSubmission": "2025-03-27",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "Thomas Jefferson",
        "Count": "335534",
        "FirstSubmission": "2018-05-18",
        "LastSubmission": "2018-05-27"
      },
      {
        "Platform": "Senator Sennis",
        "Count": "318290",
        "FirstSubmission": "2018-12-18",
        "LastSubmission": "2018-12-22"
      },
      {
        "Platform": "Andiamo",
        "Count": "314463",
        "FirstSubmission": "2021-07-21",
        "LastSubmission": "2023-05-22"
      },
      {
        "Platform": "MV Dale Artigue",
        "Count": "293323",
        "FirstSubmission": "2023-06-13",
        "LastSubmission": "2023-06-19"
      },
      {
        "Platform": "Figment",
        "Count": "289170",
        "FirstSubmission": "2017-09-04",
        "LastSubmission": "2025-01-23"
      },
      {
        "Platform": "Copper Coin",
        "Count": "289122",
        "FirstSubmission": "2023-03-27",
        "LastSubmission": "2025-04-13"
      },
      {
        "Platform": "Kainoa",
        "Count": "267784",
        "FirstSubmission": "2021-05-16",
        "LastSubmission": "2024-06-13"
      },
      {
        "Platform": "ALVA DUPRE",
        "Count": "267435",
        "FirstSubmission": "2017-12-24",
        "LastSubmission": "2018-02-08"
      },
      {
        "Platform": "M/V Tempo",
        "Count": "266419",
        "FirstSubmission": "2022-06-14",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "NOAA Ship Fairweather",
        "Count": "263220",
        "FirstSubmission": "2018-05-12",
        "LastSubmission": "2018-08-01"
      },
      {
        "Platform": "ZORA NEALE",
        "Count": "244153",
        "FirstSubmission": "2022-11-12",
        "LastSubmission": "2023-04-12"
      },
      {
        "Platform": "\"Pacific Time \"",
        "Count": "238118",
        "FirstSubmission": "2017-06-16",
        "LastSubmission": "2025-01-19"
      },
      {
        "Platform": "Temptation",
        "Count": "236830",
        "FirstSubmission": "2017-10-12",
        "LastSubmission": "2021-07-03"
      },
      {
        "Platform": "Escort",
        "Count": "233724",
        "FirstSubmission": "2021-06-13",
        "LastSubmission": "2024-07-08"
      },
      {
        "Platform": "Great Escape",
        "Count": "229604",
        "FirstSubmission": "2022-02-25",
        "LastSubmission": "2023-05-11"
      },
      {
        "Platform": "Tootega",
        "Count": "219099",
        "FirstSubmission": "2018-07-20",
        "LastSubmission": "2020-09-24"
      },
      {
        "Platform": "Magnolia",
        "Count": "207337",
        "FirstSubmission": "2018-12-23",
        "LastSubmission": "2020-01-05"
      },
      {
        "Platform": "Journey",
        "Count": "200802",
        "FirstSubmission": "2023-06-06",
        "LastSubmission": "2024-10-09"
      },
      {
        "Platform": "Slow Dancing",
        "Count": "177849",
        "FirstSubmission": "2023-06-17",
        "LastSubmission": "2025-03-02"
      },
      {
        "Platform": "Toscana",
        "Count": "175314",
        "FirstSubmission": "2021-12-27",
        "LastSubmission": "2025-05-23"
      },
      {
        "Platform": "S/V Aphrodite",
        "Count": "174035",
        "FirstSubmission": "2017-06-18",
        "LastSubmission": "2017-11-22"
      },
      {
        "Platform": "Kestrel",
        "Count": "172489",
        "FirstSubmission": "2018-05-19",
        "LastSubmission": "2025-01-12"
      },
      {
        "Platform": "BELLE AMIE",
        "Count": "167506",
        "FirstSubmission": "2019-01-28",
        "LastSubmission": "2022-06-27"
      },
      {
        "Platform": "Lagniappe",
        "Count": "162992",
        "FirstSubmission": "2024-05-25",
        "LastSubmission": "2025-05-26"
      },
      {
        "Platform": "Terry Bordelon",
        "Count": "162118",
        "FirstSubmission": "2025-01-02",
        "LastSubmission": "2025-04-28"
      },
      {
        "Platform": "Sentosa",
        "Count": "160417",
        "FirstSubmission": "2017-06-24",
        "LastSubmission": "2019-08-02"
      },
      {
        "Platform": "Sea Saga",
        "Count": "157596",
        "FirstSubmission": "2020-08-12",
        "LastSubmission": "2020-08-31"
      },
      {
        "Platform": "Tonic",
        "Count": "150091",
        "FirstSubmission": "2020-05-09",
        "LastSubmission": "2024-11-11"
      },
      {
        "Platform": "F/V Mirage",
        "Count": "146811",
        "FirstSubmission": "2017-08-08",
        "LastSubmission": "2017-10-02"
      },
      {
        "Platform": "THOR",
        "Count": "146500",
        "FirstSubmission": "2023-04-21",
        "LastSubmission": "2025-02-18"
      },
      {
        "Platform": "Belle La Vie",
        "Count": "145602",
        "FirstSubmission": "2024-04-15",
        "LastSubmission": "2025-04-09"
      },
      {
        "Platform": "ROBERT ANTHONY",
        "Count": "141843",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-04-26"
      },
      {
        "Platform": "Hot Tomolly",
        "Count": "139704",
        "FirstSubmission": "2017-07-12",
        "LastSubmission": "2020-09-22"
      },
      {
        "Platform": "Abeona",
        "Count": "132497",
        "FirstSubmission": "2022-04-11",
        "LastSubmission": "2022-04-28"
      },
      {
        "Platform": "NOAA Ship FAIRWEATHER",
        "Count": "130410",
        "FirstSubmission": "2020-12-01",
        "LastSubmission": "2021-03-06"
      },
      {
        "Platform": "ROARING POINT",
        "Count": "121068",
        "FirstSubmission": "2025-04-17",
        "LastSubmission": "2025-04-30"
      },
      {
        "Platform": "roadrunner",
        "Count": "113866",
        "FirstSubmission": "2025-02-22",
        "LastSubmission": "2025-02-22"
      },
      {
        "Platform": "FREEDOM",
        "Count": "113234",
        "FirstSubmission": "2024-08-26",
        "LastSubmission": "2025-03-04"
      },
      {
        "Platform": "Endless Summer",
        "Count": "109169",
        "FirstSubmission": "2022-05-14",
        "LastSubmission": "2024-12-16"
      },
      {
        "Platform": "Hiaqua",
        "Count": "108461",
        "FirstSubmission": "2017-06-26",
        "LastSubmission": "2019-03-10"
      },
      {
        "Platform": "tadhana",
        "Count": "106159",
        "FirstSubmission": "2019-12-03",
        "LastSubmission": "2021-04-12"
      },
      {
        "Platform": "Tiger Beetle",
        "Count": "99453",
        "FirstSubmission": "2024-11-15",
        "LastSubmission": "2024-11-25"
      },
      {
        "Platform": "Loose Wire",
        "Count": "98576",
        "FirstSubmission": "2017-07-09",
        "LastSubmission": "2020-08-24"
      },
      {
        "Platform": "Kairos",
        "Count": "98572",
        "FirstSubmission": "2017-08-08",
        "LastSubmission": "2020-07-31"
      },
      {
        "Platform": "S/V Alaska Girl",
        "Count": "93015",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2019-06-13"
      },
      {
        "Platform": "F/V Toronado",
        "Count": "89190",
        "FirstSubmission": "2019-09-12",
        "LastSubmission": "2019-09-12"
      },
      {
        "Platform": "O Sea D",
        "Count": "87590",
        "FirstSubmission": "2018-07-25",
        "LastSubmission": "2019-07-14"
      },
      {
        "Platform": "Dale Lindsey",
        "Count": "85589",
        "FirstSubmission": "2025-04-15",
        "LastSubmission": "2025-05-11"
      },
      {
        "Platform": "Robin Marie",
        "Count": "84389",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-09-18"
      },
      {
        "Platform": "Ondine",
        "Count": "82680",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2020-04-20"
      },
      {
        "Platform": "Change N Course",
        "Count": "76402",
        "FirstSubmission": "2018-06-16",
        "LastSubmission": "2024-08-28"
      },
      {
        "Platform": "Southern Grace",
        "Count": "74709",
        "FirstSubmission": "2019-03-27",
        "LastSubmission": "2021-11-02"
      },
      {
        "Platform": "Lil&apos; David",
        "Count": "73705",
        "FirstSubmission": "2024-01-11",
        "LastSubmission": "2025-02-02"
      },
      {
        "Platform": "Tardis Two",
        "Count": "70384",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-07-31"
      },
      {
        "Platform": "Paragon",
        "Count": "69663",
        "FirstSubmission": "2021-08-13",
        "LastSubmission": "2023-10-01"
      },
      {
        "Platform": "Windependence",
        "Count": "68165",
        "FirstSubmission": "2025-02-18",
        "LastSubmission": "2025-04-03"
      },
      {
        "Platform": "thomas jefferson",
        "Count": "63068",
        "FirstSubmission": "2025-05-24",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Fairweather",
        "Count": "60631",
        "FirstSubmission": "2017-06-01",
        "LastSubmission": "2017-07-12"
      },
      {
        "Platform": "M.Y. Bluewater",
        "Count": "57847",
        "FirstSubmission": "2022-06-29",
        "LastSubmission": "2023-05-08"
      },
      {
        "Platform": "Diversion",
        "Count": "56248",
        "FirstSubmission": "2018-01-13",
        "LastSubmission": "2018-08-19"
      },
      {
        "Platform": "Zephyr",
        "Count": "56196",
        "FirstSubmission": "2017-05-30",
        "LastSubmission": "2018-07-09"
      },
      {
        "Platform": "MISS MARLEY",
        "Count": "49536",
        "FirstSubmission": "2025-05-29",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "inQuest",
        "Count": "47043",
        "FirstSubmission": "2021-07-21",
        "LastSubmission": "2021-07-21"
      },
      {
        "Platform": "Endeavor",
        "Count": "43633",
        "FirstSubmission": "2019-01-30",
        "LastSubmission": "2019-06-30"
      },
      {
        "Platform": "Mystic Dance",
        "Count": "41939",
        "FirstSubmission": "2018-08-11",
        "LastSubmission": "2018-12-18"
      },
      {
        "Platform": "Mama C",
        "Count": "40514",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2018-07-12"
      },
      {
        "Platform": "Valdez Spirit",
        "Count": "40060",
        "FirstSubmission": "2023-07-04",
        "LastSubmission": "2023-07-11"
      },
      {
        "Platform": "Waves Of Grace",
        "Count": "38256",
        "FirstSubmission": "2019-03-28",
        "LastSubmission": "2019-03-28"
      },
      {
        "Platform": "Sea Dragon",
        "Count": "38118",
        "FirstSubmission": "2017-07-04",
        "LastSubmission": "2017-08-07"
      },
      {
        "Platform": "Alliance",
        "Count": "35617",
        "FirstSubmission": "2025-05-24",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "CODA",
        "Count": "31342",
        "FirstSubmission": "2024-01-08",
        "LastSubmission": "2025-05-24"
      },
      {
        "Platform": "Freedom",
        "Count": "30066",
        "FirstSubmission": "2025-05-23",
        "LastSubmission": "2025-05-28"
      },
      {
        "Platform": "Jaunu",
        "Count": "29626",
        "FirstSubmission": "2017-05-06",
        "LastSubmission": "2020-07-12"
      },
      {
        "Platform": "Kaibeto",
        "Count": "28013",
        "FirstSubmission": "2019-04-12",
        "LastSubmission": "2021-04-15"
      },
      {
        "Platform": "One With The Wibd",
        "Count": "27084",
        "FirstSubmission": "2019-10-10",
        "LastSubmission": "2019-10-14"
      },
      {
        "Platform": "MOLLY R MCCALL",
        "Count": "25728",
        "FirstSubmission": "2017-09-21",
        "LastSubmission": "2017-10-31"
      },
      {
        "Platform": "M/V Gizmo",
        "Count": "25618",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-09-28"
      },
      {
        "Platform": "Capaz",
        "Count": "24435",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-06-27"
      },
      {
        "Platform": "Robin Shelton",
        "Count": "24304",
        "FirstSubmission": "2024-06-08",
        "LastSubmission": "2024-06-09"
      },
      {
        "Platform": "FreeWill",
        "Count": "23672",
        "FirstSubmission": "2025-01-23",
        "LastSubmission": "2025-04-05"
      },
      {
        "Platform": "CREOLA",
        "Count": "23267",
        "FirstSubmission": "2020-07-13",
        "LastSubmission": "2021-10-07"
      },
      {
        "Platform": "NOAA SHip Fairweather",
        "Count": "21934",
        "FirstSubmission": "2018-08-04",
        "LastSubmission": "2018-08-04"
      },
      {
        "Platform": "Jack Odom",
        "Count": "21816",
        "FirstSubmission": "2020-01-15",
        "LastSubmission": "2020-06-05"
      },
      {
        "Platform": "MONDREAL",
        "Count": "19250",
        "FirstSubmission": "2019-06-29",
        "LastSubmission": "2019-06-29"
      },
      {
        "Platform": "Rockhopper",
        "Count": "18048",
        "FirstSubmission": "2018-04-08",
        "LastSubmission": "2019-08-27"
      },
      {
        "Platform": "ODYSSEA",
        "Count": "16769",
        "FirstSubmission": "2019-06-11",
        "LastSubmission": "2022-06-18"
      },
      {
        "Platform": "R/V Bay Commitment",
        "Count": "14393",
        "FirstSubmission": "2024-12-27",
        "LastSubmission": "2025-04-09"
      },
      {
        "Platform": "Aurora",
        "Count": "12630",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2022-06-11"
      },
      {
        "Platform": "TM",
        "Count": "12126",
        "FirstSubmission": "2021-05-05",
        "LastSubmission": "2023-06-29"
      },
      {
        "Platform": "Evening Song",
        "Count": "12036",
        "FirstSubmission": "2020-07-07",
        "LastSubmission": "2020-08-03"
      },
      {
        "Platform": "Rendezvous",
        "Count": "8077",
        "FirstSubmission": "2018-12-25",
        "LastSubmission": "2023-09-08"
      },
      {
        "Platform": "FOO BARGE",
        "Count": "8068",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-04-26"
      },
      {
        "Platform": "Spinner",
        "Count": "7640",
        "FirstSubmission": "2020-03-16",
        "LastSubmission": "2024-07-15"
      },
      {
        "Platform": "Kokomo",
        "Count": "7576",
        "FirstSubmission": "2024-06-22",
        "LastSubmission": "2025-01-28"
      },
      {
        "Platform": "Adagio",
        "Count": "7293",
        "FirstSubmission": "2018-05-27",
        "LastSubmission": "2018-05-27"
      },
      {
        "Platform": "MV Pyxis",
        "Count": "7019",
        "FirstSubmission": "2025-01-17",
        "LastSubmission": "2025-04-24"
      },
      {
        "Platform": "Anejo",
        "Count": "5456",
        "FirstSubmission": "2023-07-19",
        "LastSubmission": "2023-07-22"
      },
      {
        "Platform": "FREGATA",
        "Count": "4968",
        "FirstSubmission": "2023-02-06",
        "LastSubmission": "2023-04-30"
      },
      {
        "Platform": "Suzy Q 95 yds Poach 40 yds",
        "Count": "4507",
        "FirstSubmission": "2021-10-02",
        "LastSubmission": "2021-10-02"
      },
      {
        "Platform": "joe pyne",
        "Count": "4214",
        "FirstSubmission": "2021-08-23",
        "LastSubmission": "2021-08-23"
      },
      {
        "Platform": "Simplicity",
        "Count": "3992",
        "FirstSubmission": "2019-07-21",
        "LastSubmission": "2019-09-29"
      },
      {
        "Platform": "Windswept",
        "Count": "3928",
        "FirstSubmission": "2017-12-05",
        "LastSubmission": "2019-02-27"
      },
      {
        "Platform": "YWAM PNG",
        "Count": "3548",
        "FirstSubmission": "2019-04-08",
        "LastSubmission": "2019-04-08"
      },
      {
        "Platform": "JOE PYNE",
        "Count": "3166",
        "FirstSubmission": "2020-06-18",
        "LastSubmission": "2020-06-18"
      },
      {
        "Platform": "True North",
        "Count": "2649",
        "FirstSubmission": "2020-09-27",
        "LastSubmission": "2020-09-27"
      },
      {
        "Platform": "MISSION",
        "Count": "2451",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2020-08-10"
      },
      {
        "Platform": "MV Karen Pape",
        "Count": "2328",
        "FirstSubmission": "2020-07-31",
        "LastSubmission": "2020-07-31"
      },
      {
        "Platform": "CAPT.REGGIE LEBOEUF",
        "Count": "2318",
        "FirstSubmission": "2020-06-30",
        "LastSubmission": "2020-08-11"
      },
      {
        "Platform": "Maverick",
        "Count": "2040",
        "FirstSubmission": "2018-12-16",
        "LastSubmission": "2018-12-16"
      },
      {
        "Platform": "COPPER STAR",
        "Count": "1908",
        "FirstSubmission": "2020-10-03",
        "LastSubmission": "2024-04-18"
      },
      {
        "Platform": "Capt. Troy Green",
        "Count": "1753",
        "FirstSubmission": "2020-12-24",
        "LastSubmission": "2020-12-24"
      },
      {
        "Platform": "S/V Twist",
        "Count": "1740",
        "FirstSubmission": "2020-06-06",
        "LastSubmission": "2022-12-17"
      },
      {
        "Platform": "Seattle",
        "Count": "1582",
        "FirstSubmission": "2019-09-17",
        "LastSubmission": "2019-09-17"
      },
      {
        "Platform": "Easy Living",
        "Count": "1573",
        "FirstSubmission": "2017-06-11",
        "LastSubmission": "2021-02-24"
      },
      {
        "Platform": "HALLELUJAH!",
        "Count": "1473",
        "FirstSubmission": "2019-03-31",
        "LastSubmission": "2019-04-06"
      },
      {
        "Platform": "ASPEN",
        "Count": "1361",
        "FirstSubmission": "2023-12-12",
        "LastSubmission": "2023-12-12"
      },
      {
        "Platform": "Coda",
        "Count": "1258",
        "FirstSubmission": "2024-12-20",
        "LastSubmission": "2025-03-12"
      },
      {
        "Platform": "Serenity",
        "Count": "1077",
        "FirstSubmission": "2018-08-10",
        "LastSubmission": "2019-06-20"
      },
      {
        "Platform": "Rock n Ocean",
        "Count": "1020",
        "FirstSubmission": "2020-08-30",
        "LastSubmission": "2022-06-04"
      },
      {
        "Platform": "M.Y. Bluewater V",
        "Count": "967",
        "FirstSubmission": "2023-06-21",
        "LastSubmission": "2023-06-28"
      },
      {
        "Platform": "Urania",
        "Count": "947",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-04-26"
      },
      {
        "Platform": "Hal Pannell",
        "Count": "877",
        "FirstSubmission": "2017-10-20",
        "LastSubmission": "2017-10-20"
      },
      {
        "Platform": "Windswift",
        "Count": "833",
        "FirstSubmission": "2022-09-23",
        "LastSubmission": "2023-07-25"
      },
      {
        "Platform": "Independence",
        "Count": "729",
        "FirstSubmission": "2021-06-03",
        "LastSubmission": "2021-09-18"
      },
      {
        "Platform": "NICKIE B",
        "Count": "665",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-04-26"
      },
      {
        "Platform": "SANWAN",
        "Count": "545",
        "FirstSubmission": "2022-06-07",
        "LastSubmission": "2022-06-07"
      },
      {
        "Platform": "WILD BLUE",
        "Count": "510",
        "FirstSubmission": "2024-08-29",
        "LastSubmission": "2024-09-17"
      },
      {
        "Platform": "Kaos",
        "Count": "479",
        "FirstSubmission": "2023-09-08",
        "LastSubmission": "2024-02-23"
      },
      {
        "Platform": "Hank the Tank",
        "Count": "456",
        "FirstSubmission": "2023-03-18",
        "LastSubmission": "2025-01-11"
      },
      {
        "Platform": "Nettie Rose",
        "Count": "389",
        "FirstSubmission": "2017-07-08",
        "LastSubmission": "2018-06-10"
      },
      {
        "Platform": "ARCHIE WILSON",
        "Count": "342",
        "FirstSubmission": "2020-04-17",
        "LastSubmission": "2020-04-17"
      },
      {
        "Platform": "R/V Questuary",
        "Count": "312",
        "FirstSubmission": "2018-02-01",
        "LastSubmission": "2018-05-04"
      },
      {
        "Platform": "White Trash",
        "Count": "283",
        "FirstSubmission": "2021-03-28",
        "LastSubmission": "2021-09-25"
      },
      {
        "Platform": "Papa",
        "Count": "251",
        "FirstSubmission": "2018-06-23",
        "LastSubmission": "2019-05-25"
      },
      {
        "Platform": "ANNIE O&apos;SHEA",
        "Count": "226",
        "FirstSubmission": "2024-06-28",
        "LastSubmission": "2024-12-31"
      },
      {
        "Platform": "Joe Pyne",
        "Count": "196",
        "FirstSubmission": "2019-06-26",
        "LastSubmission": "2020-06-18"
      },
      {
        "Platform": "Kaiako",
        "Count": "178",
        "FirstSubmission": "2018-06-09",
        "LastSubmission": "2018-06-09"
      },
      {
        "Platform": "Halcyon",
        "Count": "110",
        "FirstSubmission": "2017-07-30",
        "LastSubmission": "2017-12-26"
      },
      {
        "Platform": "Mantra",
        "Count": "106",
        "FirstSubmission": "2025-05-27",
        "LastSubmission": "2025-05-29"
      },
      {
        "Platform": "ALASKAN EXPLORER",
        "Count": "93",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-04-26"
      },
      {
        "Platform": "Bella Rosa",
        "Count": "84",
        "FirstSubmission": "2024-11-13",
        "LastSubmission": "2024-11-13"
      },
      {
        "Platform": "LivLife",
        "Count": "84",
        "FirstSubmission": "2024-06-25",
        "LastSubmission": "2024-07-17"
      },
      {
        "Platform": "FRANK JAHN",
        "Count": "76",
        "FirstSubmission": "2021-11-30",
        "LastSubmission": "2021-11-30"
      },
      {
        "Platform": "TANGLEWOOD",
        "Count": "72",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-04-26"
      },
      {
        "Platform": "WENDY L",
        "Count": "72",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2018-01-18"
      },
      {
        "Platform": "Angel&apos;s Pearl",
        "Count": "58",
        "FirstSubmission": "2020-09-15",
        "LastSubmission": "2020-09-27"
      },
      {
        "Platform": "mission",
        "Count": "44",
        "FirstSubmission": "2018-08-20",
        "LastSubmission": "2018-08-20"
      },
      {
        "Platform": "Makana Kai",
        "Count": "41",
        "FirstSubmission": "2023-05-11",
        "LastSubmission": "2023-05-11"
      },
      {
        "Platform": "Sea La Vie",
        "Count": "36",
        "FirstSubmission": "2024-12-26",
        "LastSubmission": "2025-05-24"
      },
      {
        "Platform": "Bear Hunter",
        "Count": "36",
        "FirstSubmission": "2017-08-12",
        "LastSubmission": "2017-08-12"
      },
      {
        "Platform": "Seven Tenths",
        "Count": "32",
        "FirstSubmission": "2017-06-16",
        "LastSubmission": "2017-06-16"
      },
      {
        "Platform": "ondine",
        "Count": "29",
        "FirstSubmission": "2019-08-07",
        "LastSubmission": "2019-08-07"
      },
      {
        "Platform": "MV Don Carlton",
        "Count": "28",
        "FirstSubmission": "2021-12-20",
        "LastSubmission": "2021-12-20"
      },
      {
        "Platform": "Caroline Frances",
        "Count": "26",
        "FirstSubmission": "2024-07-27",
        "LastSubmission": "2024-07-27"
      },
      {
        "Platform": "ATHENA",
        "Count": "20",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-04-26"
      },
      {
        "Platform": "Glacier Spirit",
        "Count": "13",
        "FirstSubmission": "2024-05-23",
        "LastSubmission": "2024-05-23"
      },
      {
        "Platform": "IKAN TAMBAN",
        "Count": "12",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-04-26"
      },
      {
        "Platform": "Galactic",
        "Count": "12",
        "FirstSubmission": "2018-02-14",
        "LastSubmission": "2018-02-15"
      },
      {
        "Platform": "RAISINS",
        "Count": "9",
        "FirstSubmission": "2017-04-26",
        "LastSubmission": "2017-04-26"
      },
      {
        "Platform": "STBL",
        "Count": "8",
        "FirstSubmission": "2020-09-17",
        "LastSubmission": "2020-09-17"
      },
      {
        "Platform": "Mantra of Glasgow",
        "Count": "7",
        "FirstSubmission": "2022-05-04",
        "LastSubmission": "2022-05-04"
      },
      {
        "Platform": "Crowdsourcing_PC2",
        "Count": "7",
        "FirstSubmission": "2017-08-29",
        "LastSubmission": "2017-08-29"
      },
      {
        "Platform": "SEEKER",
        "Count": "6",
        "FirstSubmission": "2017-08-08",
        "LastSubmission": "2017-08-08"
      },
      {
        "Platform": "TEST",
        "Count": "4",
        "FirstSubmission": "2018-04-25",
        "LastSubmission": "2018-04-25"
      },
      {
        "Platform": "Tadhana",
        "Count": "4",
        "FirstSubmission": "2019-11-05",
        "LastSubmission": "2019-11-05"
      },
      {
        "Platform": "Noeta",
        "Count": "2",
        "FirstSubmission": "2018-05-24",
        "LastSubmission": "2018-05-24"
      },
      {
        "Platform": "OTTO",
        "Count": "2",
        "FirstSubmission": "2024-05-09",
        "LastSubmission": "2024-05-09"
      },
      {
        "Platform": "ANNIE O SHEA",
        "Count": "1",
        "FirstSubmission": "2024-06-16",
        "LastSubmission": "2024-06-16"
      },
      {
        "Platform": "MISS CAROLINE",
        "Count": "1",
        "FirstSubmission": "2019-06-07",
        "LastSubmission": "2019-06-07"
      },
      {
        "Platform": "TRIDENT",
        "Count": "1",
        "FirstSubmission": "2021-02-25",
        "LastSubmission": "2021-02-25"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2025-05-01 00:00:00.000",
        "Count": "11352098"
      },
      {
        "Month": "2025-04-01 00:00:00.000",
        "Count": "15474270"
      },
      {
        "Month": "2025-03-01 00:00:00.000",
        "Count": "18833282"
      },
      {
        "Month": "2025-02-01 00:00:00.000",
        "Count": "14755872"
      },
      {
        "Month": "2025-01-01 00:00:00.000",
        "Count": "18501801"
      },
      {
        "Month": "2024-12-01 00:00:00.000",
        "Count": "16673285"
      },
      {
        "Month": "2024-11-01 00:00:00.000",
        "Count": "16944816"
      },
      {
        "Month": "2024-10-01 00:00:00.000",
        "Count": "17497454"
      },
      {
        "Month": "2024-09-01 00:00:00.000",
        "Count": "15635577"
      },
      {
        "Month": "2024-08-01 00:00:00.000",
        "Count": "18032658"
      },
      {
        "Month": "2024-07-01 00:00:00.000",
        "Count": "18734691"
      },
      {
        "Month": "2024-06-01 00:00:00.000",
        "Count": "19189718"
      },
      {
        "Month": "2024-05-01 00:00:00.000",
        "Count": "16113206"
      },
      {
        "Month": "2024-04-01 00:00:00.000",
        "Count": "14243539"
      },
      {
        "Month": "2024-03-01 00:00:00.000",
        "Count": "15193090"
      },
      {
        "Month": "2024-02-01 00:00:00.000",
        "Count": "10537377"
      },
      {
        "Month": "2024-01-01 00:00:00.000",
        "Count": "7668504"
      },
      {
        "Month": "2023-12-01 00:00:00.000",
        "Count": "10428074"
      },
      {
        "Month": "2023-11-01 00:00:00.000",
        "Count": "11450854"
      },
      {
        "Month": "2023-10-01 00:00:00.000",
        "Count": "12198907"
      },
      {
        "Month": "2023-09-01 00:00:00.000",
        "Count": "11681949"
      },
      {
        "Month": "2023-08-01 00:00:00.000",
        "Count": "9122287"
      },
      {
        "Month": "2023-07-01 00:00:00.000",
        "Count": "9346999"
      },
      {
        "Month": "2023-06-01 00:00:00.000",
        "Count": "7257206"
      },
      {
        "Month": "2023-05-01 00:00:00.000",
        "Count": "6679185"
      },
      {
        "Month": "2023-04-01 00:00:00.000",
        "Count": "6544072"
      },
      {
        "Month": "2023-03-01 00:00:00.000",
        "Count": "5766541"
      },
      {
        "Month": "2023-02-01 00:00:00.000",
        "Count": "4057916"
      },
      {
        "Month": "2023-01-01 00:00:00.000",
        "Count": "4538618"
      },
      {
        "Month": "2022-12-01 00:00:00.000",
        "Count": "3938798"
      },
      {
        "Month": "2022-11-01 00:00:00.000",
        "Count": "4727654"
      },
      {
        "Month": "2022-10-01 00:00:00.000",
        "Count": "4798141"
      },
      {
        "Month": "2022-09-01 00:00:00.000",
        "Count": "5499256"
      },
      {
        "Month": "2022-08-01 00:00:00.000",
        "Count": "7273031"
      },
      {
        "Month": "2022-07-01 00:00:00.000",
        "Count": "7447384"
      },
      {
        "Month": "2022-06-01 00:00:00.000",
        "Count": "5679790"
      },
      {
        "Month": "2022-05-01 00:00:00.000",
        "Count": "6751406"
      },
      {
        "Month": "2022-04-01 00:00:00.000",
        "Count": "8315539"
      },
      {
        "Month": "2022-03-01 00:00:00.000",
        "Count": "3019688"
      },
      {
        "Month": "2022-02-01 00:00:00.000",
        "Count": "9592724"
      },
      {
        "Month": "2022-01-01 00:00:00.000",
        "Count": "12837204"
      },
      {
        "Month": "2021-12-01 00:00:00.000",
        "Count": "17948217"
      },
      {
        "Month": "2021-11-01 00:00:00.000",
        "Count": "17436053"
      },
      {
        "Month": "2021-10-01 00:00:00.000",
        "Count": "38193496"
      },
      {
        "Month": "2021-09-01 00:00:00.000",
        "Count": "16794296"
      },
      {
        "Month": "2021-08-01 00:00:00.000",
        "Count": "18263188"
      },
      {
        "Month": "2021-07-01 00:00:00.000",
        "Count": "25456764"
      },
      {
        "Month": "2021-06-01 00:00:00.000",
        "Count": "26481182"
      },
      {
        "Month": "2021-05-01 00:00:00.000",
        "Count": "46227192"
      },
      {
        "Month": "2021-04-01 00:00:00.000",
        "Count": "25893693"
      },
      {
        "Month": "2021-03-01 00:00:00.000",
        "Count": "13128693"
      },
      {
        "Month": "2021-02-01 00:00:00.000",
        "Count": "14262218"
      },
      {
        "Month": "2021-01-01 00:00:00.000",
        "Count": "11627129"
      },
      {
        "Month": "2020-12-01 00:00:00.000",
        "Count": "19750069"
      },
      {
        "Month": "2020-11-01 00:00:00.000",
        "Count": "15094407"
      },
      {
        "Month": "2020-10-01 00:00:00.000",
        "Count": "23927872"
      },
      {
        "Month": "2020-09-01 00:00:00.000",
        "Count": "14579035"
      },
      {
        "Month": "2020-08-01 00:00:00.000",
        "Count": "19580710"
      },
      {
        "Month": "2020-07-01 00:00:00.000",
        "Count": "21222533"
      },
      {
        "Month": "2020-06-01 00:00:00.000",
        "Count": "12803952"
      },
      {
        "Month": "2020-05-01 00:00:00.000",
        "Count": "14736059"
      },
      {
        "Month": "2020-04-01 00:00:00.000",
        "Count": "21219720"
      },
      {
        "Month": "2020-03-01 00:00:00.000",
        "Count": "17011623"
      },
      {
        "Month": "2020-02-01 00:00:00.000",
        "Count": "14626012"
      },
      {
        "Month": "2020-01-01 00:00:00.000",
        "Count": "14757854"
      },
      {
        "Month": "2019-12-01 00:00:00.000",
        "Count": "9521055"
      },
      {
        "Month": "2019-11-01 00:00:00.000",
        "Count": "12323846"
      },
      {
        "Month": "2019-10-01 00:00:00.000",
        "Count": "16528686"
      },
      {
        "Month": "2019-09-01 00:00:00.000",
        "Count": "10358738"
      },
      {
        "Month": "2019-08-01 00:00:00.000",
        "Count": "9775592"
      },
      {
        "Month": "2019-07-01 00:00:00.000",
        "Count": "9658047"
      },
      {
        "Month": "2019-06-01 00:00:00.000",
        "Count": "9694534"
      },
      {
        "Month": "2019-05-01 00:00:00.000",
        "Count": "6083319"
      },
      {
        "Month": "2019-04-01 00:00:00.000",
        "Count": "3288956"
      },
      {
        "Month": "2019-03-01 00:00:00.000",
        "Count": "3183229"
      },
      {
        "Month": "2019-02-01 00:00:00.000",
        "Count": "2005472"
      },
      {
        "Month": "2019-01-01 00:00:00.000",
        "Count": "860405"
      },
      {
        "Month": "2018-12-01 00:00:00.000",
        "Count": "1586446"
      },
      {
        "Month": "2018-11-01 00:00:00.000",
        "Count": "94352"
      },
      {
        "Month": "2018-10-01 00:00:00.000",
        "Count": "490573"
      },
      {
        "Month": "2018-09-01 00:00:00.000",
        "Count": "323064"
      },
      {
        "Month": "2018-08-01 00:00:00.000",
        "Count": "1857021"
      },
      {
        "Month": "2018-07-01 00:00:00.000",
        "Count": "3380168"
      },
      {
        "Month": "2018-06-01 00:00:00.000",
        "Count": "4511138"
      },
      {
        "Month": "2018-05-01 00:00:00.000",
        "Count": "4016810"
      },
      {
        "Month": "2018-04-01 00:00:00.000",
        "Count": "4530972"
      },
      {
        "Month": "2018-03-01 00:00:00.000",
        "Count": "3699452"
      },
      {
        "Month": "2018-02-01 00:00:00.000",
        "Count": "2429330"
      },
      {
        "Month": "2018-01-01 00:00:00.000",
        "Count": "3126882"
      },
      {
        "Month": "2017-12-01 00:00:00.000",
        "Count": "3157062"
      },
      {
        "Month": "2017-11-01 00:00:00.000",
        "Count": "4417721"
      },
      {
        "Month": "2017-10-01 00:00:00.000",
        "Count": "4764371"
      },
      {
        "Month": "2017-09-01 00:00:00.000",
        "Count": "4467290"
      },
      {
        "Month": "2017-08-01 00:00:00.000",
        "Count": "4380361"
      },
      {
        "Month": "2017-07-01 00:00:00.000",
        "Count": "4135873"
      },
      {
        "Month": "2017-06-01 00:00:00.000",
        "Count": "5324272"
      },
      {
        "Month": "2017-05-01 00:00:00.000",
        "Count": "5344647"
      },
      {
        "Month": "2017-04-01 00:00:00.000",
        "Count": "4280831"
      },
      {
        "Month": "2017-03-01 00:00:00.000",
        "Count": "646357"
      },
      {
        "Month": "2017-02-01 00:00:00.000",
        "Count": "1284706"
      },
      {
        "Month": "2017-01-01 00:00:00.000",
        "Count": "978066"
      },
      {
        "Month": "2016-12-01 00:00:00.000",
        "Count": "1914147"
      },
      {
        "Month": "2016-11-01 00:00:00.000",
        "Count": "2279476"
      },
      {
        "Month": "2016-10-01 00:00:00.000",
        "Count": "3240731"
      },
      {
        "Month": "2016-09-01 00:00:00.000",
        "Count": "2074262"
      },
      {
        "Month": "2016-08-01 00:00:00.000",
        "Count": "1843661"
      },
      {
        "Month": "2016-07-01 00:00:00.000",
        "Count": "1921243"
      },
      {
        "Month": "2016-06-01 00:00:00.000",
        "Count": "1217744"
      },
      {
        "Month": "2016-05-01 00:00:00.000",
        "Count": "14468"
      },
      {
        "Month": "2016-02-01 00:00:00.000",
        "Count": "877"
      },
      {
        "Month": "2016-01-01 00:00:00.000",
        "Count": "8"
      },
      {
        "Month": "2015-12-01 00:00:00.000",
        "Count": "1"
      },
      {
        "Month": "2015-09-01 00:00:00.000",
        "Count": "591"
      },
      {
        "Month": "2015-07-01 00:00:00.000",
        "Count": "459"
      },
      {
        "Month": "2014-10-01 00:00:00.000",
        "Count": "6090"
      },
      {
        "Month": "2014-06-01 00:00:00.000",
        "Count": "1959"
      },
      {
        "Month": "2014-05-01 00:00:00.000",
        "Count": "27895"
      },
      {
        "Month": "2014-03-01 00:00:00.000",
        "Count": "11138"
      },
      {
        "Month": "2014-02-01 00:00:00.000",
        "Count": "2783"
      },
      {
        "Month": "2014-01-01 00:00:00.000",
        "Count": "7913"
      },
      {
        "Month": "2013-05-01 00:00:00.000",
        "Count": "1"
      },
      {
        "Month": "2013-04-01 00:00:00.000",
        "Count": "1951"
      },
      {
        "Month": "2011-01-01 00:00:00.000",
        "Count": "2"
      },
      {
        "Month": "2010-01-01 00:00:00.000",
        "Count": "72"
      },
      {
        "Month": "2005-10-01 00:00:00.000",
        "Count": "344105"
      },
      {
        "Month": "2005-09-01 00:00:00.000",
        "Count": "1122604"
      },
      {
        "Month": "2005-08-01 00:00:00.000",
        "Count": "1950531"
      },
      {
        "Month": "2005-07-01 00:00:00.000",
        "Count": "1674267"
      },
      {
        "Month": "2005-06-01 00:00:00.000",
        "Count": "2552073"
      },
      {
        "Month": "2005-05-01 00:00:00.000",
        "Count": "2267234"
      },
      {
        "Month": "2005-04-01 00:00:00.000",
        "Count": "2573974"
      },
      {
        "Month": "2005-03-01 00:00:00.000",
        "Count": "1365000"
      },
      {
        "Month": "2005-02-01 00:00:00.000",
        "Count": "2414537"
      },
      {
        "Month": "2005-01-01 00:00:00.000",
        "Count": "4520852"
      },
      {
        "Month": "2004-12-01 00:00:00.000",
        "Count": "4614941"
      },
      {
        "Month": "2004-11-01 00:00:00.000",
        "Count": "4235617"
      },
      {
        "Month": "2004-10-01 00:00:00.000",
        "Count": "4827372"
      },
      {
        "Month": "2004-09-01 00:00:00.000",
        "Count": "4633744"
      },
      {
        "Month": "2004-08-01 00:00:00.000",
        "Count": "2665115"
      },
      {
        "Month": "2004-07-01 00:00:00.000",
        "Count": "4331054"
      },
      {
        "Month": "2004-06-01 00:00:00.000",
        "Count": "3667292"
      },
      {
        "Month": "2004-05-01 00:00:00.000",
        "Count": "4312264"
      },
      {
        "Month": "2004-04-01 00:00:00.000",
        "Count": "4573202"
      },
      {
        "Month": "2004-03-01 00:00:00.000",
        "Count": "3670513"
      },
      {
        "Month": "2004-02-01 00:00:00.000",
        "Count": "3073794"
      },
      {
        "Month": "2004-01-01 00:00:00.000",
        "Count": "4113920"
      },
      {
        "Month": "2003-12-01 00:00:00.000",
        "Count": "3083304"
      },
      {
        "Month": "2003-11-01 00:00:00.000",
        "Count": "2718956"
      },
      {
        "Month": "2003-10-01 00:00:00.000",
        "Count": "2580266"
      },
      {
        "Month": "2003-09-01 00:00:00.000",
        "Count": "2321554"
      },
      {
        "Month": "2003-08-01 00:00:00.000",
        "Count": "2398360"
      },
      {
        "Month": "2003-07-01 00:00:00.000",
        "Count": "2156836"
      },
      {
        "Month": "2003-06-01 00:00:00.000",
        "Count": "3501215"
      },
      {
        "Month": "2003-05-01 00:00:00.000",
        "Count": "2473287"
      },
      {
        "Month": "2003-04-01 00:00:00.000",
        "Count": "3385986"
      },
      {
        "Month": "2003-03-01 00:00:00.000",
        "Count": "2961623"
      },
      {
        "Month": "2003-02-01 00:00:00.000",
        "Count": "2216334"
      },
      {
        "Month": "2003-01-01 00:00:00.000",
        "Count": "970139"
      },
      {
        "Month": "2002-12-01 00:00:00.000",
        "Count": "1473488"
      },
      {
        "Month": "2002-11-01 00:00:00.000",
        "Count": "1080017"
      },
      {
        "Month": "2002-10-01 00:00:00.000",
        "Count": "1380603"
      },
      {
        "Month": "2002-09-01 00:00:00.000",
        "Count": "1314587"
      },
      {
        "Month": "2002-08-01 00:00:00.000",
        "Count": "616545"
      },
      {
        "Month": "2002-07-01 00:00:00.000",
        "Count": "1258833"
      },
      {
        "Month": "2002-06-01 00:00:00.000",
        "Count": "3718585"
      },
      {
        "Month": "2002-05-01 00:00:00.000",
        "Count": "1412691"
      },
      {
        "Month": "2002-04-01 00:00:00.000",
        "Count": "716930"
      },
      {
        "Month": "2002-03-01 00:00:00.000",
        "Count": "189882"
      },
      {
        "Month": "2002-02-01 00:00:00.000",
        "Count": "299"
      },
      {
        "Month": "2002-01-01 00:00:00.000",
        "Count": "8"
      },
      {
        "Month": "2001-12-01 00:00:00.000",
        "Count": "1"
      },
      {
        "Month": "2001-11-01 00:00:00.000",
        "Count": "336482"
      },
      {
        "Month": "2001-10-01 00:00:00.000",
        "Count": "6"
      },
      {
        "Month": "2001-09-01 00:00:00.000",
        "Count": "4"
      },
      {
        "Month": "2001-08-01 00:00:00.000",
        "Count": "2"
      },
      {
        "Month": "2001-07-01 00:00:00.000",
        "Count": "233"
      },
      {
        "Month": "2001-05-01 00:00:00.000",
        "Count": "11"
      },
      {
        "Month": "2001-04-01 00:00:00.000",
        "Count": "11"
      },
      {
        "Month": "2001-03-01 00:00:00.000",
        "Count": "9432"
      },
      {
        "Month": "2001-01-01 00:00:00.000",
        "Count": "168940"
      },
      {
        "Month": "2000-12-01 00:00:00.000",
        "Count": "29864"
      },
      {
        "Month": "2000-11-01 00:00:00.000",
        "Count": "4"
      },
      {
        "Month": "2000-10-01 00:00:00.000",
        "Count": "6430"
      },
      {
        "Month": "2000-09-01 00:00:00.000",
        "Count": "36"
      },
      {
        "Month": "2000-08-01 00:00:00.000",
        "Count": "4"
      },
      {
        "Month": "2000-07-01 00:00:00.000",
        "Count": "43987"
      },
      {
        "Month": "2000-04-01 00:00:00.000",
        "Count": "2"
      },
      {
        "Month": "2000-03-01 00:00:00.000",
        "Count": "174"
      },
      {
        "Month": "2000-02-01 00:00:00.000",
        "Count": "132866"
      },
      {
        "Month": "2000-01-01 00:00:00.000",
        "Count": "227722"
      },
      {
        "Month": "1999-12-01 00:00:00.000",
        "Count": "23267"
      },
      {
        "Month": "1999-10-01 00:00:00.000",
        "Count": "3"
      },
      {
        "Month": "1999-09-01 00:00:00.000",
        "Count": "210"
      },
      {
        "Month": "1999-08-01 00:00:00.000",
        "Count": "2"
      },
      {
        "Month": "1999-06-01 00:00:00.000",
        "Count": "147"
      },
      {
        "Month": "1995-04-01 00:00:00.000",
        "Count": "6"
      },
      {
        "Month": "1986-01-01 00:00:00.000",
        "Count": "13"
      },
      {
        "Month": "1983-02-01 00:00:00.000",
        "Count": "2"
      },
      {
        "Month": "1981-08-01 00:00:00.000",
        "Count": "3"
      },
      {
        "Month": "1980-01-01 00:00:00.000",
        "Count": "20"
      },
      {
        "Month": "1970-01-01 00:00:00.000",
        "Count": "22"
      },
      {
        "Month": "1963-05-01 00:00:00.000",
        "Count": "2"
      },
      {
        "Month": "1963-03-01 00:00:00.000",
        "Count": "17"
      },
      {
        "Month": "1621-11-01 00:00:00.000",
        "Count": "1"
      },
      {
        "Month": "1618-05-01 00:00:00.000",
        "Count": "1"
      },
      {
        "Month": "1611-10-01 00:00:00.000",
        "Count": "1"
      },
      {
        "Month": "1609-04-01 00:00:00.000",
        "Count": "1"
      },
      {
        "Month": "1605-02-01 00:00:00.000",
        "Count": "1"
      },
      {
        "Month": "1601-11-01 00:00:00.000",
        "Count": "1"
      },
      {
        "Month": "1601-01-01 00:00:00.000",
        "Count": "166"
      }
    ],
    "ActiveProvider": "true"
  },
  {
    "Provider": "SB2030",
    "RecordCount": "1280424",
    "PlatformCount": "5",
    "MinDateTime": "2022-07-13 06:00:38.349",
    "MaxDateTime": "2024-01-10 10:29:47.000",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "MokiMak",
        "Count": "1267662",
        "FirstSubmission": "2024-01-29",
        "LastSubmission": "2024-01-29"
      },
      {
        "Platform": "PalauVessel4",
        "Count": "4693",
        "FirstSubmission": "2025-03-11",
        "LastSubmission": "2025-03-11"
      },
      {
        "Platform": "PalauVessel1",
        "Count": "3627",
        "FirstSubmission": "2025-03-11",
        "LastSubmission": "2025-03-11"
      },
      {
        "Platform": "PalauVessel3",
        "Count": "3120",
        "FirstSubmission": "2025-03-11",
        "LastSubmission": "2025-03-11"
      },
      {
        "Platform": "PalauVessel6",
        "Count": "1322",
        "FirstSubmission": "2025-03-11",
        "LastSubmission": "2025-03-11"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2024-01-01 00:00:00.000",
        "Count": "622"
      },
      {
        "Month": "2023-12-01 00:00:00.000",
        "Count": "1356"
      },
      {
        "Month": "2023-11-01 00:00:00.000",
        "Count": "921"
      },
      {
        "Month": "2023-10-01 00:00:00.000",
        "Count": "657"
      },
      {
        "Month": "2023-07-01 00:00:00.000",
        "Count": "1031"
      },
      {
        "Month": "2023-06-01 00:00:00.000",
        "Count": "327"
      },
      {
        "Month": "2023-05-01 00:00:00.000",
        "Count": "1439"
      },
      {
        "Month": "2023-04-01 00:00:00.000",
        "Count": "283"
      },
      {
        "Month": "2023-03-01 00:00:00.000",
        "Count": "593"
      },
      {
        "Month": "2023-02-01 00:00:00.000",
        "Count": "156"
      },
      {
        "Month": "2023-01-01 00:00:00.000",
        "Count": "368"
      },
      {
        "Month": "2022-12-01 00:00:00.000",
        "Count": "396"
      },
      {
        "Month": "2022-11-01 00:00:00.000",
        "Count": "4418"
      },
      {
        "Month": "2022-09-01 00:00:00.000",
        "Count": "1267776"
      },
      {
        "Month": "2022-07-01 00:00:00.000",
        "Count": "81"
      }
    ],
    "ActiveProvider": "false"
  },
  {
    "Provider": "SeaKeepers",
    "RecordCount": "26239271",
    "PlatformCount": "20",
    "MinDateTime": "2005-03-24 01:03:59.000",
    "MaxDateTime": "2025-05-26 17:17:14.000",
    "PlatformCounts": [
      {
        "Platform": "platform_name",
        "Count": "record_count",
        "FirstSubmission": "first_submission",
        "LastSubmission": "last_submission"
      },
      {
        "Platform": "UNKNOWN",
        "Count": "8191721",
        "FirstSubmission": "2024-08-26",
        "LastSubmission": "2025-04-06"
      },
      {
        "Platform": "Spirit of NZ",
        "Count": "8184738",
        "FirstSubmission": "2025-04-14",
        "LastSubmission": "2025-04-17"
      },
      {
        "Platform": "Sorrento",
        "Count": "2642185",
        "FirstSubmission": "2025-02-12",
        "LastSubmission": "2025-02-13"
      },
      {
        "Platform": "Neo",
        "Count": "1353370",
        "FirstSubmission": "2025-03-10",
        "LastSubmission": "2025-03-23"
      },
      {
        "Platform": "Nereus",
        "Count": "1296096",
        "FirstSubmission": "2025-03-21",
        "LastSubmission": "2025-03-21"
      },
      {
        "Platform": "Moondance",
        "Count": "1070723",
        "FirstSubmission": "2025-01-28",
        "LastSubmission": "2025-01-29"
      },
      {
        "Platform": "Prime Time",
        "Count": "934596",
        "FirstSubmission": "2024-11-19",
        "LastSubmission": "2025-05-26"
      },
      {
        "Platform": "Discovery",
        "Count": "567602",
        "FirstSubmission": "2024-02-27",
        "LastSubmission": "2024-04-21"
      },
      {
        "Platform": "Diversion",
        "Count": "548271",
        "FirstSubmission": "2025-03-08",
        "LastSubmission": "2025-03-08"
      },
      {
        "Platform": "Nyla",
        "Count": "386910",
        "FirstSubmission": "2025-04-06",
        "LastSubmission": "2025-04-06"
      },
      {
        "Platform": "E-Cruz",
        "Count": "376760",
        "FirstSubmission": "2025-03-09",
        "LastSubmission": "2025-03-09"
      },
      {
        "Platform": "Dare to Dream",
        "Count": "194917",
        "FirstSubmission": "2025-04-05",
        "LastSubmission": "2025-04-05"
      },
      {
        "Platform": "Aventura",
        "Count": "124282",
        "FirstSubmission": "2025-05-09",
        "LastSubmission": "2025-05-09"
      },
      {
        "Platform": "Patea",
        "Count": "112338",
        "FirstSubmission": "2025-05-09",
        "LastSubmission": "2025-05-09"
      },
      {
        "Platform": "Warrior",
        "Count": "83336",
        "FirstSubmission": "2025-02-10",
        "LastSubmission": "2025-02-11"
      },
      {
        "Platform": "MV Duchess",
        "Count": "76820",
        "FirstSubmission": "2025-03-27",
        "LastSubmission": "2025-05-06"
      },
      {
        "Platform": "TT Dione Sun",
        "Count": "68916",
        "FirstSubmission": "2025-03-07",
        "LastSubmission": "2025-03-08"
      },
      {
        "Platform": "MV Athena",
        "Count": "10740",
        "FirstSubmission": "2025-05-24",
        "LastSubmission": "2025-05-25"
      },
      {
        "Platform": "Yeva",
        "Count": "8784",
        "FirstSubmission": "2025-02-14",
        "LastSubmission": "2025-02-14"
      },
      {
        "Platform": "Seakeeper 4 - CSBWG16 Demo",
        "Count": "6166",
        "FirstSubmission": "2025-03-24",
        "LastSubmission": "2025-03-24"
      }
    ],
    "MonthlyCounts": [
      {
        "Month": "month",
        "Count": "record_count"
      },
      {
        "Month": "2025-05-01 00:00:00.000",
        "Count": "66914"
      },
      {
        "Month": "2025-03-01 00:00:00.000",
        "Count": "696014"
      },
      {
        "Month": "2025-02-01 00:00:00.000",
        "Count": "400100"
      },
      {
        "Month": "2025-01-01 00:00:00.000",
        "Count": "259200"
      },
      {
        "Month": "2024-12-01 00:00:00.000",
        "Count": "279465"
      },
      {
        "Month": "2024-11-01 00:00:00.000",
        "Count": "329612"
      },
      {
        "Month": "2024-10-01 00:00:00.000",
        "Count": "4210513"
      },
      {
        "Month": "2024-09-01 00:00:00.000",
        "Count": "5097307"
      },
      {
        "Month": "2024-08-01 00:00:00.000",
        "Count": "623011"
      },
      {
        "Month": "2024-07-01 00:00:00.000",
        "Count": "726382"
      },
      {
        "Month": "2024-06-01 00:00:00.000",
        "Count": "2300866"
      },
      {
        "Month": "2024-05-01 00:00:00.000",
        "Count": "6305608"
      },
      {
        "Month": "2024-04-01 00:00:00.000",
        "Count": "881438"
      },
      {
        "Month": "2024-03-01 00:00:00.000",
        "Count": "838708"
      },
      {
        "Month": "2024-02-01 00:00:00.000",
        "Count": "521522"
      },
      {
        "Month": "2024-01-01 00:00:00.000",
        "Count": "1115155"
      },
      {
        "Month": "2023-12-01 00:00:00.000",
        "Count": "378588"
      },
      {
        "Month": "2023-11-01 00:00:00.000",
        "Count": "128520"
      },
      {
        "Month": "2023-10-01 00:00:00.000",
        "Count": "590542"
      },
      {
        "Month": "2023-09-01 00:00:00.000",
        "Count": "16810"
      },
      {
        "Month": "2023-08-01 00:00:00.000",
        "Count": "46056"
      },
      {
        "Month": "2023-07-01 00:00:00.000",
        "Count": "30687"
      },
      {
        "Month": "2023-05-01 00:00:00.000",
        "Count": "283915"
      },
      {
        "Month": "2005-07-01 00:00:00.000",
        "Count": "49658"
      },
      {
        "Month": "2005-06-01 00:00:00.000",
        "Count": "47977"
      },
      {
        "Month": "2005-05-01 00:00:00.000",
        "Count": "10592"
      },
      {
        "Month": "2005-03-01 00:00:00.000",
        "Count": "4111"
      }
    ],
    "ActiveProvider": "true"
  }
]
print (json.dumps(msg, indent=2))