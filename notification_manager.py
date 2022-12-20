import os
from twilio.rest import Client

twilio_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_TOKEN")
twilio_number = os.environ.get("TWILIO_NUMBER")
client = Client(twilio_sid, auth_token)


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self, my_data: list, flight_data: list):
        """initialize the attributes for NotificationManager"""
        self.sheet_data = my_data
        self.flight_data = flight_data

    def calculate_prices(self):
        """compares if the price ticket is lower than the price in sheet data"""
        for i in range(len(self.sheet_data)):
            base = self.flight_data[i][self.sheet_data[i]["city"]]
            ticket_price = base["price"]
            if ticket_price < self.sheet_data[i]["lowestPrice"]:
                print(f"you have to fly to {self.sheet_data[i]['city']}")
                message = client.messages.create(
                    body=f"Low price alert! Only ₱{ticket_price} to fly from {base['city_from']}-{base['airport_from']}"
                         f" to {self.sheet_data[i]['city']}-{base['airport_to']} on {base['date']}. Carrier is "
                         f"{base['airlines']} airline.",
                    from_=twilio_number,
                    to=os.environ.get("PHONE_NUMBER"),
                )
                print(message.status)
