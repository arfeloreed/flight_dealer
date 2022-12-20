from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# manage the sheet data
data = DataManager()
sheet_data = data.data["prices"]
country_lists = [sheet_data[n]["city"] for n in range(len(sheet_data))]
country_codes = {sheet_data[n]["city"]: sheet_data[n]["iataCode"] for n in range(len(sheet_data))}

# make a flight search object and get iata codes for cities
# search_flight = FlightSearch(country_lists)
# iata_codes = search_flight.respond()

# i = 2
# for country in iata_codes:
#     data.edit_iata_codes(iata_codes[country], i)
#     i += 1

# query for prices
prices_data = FlightData(country_codes)
flight_info = prices_data.search_flight()

# send notification
# message = NotificationManager(my_data=sheet_data, flight_data=flight_info)
# message.calculate_prices()
pprint(flight_info)
