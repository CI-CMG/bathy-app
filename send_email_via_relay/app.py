"""
send notification via email that order is complete

uses a mail proxy running in VPC to circumvent problems with NOAA blocking
messages directly from SES

triggered by SQS message and expects payload like:
  {
    "message": "Your data request is ready and can be downloaded from https://order-pickup.s3.amazonaws.com/6e49a131-9d2f-422c-9c4c-0ae386a905fc.csv.\nThe data will be available until August 14, 2024.",
    "email": "user@example.com"
  }

An empty email address indicates that no email is to be sent
"""

import smtplib
import os
import json
import logging

# email proxy address
SMTP_HOST = '10.58.150.68'
SMTP_PORT = 25
TABLE = os.getenv('ORDERS_TABLE', default='bathy-orders')
SENDER_ADDRESS = os.getenv("SENDER", 'mb.info@noaa.gov')

server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGLEVEL", "WARNING"))


def send_email(recipient, message):
    email = f"""From: NCEI/DCDB Bathymetry Data Manager <{SENDER_ADDRESS}>
To: {recipient}
Subject: Bathymetry Data Request

{message}
"""
    server.connect(host=SMTP_HOST, port=SMTP_PORT)
    server.sendmail(SENDER_ADDRESS, recipient, email)
    server.quit()


def lambda_handler(event, context):
    for record in event['Records']:
        body = json.loads(record['body'])
        recipient = body['email']
        msg = body['message']
        if recipient:
            logger.info('sending email to ' + recipient)
            send_email(recipient, msg)
        else:
            logger.info('no email specified, notification will not be sent')
