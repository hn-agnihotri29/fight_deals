import requests
from pprint import pprint
from flight_data import FlightData
from datetime import datetime, timedelta

KIWI_ENDPOINT = "KIWI_API"
KIWI_API_KEY = "KIWI_API_KEY"

headers = {
    "apikey": KIWI_API_KEY,
}
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def destination_code(self, city):
        query = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=f"{KIWI_ENDPOINT}/locations/query", params=query, headers=headers)
        code = response.json()["locations"][0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        destination_param = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=f"{KIWI_ENDPOINT}/v2/search", headers=headers, params=destination_param)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(price=data["price"],
                                 origin_city=data["cityFrom"],
                                 origin_airport=data["flyFrom"],
                                 destination_city=data["cityTo"],
                                 destination_airport=data["flyTo"],
                                 out_date=data["local_departure"].split("T")[0],
                                 return_date=data["local_departure"].split("T")[0]
                                 )

        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
