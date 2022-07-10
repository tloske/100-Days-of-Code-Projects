from datetime import datetime
from urllib.error import HTTPError
import requests
import string
from random import choice


class DataUploader:
    pixela_endpoint = "https://pixe.la/v1/users"

    def __init__(self, username=None, token=None, graph_id=None):
        self.username = username
        self.token = token
        self.graph_id = graph_id
        self.headers = {
            "X-USER-TOKEN": self.token,
        }

    def login(self, username: str, token: str) -> None:
        """Changes the username and token"""
        self.username = username
        self.token = token

    def change_graph(self, graph_id: str) -> None:
        """Changes the current graph to a different graph"""
        self.graph_id = graph_id

    def upload_hours(self, hours: str):
        """Uploads the current hours to the graph"""
        date = datetime.today().strftime("%Y%m%d")

        pixel_endpoint = f"{self.pixela_endpoint}/{self.username}/graphs/{self.graph_id}/{date}"

        try:
            response = requests.get(pixel_endpoint, headers=self.headers)
            response.raise_for_status()
            pixel_quantity = float(response.json()['quantity'])
        except requests.exceptions.HTTPError:
            pixel_quantity = 0

        pixel_params = {
            "date": date,
            "quantity": f"{hours + pixel_quantity}",
        }

        response = requests.put(
            pixel_endpoint, json=pixel_params, headers=self.headers)
        response.raise_for_status()

    def create_new_graph(self, graph_id: str, graph_name: str, units: str) -> dict:
        """Creates a new graph and returns a dictionary with the relevant data"""
        graph_endpoint = f"{self.pixela_endpoint}/{self.username}/graphs"

        graph_config = {
            "id": graph_id,
            "name": graph_name,
            "unit": units,
            "type": "float",
            "color": "kuro",
        }
        response = requests.post(
            graph_endpoint, json=graph_config, headers=self.headers)
        response.raise_for_status()

        return {"id": graph_id, "name": graph_name, "link": f"{self.pixela_endpoint}/{self.username}/graphs/{graph_id}.html"}

    def delete_graph(self):
        """Deletes the current Graph"""
        graph_endpoint = f"{self.pixela_endpoint}/{self.username}/graphs/{self.graph_id}"

        response = requests.delete(graph_endpoint, headers=self.headers)
        response.raise_for_status()

    def create_new_user(self, username: str, token: str = None) -> dict:
        """Creates a new user, if no token is given a token is generated"""
        if token is None:
            token = self.generate_token()
        params = {
            "token": token,
            "username": username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }

        response = requests.post(url=self.pixela_endpoint, json=params)
        response.raise_for_status()
        self.token = token
        self.username = username

        return {"token": token, "username": username, "graphs": []}

    def generate_token(self) -> str:
        """Generates a token"""
        symbol_list = string.ascii_lowercase + string.digits
        token = ""
        for _ in range(128):
            token += choice(symbol_list)

        print(token)
