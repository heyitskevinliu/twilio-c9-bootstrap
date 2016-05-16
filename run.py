from flask import Flask, request, redirect
import twilio.twiml
import requests
import json
from pprint import pprint
import socket

config_file = open('../config.json','r')
config = json.load(config_file)

ACCOUNT_SID = config['account_sid']
AUTH_TOKEN = config['auth_token']

app = Flask(__name__)

numbers = ['+16507401706', '+14153504316']
@app.route('/sms', methods=['GET', 'POST'])
def sms():

        return """<?xml version="1.0" encoding="UTF-8"?>
        <Response>
        <Sms to="+16507401706">Hello it's Kevin</Sms>
        </Response>"""


@app.route('/messages')
def show_messages():
    api = "https://api.twilio.com/2010-04-01" 
    uri = "/Accounts/" + ACCOUNT_SID + "/Messages.json?PageSize=1&Page=0"
    credentials = (ACCOUNT_SID, AUTH_TOKEN)
    response = requests.get(api + uri, auth=credentials)
    messages = json.loads(response.content)
    pprint (messages)
    return str(messages)
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
