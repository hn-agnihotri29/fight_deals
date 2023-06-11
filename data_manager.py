from pprint import pprint
import requests

SHEET_ENDPOINT = "https://api.sheety.co/7b7bee4fa09d73f6d9d7b73186650994/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination = {}

    def get_destination(self):
        response = requests.get(url=SHEET_ENDPOINT)
        data = response.json()
        self.destination = data["prices"]
        return self.destination

    def update_destination_code(self, code, city):
        new_data = {
            "price": {
                "iataCode": code
            }
        }
        response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", json=new_data)
        print(response.text)










