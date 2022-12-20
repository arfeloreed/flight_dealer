import os
import requests

SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
PROJECT_ID = "cheapFlight"
SHEET_NAME = "prices"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{PROJECT_ID}/{SHEET_NAME}"
header = {
    "Authorization": os.environ.get("SHEETY_AUTHORIZATION"),
}


class DataManager:
    """A class made to access the related Google sheet for the project"""
    def __init__(self):
        """Initialize the attributes for DataManager"""
        self.response = requests.get(url=SHEETY_ENDPOINT, headers=header)
        self.data = self.response.json()

    def edit_iata_codes(self, iata_code, n):
        """edits or adds codes for iata codes column"""
        edit_params = {
            "price": {
                "iataCode": f"{iata_code}",
            }
        }
        edit_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/{PROJECT_ID}/{SHEET_NAME}/{n}"
        response = requests.put(url=edit_endpoint, headers=header, json=edit_params)
