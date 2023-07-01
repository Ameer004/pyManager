from twilio.rest import Client
from flask import Flask, request

account_sid = 'ACe962575bbc7d2f512fb6dd127cd027fd'
auth_token = 'b5d9bd2491d281f8c1ec40345fc214b2'
client = Client(account_sid, auth_token)

def send_message(to, body):
    message = client.messages.create(
        body=body,
        from_='+14155238886',
        to=to
    )
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    message_body = request.form['Body']
    sender_number = request.form['From']
     # Process the received message and send a response
    if message_body.lower() == 'hello':
        response = "Hi there!"
    else:
        response = "Sorry, I don't understand."
    
    send_message(sender_number, response)
    
    return '', 200

if __name__ == '__main__':
    app.run()