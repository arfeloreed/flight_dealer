import requests
import os

kiwi_api_key = os.environ.get("KIWI_API_KEY")
kiwi_endpoint = "https://api.tequila.kiwi.com/locations/query"


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self, list_countries):
        """initialize the attributes for FlightSearch"""
        self.airport_list = list_countries

    def respond(self):
        """return testing for the IATA code query"""
        country_code = {}
        for country in self.airport_list:
            kiwi_params = {
                "term": country,
                "locale": "en-US",
                "location_types": "airport",
            }
            kiwi_header = {
                "apikey": kiwi_api_key,
            }
            response = requests.get(url=kiwi_endpoint, params=kiwi_params, headers=kiwi_header)
            response.raise_for_status()
            airport_data = response.json()["locations"][0]["city"]["code"]
            country_code[country] = airport_data
        return country_code
