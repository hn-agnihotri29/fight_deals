from pprint import pprint
from flight_search import FlightSearch
from datetime import datetime, timedelta
from data_manager import DataManager
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

ORIGIN_LOC_CODE = 'LON'

data_manager = DataManager()
sheet_data = data_manager.get_destination()
flight_search = FlightSearch()
notification_manager = NotificationManager()

for city_name in sheet_data:
    code = flight_search.destination_code(city_name["city"])
    data_manager.update_destination_code(code, city_name)

sheet_data = data_manager.get_destination()
pprint(sheet_data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_LOC_CODE,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    try:
        if flight.price < destination["lowestPrice"]:
            notification_manager.send_sms(message=f"Low price alert! Only £{flight.price} to fly from "
                                                  f"{flight.origin_city}-{flight.origin_airport}"
                                                  f"to{flight.destination_city}-{flight.destination_airport},"
                                                  f"from{flight.out_date} to {flight.return_date}")
    except AttributeError:
        print(f"No message is sent since the flight for {destination['city']} is not available")
