from twilio.rest import Client

ACCOUNT_ID = "ACe6c9ff434ad5a8cf19e2a2772247b65f"
AUTH_TOKEN = "9cfc444224ef4569c2249b3fcf602422"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(ACCOUNT_ID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
           body=message,
           from_="+19786784065",
           to="+919431447302"
        )
        print(message.sid)



