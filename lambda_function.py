from __future__ import print_function
from twilio import twiml
from twilio.rest import Client
import json

client = Client("<your twilio account sid>", "<your auth token>")

def lambda_handler(event, context):
    print("this is the event passed to lambda_handler: ",   json.dumps(event))
    print("parameters",   event['to_number'], event['from_number'], event["message"])
    client.messages.create(to=event['to_number'], from_=event['from_number'], body=event['message'])
    return "message sent"

