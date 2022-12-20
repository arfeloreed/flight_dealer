import requests
import os
from datetime import datetime, timedelta

kiwi_api_key = os.environ.get("KIWI_API_KEY")
kiwi_endpoint = "https://api.tequila.kiwi.com/v2/search"
header = {"apikey": kiwi_api_key}
date = datetime.now() + timedelta(days=1)


class FlightData:
    """This class is responsible for structuring the flight data."""
    def __init__(self, destinations: dict):
        """Initialize the attributes for FlightData"""
        self.departure_from = "GES"
        self.destinations = destinations
        self.date_from = date.strftime("%d/%m/%Y")
        self.date_to = (date + timedelta(days=60)).strftime("%d/%m/%Y")

    def search_flight(self):
        """search available flights from departure city to destination"""
        prices = []
        for destination in self.destinations:
            city = {}
            data_info = {}
            search_params = {
                "fly_from": self.departure_from,
                "fly_to": self.destinations[destination],
                "date_from": self.date_from,
                "date_to": self.date_to,
            }
            response = requests.get(url=kiwi_endpoint, params=search_params, headers=header)
            response.raise_for_status()
            data = response.json()["data"][0]
            price = data['price'] * 58.81
            data_info["price"] = round(price)
            data_info["city_from"] = data["cityFrom"]
            data_info["airport_from"] = data["flyFrom"]
            data_info["airport_to"] = data["flyTo"]
            flight_on = data["local_departure"].split("T")
            data_info["date"] = flight_on[0]
            data_info["airlines"] = data["airlines"]
            city[destination] = data_info
            prices.append(city)
        return prices
