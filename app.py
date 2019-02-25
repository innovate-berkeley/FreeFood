from flask import Flask, jsonify
from twilio.rest import Client

account_sid = 'AC0f1074a007138b64c7b1b5568afa9486'
auth_token = 'b01683d2e9a56d5e43d71c3bb6eb7bc1'
client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/test', methods=['POST'])
def test_message():
   pass

if __name__ == '__main__':
    app.run(debug=True)