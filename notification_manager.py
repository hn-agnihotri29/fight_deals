from twilio.rest import Client

ACCOUNT_ID = "TWILIO_ACCOUNT_ID"
AUTH_TOKEN = "TOKEN"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(ACCOUNT_ID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
           body=message,
           from_="+19786784065",
           to="WRITE_NUMBER"
        )
        print(message.sid)



