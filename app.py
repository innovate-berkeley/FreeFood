from flask import Flask, jsonify, request
from twilio.rest import Client
import sys, os

from dotenv import load_dotenv
load_dotenv()

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
phone_number = os.getenv("PHONE_NUMBER")

client = Client(account_sid, auth_token)

app = Flask(__name__)

def get_numbers():
   return ["+17706811621", "+16508620505", "+19168059032"]

for number in get_numbers():
   validation_request = client.validation_requests \
                        .create(
                              friendly_name='',
                              phone_number=number
                           )
   print(validation_request)

@app.route('/')
def index():
   return "Hello, World!"

@app.route('/test', methods = ['POST'])
def test_mass_message():
   text = request.args.get("message", default = "Yo")
   for number in get_numbers():
      message = client.messages.create(
      to=number, 
      from_=phone_number,
      body=text)
   return message.sid

def add_number():
   pass


if __name__ == '__main__':
    app.run(debug=True)